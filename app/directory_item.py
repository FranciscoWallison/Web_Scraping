from urllib.request import urlopen
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import pandas as pd
import time

file_path = "inst_text/item/item_db_equip.txt"
# TRADUZINDO O BANCO 
# file_path_new = "inst_text/mob_db_re_new.txt"
# path_new = open(file_path_new, "wt")

# CRIANDO SQL COM OS DADOS DO SITE
# file_path_mob_new = "db_extra/create_scrapin/mob_description_re.txt"
# path_mob_new = open(file_path_mob_new, "wt")
# file_path_drop_new = "db_extra/create_scrapin/mob_item_drop_re.txt"
# path_drop_new = open(file_path_drop_new, "wt")

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

    if valores[3] == "'Weapon'" or valores[3] == "'Petarmor'":
        type_item = "armamentos"
    if valores[3] == "'Poring_Egg'" or valores[3] == "'Armor'" or valores[3] == "'Petegg'":
        type_item = "equipamentos"
   
    id_name_mob = valores[1]
    url = "https://playragnarokonlinebr.com/database/thor/"+type_item.replace('\'', '')+"/detalhes/"+ id_name_item_url.replace('\'', '')
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    print(valores[3])
    print(id_name_item, id_name_item_url)
    
    try:
        time.sleep(1)
        html = urlopen(req).read()
    except HTTPError as e:
        time.sleep(3)
        if e.code == 500:
            # path_new.write(i) # TRADUZINDO O BANCO 
            print(e.code)
            print(url)
            continue
        # html = urlopen(req).read()
        print("----- ERROR-----")
        print(e.code)
        print(url)
        break

    bs = BeautifulSoup(html, 'html.parser')
    linhas = bs.find('main', {'id':'itens-main'})

    linhaNome = bs.find('article',{'class':'items-emphasis'})

    if(len(linhaNome.findChildren("h1")) == 0):
        print("----- NÃO TEM -----")
        print(url)
        break
        # path_new.write(i) # TRADUZINDO O BANCO 
    # else:

        # newLine = i.replace(valores[2], "'"+nome_mobe+"'")
        # newLine = newLine.replace(valores[3], "'"+nome_mobe+"'")        
        # path_new.write(newLine) # TRADUZINDO O BANCO 

    #     print("----- "+type_item.capitalize()+" -----")
    #     nome_traduzido = linhaNome.findChildren("h1")[0].text
    #     print("Nome: ", nome_traduzido) 

    #     print("----- Descrição -----") 
    #     descricao_iteminfor = bs.find_all('meta',{'name':'description'})[0]['content']
    #     print(descricao_iteminfor)
    #     descricao = linhaNome.findChildren("pre")[0].text
    #     # print( descricao ) 

    #     print("----- Informações -----") 
    #     informacoes = bs.find_all('ul',{'class':'list'})[0]
    #     # Preço
    #     preco = informacoes.findChildren("li")[1].text.replace('.', '').replace('zeny', '').replace(' ', '')
    #     print(informacoes.findChildren("li")[0].text, preco + "zeny")
    #     # Peso
    #     peso = informacoes.findChildren("li")[3].text
    #     print(informacoes.findChildren("li")[2].text, preco)

    #     print("----- Pode ser... -----")
    #     pode_ser = bs.find_all('ul',{'class':'flex-check'})[0]
    #     # Jogado no chão
    #     jogado_no_chao = 'true' if "POSITIVE" in pode_ser.findChildren("li")[0].findAll('img')[0]['src'] else 'false'
    #     print(pode_ser.findChildren("li")[1].text, jogado_no_chao)
    #     # Guardado no carrinho
    #     guardado_no_carrinho = 'true' if "POSITIVE" in pode_ser.findChildren("li")[2].findAll('img')[0]['src'] else 'false'
    #     print(pode_ser.findChildren("li")[3].text, guardado_no_carrinho)
    #     # Negociado
    #     negociado = 'true' if "POSITIVE" in pode_ser.findChildren("li")[4].findAll('img')[0]['src'] else 'false'
    #     print(pode_ser.findChildren("li")[5].text, negociado)
    #     # Vendido para NPC
    #     vendido_para_npc = 'true' if "POSITIVE" in pode_ser.findChildren("li")[6].findAll('img')[0]['src'] else 'false'
    #     print(pode_ser.findChildren("li")[7].text, vendido_para_npc)
    #     # Colocado no armazém
    #     colocado_no_armazem = 'true' if "POSITIVE" in pode_ser.findChildren("li")[8].findAll('img')[0]['src'] else 'false'
    #     print(pode_ser.findChildren("li")[9].text, colocado_no_armazem)
    #     # Colocado no armazém da guilda
    #     colocado_armazem_guilda = 'true' if "POSITIVE" in pode_ser.findChildren("li")[10].findAll('img')[0]['src'] else 'false'
    #     print(pode_ser.findChildren("li")[11].text, colocado_armazem_guilda)
                
    # if(porcentagemtotal  == 100.0):
    #     print("------------FIM------------")
    # else:
    #     print("Quantidade: ", len(lines), " Atual:", index , " Completo:", porcentagemtotal,"% " )

    # if(index == 2 ):
    #     break

# TRADUZINDO O BANCO 
# path_new.close()

# CRIANDO SQL INSERT CUSTON
# path_mob_new.close()
# path_drop_new.close()