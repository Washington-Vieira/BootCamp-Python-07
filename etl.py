# Ler csv
# input csv output lista de dicionarios com dados


import csv

path_arquivo = "vendas.csv"

def ler_csv(nome_de_arquivo_csv: str) -> list[dict]:

    """
    Funcao que le um arquivo csv e retorna uma lista de dicionarios
    """
    lista = []
    with open(nome_de_arquivo_csv, mode="r", encoding='utf-8') as arquivo:   
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            lista.append(linha)
    return lista

# vendas_itens: list[dict] 
# vendas_itens = ler_csv(path_arquivo)
# print(vendas_itens)




# Filtrar produtos que não foram entregues
# input lista_de_produtos output lista_de_produtos entregue = True

def filtrar_produtos_nao_entregues(lista: list[dict]) -> list[dict]:

    """
    Funcao que filtra produtos onde entraga é = True
    """
    lista_com_produtos_filtrados = []
    for produto in lista:
        if produto.get("entregue") == "True":
            lista_com_produtos_filtrados.append(produto)
    return lista_com_produtos_filtrados

# lista_de_produtos = ler_csv(path_arquivo)
# produtos_entregues = filtrar_produtos_nao_entregues(lista_de_produtos)
# print(produtos_entregues)



#somar valores dos produtos

def somar_valores_dos_produtos(lista_com_produtos_filtrados: list[dict]) -> int:

    """
    soma todos os produtos que estao na lista
    """
    valor_total = 0
    for produto in lista_com_produtos_filtrados:
        valor_total += int(produto.get("price"))
    
    return valor_total



#------- ADICIONEI NO ARQUIVO MAIN.PY E IMPORTEI AS FUNÇÕES

# lista_de_produtos = ler_csv(path_arquivo)
# produtos_entregues = filtrar_produtos_nao_entregues(lista_de_produtos)
# valor_dos_produtos_entregues = somar_valores_dos_produtos(produtos_entregues)

# print(valor_dos_produtos_entregues)
