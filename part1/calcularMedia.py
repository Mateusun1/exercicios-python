import os
"""
7 - Construa um código que calcule a média dos valores em uma lista. 
Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.
"""

valores = []
valor_total = 0

def exibir_menu():
    print('Escolha uma das opções: \n')
    print('1. Inserir Nota do Aluno')
    print('2. Somar Média do aluno\n\n')

def inserir_media():
    nota = float(input('Insira a nota do aluno: '))

    valores.append(nota)

    print('Nota inserida com sucesso!')

    main()

def erro_tamanho_zero():
    os.system('cls')
    print('Erro: Tamanho da lista não pode ser igual a zero, preencha a lista antes de somar a média!')
    main()

def erro_caractere_invalido():
    os.system('cls')
    print('Erro: Caractere invalido, tente novamente!')
    main()

def calcular_media():
    global valor_total
    try: 
        for i in valores:
            valor_total += i
        
        media = valor_total / len(valores)

        print(f'A média final do aluno é de: {media}')
    except:
        erro_tamanho_zero()

def exibir_informacoes():
    exibir_menu()

    resposta = int(input('Escolha uma das opções: '))

    try:
        if resposta == 1:
            inserir_media()
        elif resposta == 2:
            calcular_media()
    except:
        erro_caractere_invalido()


def main():
    exibir_informacoes()

if __name__ == '__main__':
    main()