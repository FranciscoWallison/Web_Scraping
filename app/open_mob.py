from urllib.request import urlopen
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import pandas as pd
import time

file_path = "inst_text/mob_db_re.txt"
file_path_new = "inst_text/mob_db_re_new.txt"
path_new = open(file_path_new, "wt")

with open(file_path) as f:
    lines = f.readlines() ##Assume the sample file has 3 lines
    # first = lines.split('\n', 1)[0]

for idx, i in enumerate(lines):
    index = idx+1
    porcentagemtotal =  ((index / len(lines)) * 100)
    print("Quantidade: ", len(lines), " Atual:", index , " Completo:", porcentagemtotal,"% " )
    campos_valores = i.split(" VALUES ")
    valores = campos_valores[1].split(",")
    idname_mob = valores[1]
    url = "https://playragnarokonlinebr.com/database/thor/monstros/detalhes/"+ idname_mob.replace('\'', '')
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        time.sleep(1)
        html = urlopen(req).read()
    except HTTPError as e:
        time.sleep(3)
        html = urlopen(req).read()

    bs = BeautifulSoup(html, 'html.parser')
    linhas = bs.find('div', {'id':'itemDescription'})
    linhaNome = bs.find('div',{'class':'col-xs-10'})
    if(len(linhaNome.findChildren("h1")) == 0):
        print("----- NÃO TEM -----")
        path_new.write(i)
    else:
        print("----- Monstro -----") 
        # nome mob
        nome_mobe = linhaNome.findChildren("h1")[0].text
        print("Nome: ", nome_mobe) 

        newLine = i.replace(valores[2], "'"+nome_mobe+"'")
        newLine = newLine.replace(valores[3], "'"+nome_mobe+"'")
        path_new.write(newLine)

        print("----- Informações -----") 
        informacoes = bs.find('ul',{'id':'informacoes-list'})
        # Nível
        print(informacoes.findChildren("li")[0].text , informacoes.findChildren("li")[1].text)
        # Raça
        print(informacoes.findChildren("li")[2].text , informacoes.findChildren("li")[3].text)
        # Propriedade
        print(informacoes.findChildren("li")[4].text , informacoes.findChildren("li")[5].text)
        # Tamanho
        print(informacoes.findChildren("li")[6].text , informacoes.findChildren("li")[7].text)
        # Exp Base
        print(informacoes.findChildren("li")[8].text , informacoes.findChildren("li")[9].text)
        # Exp Classe
        print(informacoes.findChildren("li")[10].text , informacoes.findChildren("li")[11].text)

        print("----- Resistências e Fraquezas -----") 
        resistencias_fraquezas = bs.find('ul',{'id':'property'})
        # Neutro
        print(resistencias_fraquezas.findChildren("li")[0].text , resistencias_fraquezas.findChildren("li")[1].text)
        # Água
        print(resistencias_fraquezas.findChildren("li")[2].text , resistencias_fraquezas.findChildren("li")[3].text)
        # Terra
        print(resistencias_fraquezas.findChildren("li")[4].text , resistencias_fraquezas.findChildren("li")[5].text)
        # Fogo
        print(resistencias_fraquezas.findChildren("li")[6].text , resistencias_fraquezas.findChildren("li")[7].text)
        # Vento
        print(resistencias_fraquezas.findChildren("li")[8].text , resistencias_fraquezas.findChildren("li")[9].text)
        # Veneno
        print(resistencias_fraquezas.findChildren("li")[10].text , resistencias_fraquezas.findChildren("li")[11].text)
        # Sagrado
        print(resistencias_fraquezas.findChildren("li")[12].text , resistencias_fraquezas.findChildren("li")[13].text)
        # Sombrio
        print(resistencias_fraquezas.findChildren("li")[14].text , resistencias_fraquezas.findChildren("li")[15].text)
        # Fantasma
        print(resistencias_fraquezas.findChildren("li")[16].text , resistencias_fraquezas.findChildren("li")[17].text)
        # Maldito
        print(resistencias_fraquezas.findChildren("li")[18].text , resistencias_fraquezas.findChildren("li")[19].text)

        print("----- Atributos -----") 
        atributos = bs.find('div',{'id':'two-flexbox'})
        atributos1 = atributos.findChildren("ul")[0]
        # HP
        print(atributos1.findChildren("li")[0].text , atributos1.findChildren("li")[1].text)
        # Ataque
        print(atributos1.findChildren("li")[2].text , atributos1.findChildren("li")[3].text)
        # Alcance
        print(atributos1.findChildren("li")[4].text , atributos1.findChildren("li")[5].text)
        # Precisão
        print(atributos1.findChildren("li")[6].text , atributos1.findChildren("li")[7].text)
        # Esquiva
        print(atributos1.findChildren("li")[8].text , atributos1.findChildren("li")[9].text)
        atributos2 = atributos.findChildren("ul")[1]
        # DEF
        print(atributos2.findChildren("li")[0].text , atributos2.findChildren("li")[1].text)
        # VIT
        print(atributos2.findChildren("li")[2].text , atributos2.findChildren("li")[3].text)
        # DEFM
        print(atributos2.findChildren("li")[4].text , atributos2.findChildren("li")[5].text)
        # INT
        print(atributos2.findChildren("li")[6].text , atributos2.findChildren("li")[7].text)
        # FOR
        print(atributos2.findChildren("li")[8].text , atributos2.findChildren("li")[9].text)
        # DES
        print(atributos2.findChildren("li")[10].text , atributos2.findChildren("li")[11].text)
        # AGI
        print(atributos2.findChildren("li")[12].text , atributos2.findChildren("li")[13].text)
        # SOR
        print(atributos2.findChildren("li")[14].text , atributos2.findChildren("li")[15].text)

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
                valor_drop = i.find_all('label')[1].text.split(" ")[1]

                texto_preco = i.find_all('label')[2].text.split(" ")[0]
                valor_preco = i.find_all('label')[2].text.split(" ")[1]
                
                
                print( " Tipo de item: ", type_item, ", ID_Name: ",id_name_item , ", Nome: ", nome, ","
                , texto_drop, ": ", valor_drop, ",", texto_preco, ": ",valor_preco )
                
    if(porcentagemtotal  == 100.0):
        print("------------FIM------------")
    else:
        print("Quantidade: ", len(lines), " Atual:", index , " Completo:", porcentagemtotal,"% " )

    # if(index == 2 ):
    #     break

path_new.close()