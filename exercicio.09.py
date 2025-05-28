import json
import os

data = "funcionarios.json"

def carregar_dados():
    if os.path.exists(data):
        with open(data, "r", encoding="utf-8") as arq_json:
            return json.load(arq_json)
    else:
        return[]
    
funcionarios = carregar_dados()
for funcionarios in funcionarios:
     print(f"Nome do funcionario: {funcionarios["nome"]}' salario do funcionario: {funcionarios["salario"]}")

    
