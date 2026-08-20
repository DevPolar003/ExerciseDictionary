import os

nome_dicionario = {}
# Mapeamento para converter o texto digitado no tipo real
tipos = {"str": str, "int": int, "float": float, "bool": bool}

while True:
    os.system("cls" if os.name == "nt" else "clear")
    print(f"Dicionário atual: {nome_dicionario}\n")
    print("0 - Sair | 1 - Zerar | 2 - Adicionar key | 3 - Editar value | 4 - Apagar key")
    
    opcao = input("Escolha uma opção: ")

    match opcao:
        case "0":
            print("Saindo...")
            break

        case "1":
            nome_dicionario.clear()
            print("Dicionário zerado!")

        case "2":
            chave = input("Nome da key: ").strip().lower()
            tipo_nome = input("Tipo (str, int, float, bool): ").strip().lower()
            conteudo = input("Conteúdo: ")

            # Converte para o tipo correto se existir no dicionário de tipos, senão mantém como texto
            construtor = tipos.get(tipo_nome, str)
            nome_dicionario[chave] = construtor(conteudo)
            print(f"Key '{chave}' adicionada com sucesso!")

        case "3":
            if not nome_dicionario:
                print("Dicionário está vazio!")
            else:
                print("\nKeys disponíveis:")
                for k, v in nome_dicionario.items():
                    print(f"- {k} (atual: {v}, tipo: {type(v).__name__})")
                
                chave = input("\nQual key deseja editar? ").strip().lower()
                if chave in nome_dicionario:
                    tipo_nome = input("Novo tipo (str, int, float, bool): ").strip().lower()
                    conteudo = input("Novo conteúdo: ")
                    construtor = tipos.get(tipo_nome, str)
                    nome_dicionario[chave] = construtor(conteudo)
                    print("Valor atualizado!")
                else:
                    print("Key não encontrada.")

        case "4":
            chave = input("Key que deseja apagar: ").strip().lower()
            if nome_dicionario.pop(chave, None) is not None:
                print(f"A chave '{chave}' foi apagada com sucesso!")
            else:
                print("Essa chave não existe.")
    
    input("\nPressione ENTER para continuar...")
    
