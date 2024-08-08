import os

idade = int(input('Digite sua idade: '))

if idade <= 12:
    os.system('cls')
    print('Você é criança')
elif idade <= 17:
    os.system('cls')
    print('Você é adolescente')
else: 
    os.system('cls')
    print('Você é adulto')