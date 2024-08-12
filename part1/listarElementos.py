import os
"""
2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.
"""
elementos = []
def listar_escolhas():
    print('1. Cadastrar Elementos')
    print('2. Listar Elementos\n\n')

def criar_elementos():
    valor = input('Digite qualquer coisa: ')

    elementos.append(valor)

    os.system('cls')

    print(f'Valor {valor} cadastrado!')

    main()

def listar_elementos():
    for elemento in elementos:
        print(f'Elemento cadastrado: {elemento}')
    
    main()

def exibir_menu():
    listar_escolhas()
    valor_escolhido = int(input('Digite um número da lista: '))

    try:
        if valor_escolhido == 1:
            criar_elementos()
        elif valor_escolhido == 2:
            listar_elementos()
    except:
        print('Valor Desconhecido')
    


def main():
    exibir_menu()

if __name__ == '__main__':
    main() 