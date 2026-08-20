import os
os.system("cls") 
nome_dicionario = {}

while True:
    print("0 - Sair")
    print("1 - Zerar dicionário")
    print("2 - Criar uma chave")
    print("3 - Procurar um dado na chave")
    print("4 - Editar o valor de uma chave")
    print(f"Dicionário atual: {nome_dicionario}")
    
    valor = int(input("\nEscolha uma opção: "))

    match valor:
        case 0:
            print("Saindo do programa...")
            break

        case 1:
            nome_dicionario = {}
            print("Dicionário zerado!")

#Faça um programa que inicialize um dicionário zerado e apareça as opcoes:
#0 - SAIR
#1 - Zerar o dicionário
#2 - Adicionar keys
#3 - Editar values
#4 - Apagar keys


#2- Ao adicionar keys, pergunte:
#- o nome da key
#- o tipo da key
#- o conteúdo da key

#3- Ao editar uma um value, liste as keys existentes para o usuário esolher
#qual editar, e coloque o tipo correspondente do conteúdo.

#4 - Antes de apagar a key, liste as existentes para que ele escolha a que será excluída



