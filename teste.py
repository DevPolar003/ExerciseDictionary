import os
os.system("cls")
dicionario = {}

def zerar_dicionario(dicio: dict) -> None:
    if len(dicio) == 0:
        print("--------Conteúdo do dicionario \n \tVAZIO!")
        input("Pressione algo para continuar...")
    else:
        print(">>>>>> Dicionario zerado!")
        dicio.clear()
        input("Pressione algo para continuar...")
        
def exibir_dicionario(dicio: dict) -> None:
    if len(dicio) == 0:
        print(">>>>> O dicionário está vazio!")
    else:
        print("\n-------Conteudo do dicionario")
        for k, v in dicio.items():
            print(f"{k}.........: {v}")
        print("------------------------------")
        input("Pressione algo para continuar...")

def adicionar_key(dicio: dict) -> None:
        nome_key = input("Nome da key: ").lower()
        if nome_key in dicio:
            print(f">>>>> A key '{nome_key}' já existe!")
        else:    
            print("""
            1 - int
            2 - float
            3 - str
            4 - bool
            """)
            tipo_dado= int(input("\tEscolha: "))
            conteudo_key = input("Digite o conteudo: ")
            
            match (tipo_dado):
                    case 1:
                        if conteudo_key == "":
                            dicio[nome_key] = 0
                        else:
                            dicio[nome_key] = int(conteudo_key)
                            print(f"{nome_key}: {conteudo_key} foi criado com sucesso")
                            input("Pressione algo para continuar...")
                    case 2:
                        if conteudo_key == "":
                            dicio[nome_key] = 0.0
                        else:
                            dicio[nome_key] = float(conteudo_key)
                            print(f"{nome_key}: {conteudo_key} foi criado com sucesso")
                            input("Pressione algo para continuar...")
                    case 3 :
                        dicio[nome_key] = conteudo_key
                        print(f"{nome_key}: {conteudo_key} foi criado com sucesso")
                        input("Pressione algo para continuar...")
                    case 4:
                        if conteudo_key == "":
                            dicio[nome_key] = False
                        else:
                            dicio[nome_key] = bool(conteudo_key)
                            print(f"{nome_key}: {conteudo_key} foi criado com sucesso")
                            input("Pressione algo para continuar...")
                    case _ :
                        print("Opçao invalida")

def editar_value(dicio: dict) -> None:
    if len(dicio) == 0:
        print(">>>>> O dicionário está vazio!")
    else:
        print("Keys:")
        for i, (k, v) in enumerate(dicio.items(), start=1):
            print(f"{i} - {k}: {v}")
        nun_chave = int(input("Número da chave: "))
        
        chave_selecionada = 0
        for i, (k, v) in enumerate(dicio.items(), start=1):
            if i == nun_chave:
                chave_selecionada = k
                
        if chave_selecionada != 0:
            novo_valor = input("Novo valor: ")

            tipo_atual = type(dicio[chave_selecionada])
            if tipo_atual == int:
                dicio[chave_selecionada] = int(novo_valor)
            elif tipo_atual == float:
                dicio[chave_selecionada] = float(novo_valor)
            elif tipo_atual == bool:
                dicio[chave_selecionada] = bool(novo_valor)
            else:
                dicio[chave_selecionada] = novo_valor
            exibir_dicionario(dicio)
        else:
            print(f">>>>> '{nun_chave}' é um número de chave inválido!")

def remover_key(dicio: dict) -> None:
    if len(dicio) == 0:
        print(">>>>> O dicionário está vazio!")
    else:
        print("Keys:")
        for i, (k, v) in enumerate(dicio.items(), start=1):
            print(f"{i} - {k}: {v}")
  
        nun_chave = int(input("Deseja excluir qual chave? "))
        
        chave_selecionada = 0
        for i, (k, v) in enumerate(dicio.items(), start=1):
            if i == nun_chave:
                chave_selecionada = k
                
        if chave_selecionada != 0:
            del dicio[chave_selecionada]
            exibir_dicionario(dicio)
        else:
            print(f">>>>> '{nun_chave}' é um número de chave inválido!")

def menu_principal(dicionario: dict) -> None:
    while True:
        print("""
            M E N U
            -------
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

menu_principal(dicionario)
