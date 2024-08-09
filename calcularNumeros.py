import os
"""
6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. 
Utilize um bloco try-except para lidar com possíveis exceções.
"""

lista_de_numeros = []
valor_total = 0
def erro_valor_invalido():
    os.system('cls')

    print('Valor inválido, tente novamente com um número.')

    main()

def listar_menu():
    print('Escolha uma das opções: \n')
    print('1. Cadastrar lista de números')
    print('2. Somar o número total\n')

def cadastrar_numeros():
    valor_informado = int(input("Digite um número para a lista: "))


    lista_de_numeros.append(valor_informado)

    main()

def somar_numeros():
    global valor_total

    for numero in lista_de_numeros:
        valor_total += numero

    os.system('cls')
    print(f'O valor total foi de: {valor_total}')

    main()

def exibir_informacoes():
    listar_menu()

    resposta = int(input('Digite uma das opções: '))

    try:
        if resposta == 1:
            cadastrar_numeros()
        elif resposta == 2:
            somar_numeros()
    except:
        erro_valor_invalido()



def main():
    exibir_informacoes()

if __name__ == '__main__':
    main()