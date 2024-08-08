import os

x = int(input('Digite um número: '))
y = int(input('Digite outro número: '))

primeiro_quadrante = x > 0 and y > 0
segundo_quadrante = x < 0 and y > 0
terceiro_quadrante = x < 0 and y < 0
quatro_quadrante = x > 0 and y < 0

if primeiro_quadrante:
    os.system('cls')
    print('Primeiro Quadrante')
elif segundo_quadrante:
    os.system('cls')
    print('Segundo Quadrante')
elif terceiro_quadrante:
    os.system('cls')
    print('Terceiro Quadrante')
elif quatro_quadrante:
    os.system('cls')
    print('Quarto Quadrante')
else:
    os.system('cls')
    print('o ponto está localizado no eixo ou origem.')