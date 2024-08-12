"""
4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.
"""

dicionarios = {'nome': 'Matheus'}
nome = input('Digite uma chave especifica: \n')

if nome in dicionarios:
    print(f'O nome {nome} existe no dicionario!')
else:
    print(f'O nome {nome} não existe no dicionario!')        