import yaml
import mysql.connector

mydb = mysql.connector.connect(
  host="db",
  user="ragnarok",
  password="ragnarok",
  database="ragnarok",
  port=3306
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM item_db")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
  break
  
file_path_item_new = "data.yml"
path_item_new = open(file_path_item_new, "wt")

with open("yml/item/item_db_equip.yml", 'r') as f:
    try:
        body = []
        for idx, i in enumerate(yaml.full_load(f)['Body']):
            # print(idx, i )
            body.append(i)
            if idx == 2:
                break
        
        print(body)
        yaml.dump(body, path_item_new, default_flow_style=False)
    except yaml.YAMLError as exc:
        print(exc)
    