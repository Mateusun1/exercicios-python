"""
3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.
"""

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
soma_total = 0

for i in numeros:
    if i %2 != 0:
        soma_total += i

print(f'A soma total dos números ímpares é: {soma_total}')