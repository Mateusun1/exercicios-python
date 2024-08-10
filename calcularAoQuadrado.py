"""
3 - Crie um dicionário utilizando para representar números e seus quadrados de 1 a 5.
"""
numero = [1, 2, 3, 4, 5]
numeros_ao_quadrado = []
for i in numero:
    valor_ao_quadrado = i ** 2
    numeros_ao_quadrado.append(valor_ao_quadrado)

print(numeros_ao_quadrado)