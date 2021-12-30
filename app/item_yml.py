import yaml
import mysql.connector


mydb = mysql.connector.connect(
  host="db",
  user="ragnarok",
  password="ragnarok",
  database="ragnarok",
  port=3306,
  charset='utf8'
)
mydb.set_charset_collation('utf8', 'utf8_general_ci')
mycursor = mydb.cursor()

file_path_item_new = "yml/item_new/pre-re/item_db_equip_new.yml"
path_item_new = open(file_path_item_new, "wt")

with open("yml/item/pre-re/item_db_equip.yml", 'r') as f:
    try:
        body = ['Body']
        itens = []
        for idx, i in enumerate(yaml.full_load(f)['Body']):
            id = 0
            name_aegis = ''
            name_english = ''
            mycursor.execute('SET NAMES utf8;')
            mycursor.execute('SET CHARACTER SET utf8;')
            mycursor.execute('SET character_set_connection=utf8;')
            mycursor.execute("SELECT * FROM item_db where id = " + str(i['Id']))

            myresult = mycursor.fetchall()

            for x in myresult:
              id = x[0]
              name_aegis = x[1]
              try:
                name_english = str(x[2]).encode("latin-1").decode("utf-8")
              except Exception as exc:
                name_english = str(x[2]).encode('cp1252').decode('utf-8')              
              
              break

            if(id == i['Id'] and name_aegis == i['AegisName'] ):
              print(name_english, "name_english")
              i['Name'] = name_english
            

            itens.append(i)
            # if idx == 1:
            #     break
        # print(body)
        yaml.dump(itens, path_item_new, default_flow_style=False , encoding=('utf-8') , allow_unicode=True)
    except yaml.YAMLError as exc:
        print(exc)