import os
"""
1. Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.✔
"""

pessoas = [{'nome': 'Matheus', 'idade': 21, 'cidade': 'Caxias do Sul', 'profissao': 'Analista de Qualidade'},
           {'nome': 'João', 'idade': 21, 'cidade': 'Caxias do Sul', 'profissao': 'Analista de Qualidade'}]

"""
2. Utilizando o dicionário criado no item 1:

Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);✔
Adicione um campo de profissão para essa pessoa;✔
Remova um item do dicionário.
"""
def limpar_cmd():
    os.system('cls')

def printar_erro(erro_mensagem):
    print(erro_mensagem)

def exibir_dados_escolha():
    print('Escolha qual dado você quer atualizar: \n')
    print('1. Nome')
    print('2. Idade')
    print('3. Cidade')
    print('4. Profissão')

def atualizar_nome():
    limpar_cmd()
    pesquisar_nome = input('Digite o nome da pessoa que você gostaria de atualizar: \n')

    for pessoa in pessoas:
        if pesquisar_nome == pessoa['nome']:

            nome_desejado = input(f'{pesquisar_nome} foi encontrado! Digite o nome substituto: ')
            pessoa.update({'nome' :nome_desejado})

            limpar_cmd()
            print('Perfil alterado com sucesso!')
            main()
        else: 
            printar_erro('Pessoa não Encontrada, tente novamente!')
            main()

def atualizar_idade():
    limpar_cmd()
    pesquisar_nome = input('Digite o nome da pessoa que você gostaria de atualizar: \n')

    for pessoa in pessoas:
        if pesquisar_nome == pessoa['nome']:

            idade = int(input(f'{pesquisar_nome} foi encontrado! Digite a idade substituto: '))
            pessoa.update({'idade' :idade})

            limpar_cmd()
            print('Perfil alterado com sucesso!')
            main()
        else: 
            printar_erro('Pessoa não Encontrada, tente novamente!')
            main()

def atualizar_cidade():
    limpar_cmd()
    pesquisar_nome = input('Digite o nome da pessoa que você gostaria de atualizar: \n')

    for pessoa in pessoas:
        if pesquisar_nome == pessoa['nome']:

            cidade = input(f'{pesquisar_nome} foi encontrado! Digite a cidade substituta: ')
            pessoa.update({'cidade' :cidade})

            limpar_cmd()
            print('Perfil alterado com sucesso!')
            main()
        else: 
            printar_erro('Pessoa não Encontrada, tente novamente!')
            main()

def atualizar_profissao():
    limpar_cmd()
    pesquisar_nome = input('Digite o nome da pessoa que você gostaria de atualizar: \n')

    for pessoa in pessoas:
        if pesquisar_nome == pessoa['nome']:

            profissao = input(f'{pesquisar_nome} foi encontrado! Digite a profissao substituta: ')
            pessoa.update({'profissao': profissao})

            limpar_cmd()
            print('Perfil alterado com sucesso!')
            main()
        else: 
            printar_erro('Pessoa não Encontrada, tente novamente!')
            main()

def atualizar_dados():
    exibir_dados_escolha()

    opcao_desejada = int(input('Escolha uma das opções acima: '))

    if opcao_desejada == 1:
        atualizar_nome()
    elif opcao_desejada == 2:
        atualizar_idade()
    elif opcao_desejada == 3:
        atualizar_cidade()
    elif opcao_desejada == 4:
        atualizar_profissao()
    else:
        printar_erro('Erro: O resultado não bate com os caracteres exibidos acima.')

def exibir_dados_pessoas():
    for pessoa in pessoas:
        print(f'| Nome: {pessoa['nome'] } | Idade: {pessoa['idade']} | Cidade: {pessoa['cidade']} | Profissão: {pessoa['profissao']} |\n')

    input('Digite ENTER para voltar para o menu')
    main()    

def deletar_dados():
    limpar_cmd()
    pesquisar_nome = input('Digite o nome da pessoa que você gostaria de deletar: \n')

    for pessoa in pessoas:
        if pesquisar_nome == pessoa['nome']:
            tipo_item = input('Digite o tipo de item que deseja deletar: \n')
            del pessoa[tipo_item] 
            
            limpar_cmd()
            print(f'Tipo item {tipo_item} deletado com sucesso!')
            main()
        else: 
            printar_erro('Pessoa não Encontrada, tente novamente!')
            main()

def exibir_menu():
    print('Bem Vindo, escolha uma das opções abaixo: \n')
    print('1. Atualizar os dados pessoais.')
    print('2. Listar os dados pessoais.')
    print('3. Remover um item.\n')

def iniciar_menu():
    exibir_menu()

    valor = int(input('Escolha uma das opções acima: '))

    if valor == 1:
        atualizar_dados()
    elif valor == 2:
        exibir_dados_pessoas()
    elif valor == 3:
        deletar_dados()



def main():
    iniciar_menu()

if __name__ == '__main__':
    main()