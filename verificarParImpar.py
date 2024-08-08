import os

numero_digitado = int(input('Digite um número: '))

if numero_digitado % 2 == 0:
    os.system('cls')
    print('Esse número é par')
else:
    os.system('cls')
    print('Esse número é impar')