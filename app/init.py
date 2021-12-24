from urllib.request import urlopen
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import pandas as pd


file_path_mob_new = "db_extra/create_scrapin/mob_description.txt"
path_mob_new = open(file_path_mob_new, "wt")

file_path_drop_new = "db_extra/create_scrapin/mob_item_drop.txt"
path_drop_new = open(file_path_drop_new, "wt")

id_name_mob = "aliot"
req = Request("https://playragnarokonlinebr.com/database/thor/monstros/detalhes/"+ id_name_mob, headers={'User-Agent': 'Mozilla/5.0'})
html = urlopen(req).read()
bs = BeautifulSoup(html, 'html.parser')
linhas = bs.find('div', {'id':'itemDescription'})


linhaNome = bs.find('div',{'class':'col-xs-10'})

if(len(linhaNome.findChildren("h1")) == 0):
    print("----- NÃO TEM -----")
    
else:
    print("----- Monstro -----")
    print("Nome: ", linhaNome.findChildren("h1")[0].text) 

    print("----- Informações -----") 
    informacoes = bs.find('ul',{'id':'informacoes-list'})
    # Nível
    nivel = informacoes.findChildren("li")[1].text
    print(informacoes.findChildren("li")[0].text , nivel)
    # Raça
    raca = "'"+informacoes.findChildren("li")[3].text+"'"
    print(informacoes.findChildren("li")[2].text , raca)
    # Propriedade
    propriedade = "'"+informacoes.findChildren("li")[5].text+"'"
    print(informacoes.findChildren("li")[4].text , propriedade)
    # Tamanho
    tamanho = "'"+informacoes.findChildren("li")[7].text+"'"
    print(informacoes.findChildren("li")[6].text , tamanho)
    # Exp Base
    exp_base = informacoes.findChildren("li")[9].text.replace('.', '')
    print(informacoes.findChildren("li")[8].text , exp_base)
    # Exp Classe
    exp_classe = informacoes.findChildren("li")[11].text.replace('.', '')
    print(informacoes.findChildren("li")[10].text , exp_classe)

    print("----- Resistências e Fraquezas -----") 
    resistencias_fraquezas = bs.find('ul',{'id':'property'})
    # Neutro
    neutro = resistencias_fraquezas.findChildren("li")[1].text.replace('%', '')
    print(resistencias_fraquezas.findChildren("li")[0].text , neutro)
    # Água
    agua = resistencias_fraquezas.findChildren("li")[3].text.replace('%', '')
    print(resistencias_fraquezas.findChildren("li")[2].text , agua)
    # Terra
    terra = resistencias_fraquezas.findChildren("li")[5].text.replace('%', '')
    print(resistencias_fraquezas.findChildren("li")[4].text , terra)
    # Fogo
    fogo =  resistencias_fraquezas.findChildren("li")[7].text.replace('%', '')
    print(resistencias_fraquezas.findChildren("li")[6].text , fogo)
    # Vento
    vento = resistencias_fraquezas.findChildren("li")[9].text.replace('%', '')
    print(resistencias_fraquezas.findChildren("li")[8].text , vento)
    # Veneno
    veneno = resistencias_fraquezas.findChildren("li")[11].text.replace('%', '')
    print(resistencias_fraquezas.findChildren("li")[10].text , veneno)
    # Sagrado
    sagrado = resistencias_fraquezas.findChildren("li")[13].text.replace('%', '')
    print(resistencias_fraquezas.findChildren("li")[12].text , sagrado)
    # Sombrio
    sombrio = resistencias_fraquezas.findChildren("li")[15].text.replace('%', '')
    print(resistencias_fraquezas.findChildren("li")[14].text , sombrio)
    # Fantasma
    fantasma = resistencias_fraquezas.findChildren("li")[17].text.replace('%', '')
    print(resistencias_fraquezas.findChildren("li")[16].text , fantasma)
    # Maldito
    maldito = resistencias_fraquezas.findChildren("li")[19].text.replace('%', '')
    print(resistencias_fraquezas.findChildren("li")[18].text , maldito)

    print("----- Atributos -----") 
    atributos = bs.find('div',{'id':'two-flexbox'})
    atributos1 = atributos.findChildren("ul")[0]
    # HP
    hp = atributos1.findChildren("li")[1].text.replace('.', '')
    print(atributos1.findChildren("li")[0].text , hp)
    # Ataque
    ataque = "'"+atributos1.findChildren("li")[3].text+"'"
    print(atributos1.findChildren("li")[2].text , ataque)
    # Alcance
    alcance = atributos1.findChildren("li")[5].text
    print(atributos1.findChildren("li")[4].text , alcance)
    # Precisão
    precisao = atributos1.findChildren("li")[7].text
    print(atributos1.findChildren("li")[6].text , precisao)
    # Esquiva
    esquiva = atributos1.findChildren("li")[9].text
    print(atributos1.findChildren("li")[8].text , esquiva)
    atributos2 = atributos.findChildren("ul")[1]
    # DEF
    defense = atributos2.findChildren("li")[1].text
    print(atributos2.findChildren("li")[0].text , defense)
    # VIT
    vit =  atributos2.findChildren("li")[3].text
    print(atributos2.findChildren("li")[2].text , vit)
    # DEFM
    defm = atributos2.findChildren("li")[5].text
    print(atributos2.findChildren("li")[4].text , defm)
    # INT
    int = atributos2.findChildren("li")[7].text
    print(atributos2.findChildren("li")[6].text , int)
    # FOR
    force = atributos2.findChildren("li")[9].text
    print(atributos2.findChildren("li")[8].text , force)
    # DES
    des = atributos2.findChildren("li")[11].text
    print(atributos2.findChildren("li")[10].text , des)
    # AGI
    agi = atributos2.findChildren("li")[13].text
    print(atributos2.findChildren("li")[12].text , agi)
    # SOR
    sor = atributos2.findChildren("li")[15].text
    print(atributos2.findChildren("li")[14].text , sor)

    strin_insert_mob_db = "REPLACE INTO `mob_description` "
    strin_insert_mob_db = strin_insert_mob_db + "(`name_aegis`,`nivel`,`raca`,`propriedade`,`tamanho`,`exp_base`,`exp_classe`,`neutro`,`agua`,`terra`,`fogo`,`vento`,`veneno`,`sagrado`, `sombrio`, `fantasma`,`maldito`,`hp`,`ataque`,`alcance`,`precisao`,`esquiva`,`def`,`vit`,`defm`,`int`,`for`,`des`,`agi`,`sor`) VALUES ("
    strin_insert_mob_db = strin_insert_mob_db + "'"+id_name_mob +"'"+", "+ nivel+", "+ raca+", "+ propriedade+", "+ tamanho+", "+ exp_base+", "+ exp_classe+", "+neutro+", "+agua+", "+terra+", "+fogo+", "+vento+", "+veneno+", "+sagrado+", "+sombrio+", "+fantasma+", "+maldito+", "+hp+", "+ataque+", "+alcance+", "+precisao
    strin_insert_mob_db = strin_insert_mob_db +", " + esquiva+", " + defense+", " +vit+", " +defm+", " +int+", " +force+", " +des+", " +agi+", "+sor + ");"

    print(strin_insert_mob_db)
    # path_new.write(strin_insert_mob_db)
    path_mob_new.write(strin_insert_mob_db)
    # init drop
    drop = bs.find('section',{'id':'slider-result'})
    listitens = drop.findChildren("ul")[0]
    contents = listitens.findChildren("li")
    drop_quantidaded = bs.find('li',{'class':'drops-monsters'})
    print("----- ",drop_quantidaded.text," -----")
    if drop_quantidaded.text != "Drops (0)":
        for i in contents:
            type_item = i.find('a')['href'].split("/")[5]
            id_name_item = i.find('a')['href'].split("/")[7]
            nome = i.find('h5').text

            texto_drop = i.find_all('label')[1].text.split(" ")[0]
            valor_drop = i.find_all('label')[1].text.split(" ")[1].replace('%', '').replace('.', '')
            texto_preco = i.find_all('label')[2].text.split(" ")[0]
            valor_preco = i.find_all('label')[2].text.split(" ")[1].replace('Z', '')
            
            # print( " Tipo de item: ", type_item, ", ID_Name: ",id_name_item , ", Nome: ", nome, ","
            # , texto_drop, ": ", valor_drop, ",", texto_preco, ": ",valor_preco )
            insert_mob_item_drop_db = "REPLACE INTO `mob_item_drop` " 
            insert_mob_item_drop_db = insert_mob_item_drop_db + "(`name_aegis_mob`, `name_aegis_item`, `type`, `name`, `drop`, `preco`) VALUES ("
            insert_mob_item_drop_db= insert_mob_item_drop_db + "'"+id_name_mob +"'"+", "+  "'"+id_name_item +"'"+", '"+type_item+"', "+"'"+nome+"', "+valor_drop+", "+valor_preco+ ");\n"
            path_drop_new.write(insert_mob_item_drop_db)
            print( insert_mob_item_drop_db)
            
            # print(i)
        

path_drop_new.close()
path_mob_new.close()

## Imprime todo texto contido em cada linha ##
# for i in linhaNome:
#     filho = i.findChildren("h1")
#     print(filho)
        
## Imprime o texto de cada uma das tags filhas ##
# for i in linhas:
#     filhas = i.findChildren("span")
#     print(filhas[0])
#     print(filhas[1])
#     print(filhas[2])

# codigo, descricao, periodo = [], [], []

# for i in linhas:
#     children = i.findChildren("span")
#     codigo.append(children[0].text)
#     descricao.append(children[1].text)
#     periodo.append(children[2].text)

# df = pd.DataFrame({'Código': codigo, 'Descrição': descricao, 'Período': periodo})
# df.head()
# df.to_excel('caminho_do_arquivo.xlsx')