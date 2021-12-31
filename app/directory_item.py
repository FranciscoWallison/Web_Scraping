from urllib.request import urlopen
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import pandas as pd
import time

file_path = "inst_text/item/item_db_re_usable.txt"
# TRADUZINDO O BANCO 
file_path_new = "inst_text/item_db_re_usable_new.txt"
path_new = open(file_path_new, "wt")

# CRIANDO SQL COM OS DADOS DO SITE
file_path_item_new = "db_extra/create_scrapin/item_description_re_usable.txt"
path_item_new = open(file_path_item_new, "wt")

with open(file_path) as f:
    lines = f.readlines() ##Assume the sample file has 3 lines
    # first = lines.split('\n', 1)[0]

for idx, i in enumerate(lines):
    index = idx+1
    porcentagemtotal =  ((index / len(lines)) * 100)
    print("Quantidade: ", len(lines), " Atual:", index , " Completo:", porcentagemtotal,"% " )
    campos_valores = i.split(" VALUES ")
    valores = campos_valores[1].split(",")
    id_name_item = valores[1]
    id_name_item_url = id_name_item.replace("\\\'s", '').replace('\\', '').replace("'s", '').replace('\'', '')
    type_item = ''

    # SELECT type, count(*)
    # FROM item_db_re 
    # GROUP by type
    # ORDER BY type

    if valores[3] == "'Weapon'" or valores[3] == "'Petarmor'" or valores[3] == "'Ammo'":
        type_item = "armamentos"
    if valores[3] == "'Poring_Egg'" or valores[3] == "'Armor'" or valores[3] == "'Petegg'" or valores[3] == "'Petarmor'" : 
        type_item = "equipamentos"
    if valores[3] == "'Card'":
        type_item = "itens-slot"
    if valores[3] == "'Cash'" or valores[3] == "'Delayconsume'" or valores[3] == "'Etc'" or valores[3] == "'Healing'" or valores[3] == "'Usable'": 
        type_item = "itens"
    if valores[3] == "'Shadowgear'":  # não achei categoria para esse item
        print("'Shadowgear'", id_name_item_url)
        path_new.write(i) # NÃO SEI QUAL O TIPO  
        continue
    
    url = "https://playragnarokonlinebr.com/database/thor/"+type_item.replace('\'', '')+"/detalhes/"+ id_name_item_url.replace('\'', '')
    print(url, id_name_item_url, id_name_item)
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    # print(valores[3])
    # print(id_name_item, id_name_item_url)
    
    try:
        time.sleep(1)
        html = urlopen(req).read()
    except HTTPError as e:
        time.sleep(3)
        if e.code == 500:
            path_new.write(i) # O ITEM NÃO FOI ACHADO OU NÃO EXISTE
            print(e.code)
            print(url)
            continue
        # html = urlopen(req).read()
        print("----- ERROR-----")
        print(e.code, id_name_item_url, type_item.replace('\'', ''))
        print(url)
        path_new.write(i) # O ITEM NÃO FOI ACHADO OU NÃO EXISTE
        continue

    bs = BeautifulSoup(html, 'html.parser')
    linhas = bs.find('main', {'id':'itens-main'})

    linhaNome = bs.find('article',{'class':'items-emphasis'})
    try:
        if(len(linhaNome.findChildren("h1")) == 0):
            print("----- NÃO TEM -----")
            print(url)        
            path_new.write(i) #  O ITEM NÃO FOI ACHADO OU NÃO EXISTE
        else:
            print("----- "+type_item.capitalize()+" -----")
            nome_traduzido = linhaNome.findChildren("h1")[0].text.replace(" [4]", "").replace(" [3]", "").replace(" [2]", "").replace(" [1]", "")
            id_item = valores[0].replace("(", "")
            print(id_item, "- Nome: ", nome_traduzido)
            newLine = i.replace(""+valores[1]+","+valores[2]+"", ""+valores[1]+',"'+nome_traduzido+'"')        
            path_new.write(newLine) # TRADUZINDO A LINHA 
            print("----- Descrição -----")
            descricao_iteminfor = bs.find_all('meta',{'name':'description'})[0]['content']
            print(descricao_iteminfor)

            print("----- Informações -----") 
            informacoes = bs.find_all('ul',{'class':'list'})[0]
            # Preço
            preco = informacoes.findChildren("li")[1].text.replace('.', '').replace('zeny', '').replace(' ', '')
            print(informacoes.findChildren("li")[0].text, preco + " zeny")
            # Peso
            peso = informacoes.findChildren("li")[3].text
            print(informacoes.findChildren("li")[2].text, preco)

            print("----- Pode ser... -----")
            pode_ser = bs.find_all('ul',{'class':'flex-check'})[0]
            # Jogado no chão
            jogado_chao = 'true' if "POSITIVE" in pode_ser.findChildren("li")[0].findAll('img')[0]['src'] else 'false'
            print(pode_ser.findChildren("li")[1].text, jogado_chao)
            # Guardado no carrinho
            guardado_carrinho = 'true' if "POSITIVE" in pode_ser.findChildren("li")[2].findAll('img')[0]['src'] else 'false'
            print(pode_ser.findChildren("li")[3].text, guardado_carrinho)
            # Negociado
            negociado = 'true' if "POSITIVE" in pode_ser.findChildren("li")[4].findAll('img')[0]['src'] else 'false'
            print(pode_ser.findChildren("li")[5].text, negociado)
            # Vendido para NPC
            vendido_npc = 'true' if "POSITIVE" in pode_ser.findChildren("li")[6].findAll('img')[0]['src'] else 'false'
            print(pode_ser.findChildren("li")[7].text, vendido_npc)
            # Colocado no armazém
            colocado_armazem = 'true' if "POSITIVE" in pode_ser.findChildren("li")[8].findAll('img')[0]['src'] else 'false'
            print(pode_ser.findChildren("li")[9].text, colocado_armazem)
            # Colocado no armazém da guilda
            colocado_armazem_guilda = 'true' if "POSITIVE" in pode_ser.findChildren("li")[10].findAll('img')[0]['src'] else 'false'
            print(pode_ser.findChildren("li")[11].text, colocado_armazem_guilda)

            sql_inset_description = "REPLACE INTO `item_description` "
            sql_inset_description = sql_inset_description +"(`id_item`,`name_aegis`,`nome_traduzido`,`description`,`preco`,`peso`,`jogado_chao`,`guardado_carrinho`,`negociado`,`vendido_npc`,`colocado_armazem`,`colocado_armazem_guilda`) VALUES ("
            sql_inset_description = sql_inset_description + ""+id_item +"," +valores[1]+",'"+nome_traduzido+ "','"+descricao_iteminfor+"',"+preco+","+peso+","+jogado_chao+","+guardado_carrinho+","+negociado+","+vendido_npc+","+colocado_armazem+","+colocado_armazem_guilda+");"
            path_item_new.write(sql_inset_description) # CRIANDO SQL COM OS DADOS DO SITE
    
    except Exception as e:
        print("----- ERROR-----")
        print(e, id_name_item_url, type_item.replace('\'', ''))
        print(url)
        path_new.write(i) # O ITEM NÃO FOI ACHADO OU NÃO EXISTE

    if(porcentagemtotal  == 100.0):
        print("------------FIM------------")
    else:
        print("Quantidade: ", len(lines), " Atual:", index , " Completo:", porcentagemtotal,"% " )

# TRADUZINDO O BANCO 
path_new.close()

# CRIANDO SQL INSERT CUSTON
path_item_new.close()
# path_drop_new.close()