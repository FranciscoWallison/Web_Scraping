import yaml

with open("yml/item/item_db_equip.yml", 'r') as f:
    try:
        print(yaml.full_load(f))
    except yaml.YAMLError as exc:
        print(exc)