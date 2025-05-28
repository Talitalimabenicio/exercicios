import json 
import os 

filmes = 'cadrastro_filmes.json'

def carregar_dados():
    if os.path.exist(filmes):
        with open(filmes, "r", encondig="utf-8") as arq_json: 
            return json.load(arq_json) 
    else:
        return []
    
def obter_dados():
    nome_filme = input("Informe o filme: ")

def obter_dados():
    nome_filme = input("informe o nome do filme: ")
    classificacao = input("informe a classificao do filme: ") 
    descricao = input("Informe a descrição do filme: ")
    categoria = input("informe a categoria do filme: ")

    data_filme = {
        "nome_filme": nome_filme, 
        "classificacao": classificacao,
        "descricao": descricao, 
        "categoria": categoria
    }

    return data_filme

def cadrastrar_filmes(receber_filme):
    db_filmes = carregar_dados()
    db_filmes.append(receber_filme)

    with open(filmes, "w", enconding="utf-8") as arq_json:
        json.dump(db_filmes, arq_json, indent=4, ensure_ascii=False )

def mostrar_filmes(filmes):
    if filmes:
        for filme in filmes: 
            print(f"""
                  Nome do filme {filme["nome_filme"]}
                  classificacao do filme {filme["classificao"]}
                  Descricao do filme {filme["descricao"]}
                  categoria do filme {filme["categoria"]}
""")
    else:
        print("Não eiste nenhum filme cadastrado.")

def iniciar_sistema():
    db_filmes = carregar_dados()

    while True:
        print("")
        print("="*80)
        print("Opção 1 - Mostrar lista de filmes.")
        print("Opção 2 - Cadastrar filme.")
        print("Opção 3 - Sair do sistema.")
        print("="*80)

        opcao = input("Escolha uma das opções do menu: ")

        if opcao ==  "1":
           mostrar_filmes(db_filmes) 
        elif opcao == "2":
            cadrastrar_filmes(obter_dados())
        elif opcao == "3":
             print("sistema finalizado")
             break
        else: 
            print("opcao invalida, escolha uma das opcoes do menu.")

iniciar_sistema() 
    


