def cadastrar_filmes(nome, classificacao, categoria1, categoria2):
    lista = []
    dicionario = {
        "nome" : nome,
        "classificacao" : classificacao,
        "categoria" : [categoria1, categoria2]
    }
    lista.append(dicionario)
    return lista


print(cadastrar_filmes("Homem de ferro", 12, "acao", "aventura"))


