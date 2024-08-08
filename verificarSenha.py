import os

usuario = input('Digite seu Usuario: ')
senha = input('Digite sua Senha: ')

if usuario == 'root' and senha == '123':
    os.system('cls')
    print('Bem Vindo!')
else:
    os.system('cls')
    print('Usuario ou Senha incorretas!')