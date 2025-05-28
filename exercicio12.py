import json
import os

agenda = "agenda.json"

def carregaar_dados():
    if os.path.exist(agenda):
        with open(agenda, "r", enconding="utf-8") as arq_json:
            return json.load(arq_json) 
        