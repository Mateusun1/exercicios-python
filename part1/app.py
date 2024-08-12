import os

restaurantes = [{'nome': 'Praça', 'categoria': 'Japonesa', 'ativo': False}, 
                {'nome': 'Cantina', 'categoria': 'Pizza', 'ativo': True},
                {'nome': 'Pizzaiolo', 'categoria': 'Pizza', 'ativo': False}]

def retornar_ao_menu_principal():
    input('\nDigite enter para voltar ao menu principal ')
    main()

def exibir_subtitulo(titulo):
    os.system('cls')
    print(titulo)

def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░""")

def exibir_opcoes():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Ativar Restaurante')
    print('4. Sair Restaurante\n')

def finalizar_app():
    exibir_subtitulo('Encerrando Programa...')

def opcao_invalida():
    print('opção invalida')
    input('digite um tecla para voltar a tela principal: ')
    main()

def alternar_estado_restaurante():
    nome_restaurante = input('Escreva o nome do restaurante que ja foi cadastrado: ')
    
    print ('Alteranto estado do restaurante...')

    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            os.system('cls')
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O Restaurante {nome_restaurante} foi inativado com sucesso!'
            print(mensagem)

    if not restaurante_encontrado:
        print('Restaurante não encontrado!')

    retornar_ao_menu_principal()


def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes\n')
    nome_do_restaurante = input('Digite o nome do restaurante que você quer cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    
    restaurante_completo = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(restaurante_completo)

    print(f'O Restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    retornar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listando todos os restaurantes:')
    
    for restaurante in restaurantes:

        ativo = 'ativado' if restaurante['ativo'] else 'Desativado'
        print(f'{restaurante['nome']} | {restaurante['categoria']} | {ativo}')
    retornar_ao_menu_principal()
    main()










def escolher_opcoes():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()
        

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main()