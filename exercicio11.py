import json
import os 

veiculos = "catrastro_veiculos.json"

def carregar_dados():
    if os.path.exists(veiculos):
        with open(veiculos, "r", encoding="utf-8") as arq_json:
            return json.load(arq_json)
    else: 
       return []
    
def obter_dados():
   marca = input("informe a marca do veiculo")  
   modelo = input("informe o modelo do carro") 
   ano = input("informe o ano do carro")
   cor = input("inform a cor do carro")

   data_veiculos = {
   "marca" : marca,
   "modelo": modelo,
   "ano": ano,
   "cor": cor
   }
   return (data_veiculos)

def cadastrar_veiculos(receber_veiculos):
    db_veiculos = carregar_dados()
    db_veiculos.append(receber_veiculos)

    with open(veiculos, "w", encoding="utf-8") as arq_json:
        json.dump(db_veiculos,arq_json, indent=4, ensure_ascii=False)

def mostrar_veiculos(veiculos):
    if veiculos:
        for veiculo in veiculos:
            print(f"""
                  Marca do veiculo {veiculo["marca"]}
                  Modelo do veiculo {veiculo["modelo"]}
                  Ano do veiculo {veiculo["ano"]}
                  Cor do veiculo {veiculo["cor"]}
            """)
    else:
        print("Não existe nenhum veiculo cadastrado.")

def iniciar_sistema():
    db_veiculos = carregar_dados()
    while True:
        print("")
        print("="*80)
        print("Opção 1 - Exibir os veiculos")
        print("Opção 2 - Cadastrar um novo veiculo")
        print("Opção 3 - Sair do sistema")
        print("="*80)

        opcao = input("Escolha uma das opções do menu: ")

        if opcao == "1":
            mostrar_veiculos(db_veiculos)
        elif opcao == "2":
            cadastrar_veiculos(obter_dados())
        elif opcao == "3":
            print("Sistema finalizado!")
            break
        else:
            print("Opção invalida, escolha uma das opções do menu.")

iniciar_sistema()
   


