"""
5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir 
a tabuada desse número, indo de 1 a 10.
"""

valor = int(input('Digite um número para a tabuada: '))

for i in range(1,11):
    print(f'{i} X {valor} = ', i * valor)