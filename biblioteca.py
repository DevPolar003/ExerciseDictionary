def adicionar_key(dicio: dict) -> None:
    nome_key = input("Nome da key: ").strip().lower()
    if nome_key in dicio:
        print(f">>>>> A key '{nome_key}' já existe!")
        input("Pressione algo para continuar...")
    else:    
        print("""
            1 - int
            2 - float
            3 - str
            4 - bool
        """)
        
        try:
            tipo_dado = int(input("\tEscolha: "))
            conteudo_key = input("Digite o conteudo: ")
            
            match (tipo_dado):
                case 1:
                    if conteudo_key == "":
                        dicio[nome_key] = 0
                        print(f"{nome_key}: {dicio[nome_key]} foi criado com sucesso")
                        input("Pressione algo para continuar...")
                    else:
                        try:
                            dicio[nome_key] = int(conteudo_key)
                            print(f"{nome_key}: {dicio[nome_key]} foi criado com sucesso")
                            input("Pressione algo para continuar...")
                        except ValueError:
                            print(">>>>> Erro: Você escolheu 'int', mas não digitou um valor valido")
                            input("Pressione algo para continuar...")
                            
                case 2:
                    if conteudo_key == "":
                        dicio[nome_key] = 0.0
                        print(f"{nome_key}: {dicio[nome_key]} foi criado com sucesso")
                        input("Pressione algo para continuar...")
                    else:
                        try:
                            dicio[nome_key] = float(conteudo_key)
                            print(f"{nome_key}: {dicio[nome_key]} foi criado com sucesso")
                            input("Pressione algo para continuar...")
                        except ValueError:
                            print(">>>>> Erro: Você escolheu 'float', mas não digitou um valor valido")
                            input("Pressione algo para continuar...")
                            
                case 3:
                    dicio[nome_key] = conteudo_key
                    print(f"{nome_key}: {conteudo_key} foi criado com sucesso")
                    input("Pressione algo para continuar...")
                    
                case 4:
                    if conteudo_key == "":
                        dicio[nome_key] = False
                        print(f"{nome_key}: {conteudo_key} foi criado com sucesso")
                        input("Pressione algo para continuar...")
                    elif conteudo_key.lower() == "false": 
                        dicio[nome_key] = False
                        print(f"{nome_key}: {conteudo_key} foi criado com sucesso")
                        input("Pressione algo para continuar...")
                    else:    
                        dicio[nome_key] = bool(conteudo_key)
                        print(f"{nome_key}: {conteudo_key} foi criado com sucesso")
                        input("Pressione algo para continuar...")
                    
                case _:
                    print(">>>>> Opção inválida")
                    input("Pressione algo para continuar...")
                    
        except ValueError:
            print(">>>>> Escolha inválida. digite um número de 1 a 4.>>>>>")
            input("Pressione algo para continuar...")


def editar_value(dicio: dict) -> None:
    if len(dicio) == 0:
        print(">>>>> O dicionário está vazio!")
        input("Pressione algo para continuar...")
    else:
        print("Keys:")
        for i, (k, v) in enumerate(dicio.items(), start=1):
            print(f"{i} - {k}: {v}")
        try:
            nun_chave = int(input("Número da chave: "))
            chave_selecionada = 0
            for i, (k, v) in enumerate(dicio.items(), start=1):
                if i == nun_chave:
                    chave_selecionada = k
            if chave_selecionada != 0:
                novo_valor = input("Novo valor: ")
                try:
                    if type(dicio[chave_selecionada]) == int:
                        dicio[chave_selecionada] = int(novo_valor)
                    elif type(dicio[chave_selecionada]) == float:
                        dicio[chave_selecionada] = float(novo_valor)
                    elif type(dicio[chave_selecionada]) == bool:
                        if novo_valor == "":
                            dicio[chave_selecionada] = False
                        elif novo_valor.lower() == "false":
                            dicio[chave_selecionada] = False
                        else:
                            dicio[chave_selecionada] = bool(novo_valor)
                    else:
                        dicio[chave_selecionada] = novo_valor
                    exibir_dicionario(dicio)
                    
                except ValueError:
                    print(">>>>> O valor digitado é diferente com o tipo original da chave!")
                    input("Pressione algo para continuar...")
            else:
                print(f">>>>> {nun_chave} é um número de chave inválido!")
                input("Pressione algo para continuar...")
                
        except ValueError:
            print(">>>>> Erro: Você deve digitar o numero correspondente à chave!")
            input("Pressione algo para continuar...")


def remover_key(dicio: dict) -> None:
    if len(dicio) == 0:
        print(">>>>> O dicionário está vazio!")
        input("Pressione algo para continuar...")
    else:
        print("Keys:")
        for i, (k, v) in enumerate(dicio.items(), start=1):
            print(f"{i} - {k}: {v}")
  
        try:
            nun_chave = int(input("Deseja excluir qual chave? "))
            
            chave_selecionada = 0
            for i, (k, v) in enumerate(dicio.items(), start=1):
                if i == nun_chave:
                    chave_selecionada = k
                    
            if chave_selecionada != 0:
                del dicio[chave_selecionada]
                exibir_dicionario(dicio)
            else:
                print(f">>>>> '{nun_chave}' é um número de chave invalido")
                input("Pressione algo para continuar...")
                
        except ValueError:
            print(">>>>> Erro: Você deve digitar o numero correspondente a chave")
            input("Pressione algo para continuar...")

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
        input("Pressione algo para continuar...")
    else:
        print("\n-------Conteudo do dicionario")
        for k, v in dicio.items():
            print(f"{k}.........: {v}")
        print("------------------------------")
        input("Pressione algo para continuar...")
