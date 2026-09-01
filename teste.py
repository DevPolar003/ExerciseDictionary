import os
os.system("cls")
dicionario = {}

def zerar_dicionario(dicio: dict) -> None:
    if len(dicio) == 0:
        print("--------Conteúdo do dicionario \n \tVAZIO!")
    else:
        dicio = {}
        
def exibir_dicionario(dicio: dict) -> None:
    print("\n------- Conteudo do dicionario")
    for k, v in dicio.items():
        print(f"{k}.........: {v}")
    print("------------------------------")

def adicionar_key(dicio: dict) -> None:
        nome_key = input("Nome da key: ")
        print("""
        1 - int
        2 - float
        3 - str
        4 - bool
        """)
        tipo_dado= int(input("\tEscolha: "))
        match (tipo_dado):
                case 1:
                    conteudo_key = int(input("Digite o conteudo: "))
                    dicio[nome_key] = conteudo_key
                case 2:
                    conteudo_key = float(input("Digite o conteudo: "))
                    dicio[nome_key] = conteudo_key
                case 3 :
                    conteudo_key = input("Digite o conteudo: ")
                    dicio[nome_key] = conteudo_key
                case 4:
                    conteudo_key = bool(input("Digite o conteudo: "))
                    dicio[nome_key] = conteudo_key
                case _ :
                    print("Opçao invalida")

def editar_value(dicio: dict) -> None:
    print("Keys:")
    for k, v in dicio.items():
         print(f"{k}.........: {v}")
    nun_chave = input("Numero da chave: ")
    novo_valor = input("Novo valor: ")
    exibir_dicionario(dicio)

def remover_key(dicio: dict) -> None:
    print("Keys:")
    for k, v in dicio.items():
         print(f"{k}.........: {v}")
    nun_chave = input("Deseja excluir qual chave? ")

while True:
    print("""
        0 - Sair
        1 - Zerar dicionario
        2 - Adicionar uma key
        3 - Editar value
        4 - Remover uma key
        5 - Exibir dicionario
    """)
    escolha = int(input("\tEscolha: "))

    match (escolha):
        case (0):
            break
        case 1:
            zerar_dicionario(dicionario)
        case 2:
            adicionar_key(dicionario)
        case 3:
            editar_value(dicionario)
        case 4:
            remover_key(dicionario)
        case 5:
            exibir_dicionario(dicionario)
