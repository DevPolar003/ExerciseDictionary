# Joao victor rivaroli marques
# luis felipe

import biblioteca
import os
os.system('cls')

dicionario = {}

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
        
    try:
        escolha = int(input("\tEscolha: "))
            
        match (escolha):
            case 0:
                    print("Encerrando...")
                    break
            case 1:
                biblioteca.zerar_dicionario(dicionario)
            case 2:
                biblioteca.adicionar_key(dicionario)
            case 3:
                biblioteca.editar_value(dicionario)
            case 4:
                biblioteca.remover_key(dicionario)
            case 5:
                biblioteca.exibir_dicionario(dicionario)
            case _:
                print(">>>>> Opção inválida! Escolha um número de 0 a 5.")
                input("Pressione algo para continuar...")
    except ValueError:
            print(">>>>> Opção inválida! Por favor, digite um número do menu.")
            input("Pressione algo para continuar...")