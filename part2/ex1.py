"""
1. Atribua o valor 'Italiana' ao atributo categoria da instância restaurante_praca da classe Restaurante.
"""
class Restaurante():
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.categoria = 'Italiana'

"""
2. Acesse o valor do atributo nome da instância restaurante_praca da classe Restaurante.
"""

restaurante_praca.nome = 'Praça'
print(restaurante_praca.nome)

"""
Verifique o valor inicial do atributo ativo para a instância restaurante_praca e exiba uma mensagem informando se o restaurante está ativo ou inativo.
"""

print(f'Status do restaurante {restaurante_praca.ativo}')

"""
Acesse o valor do atributo de classe categoria diretamente da classe Restaurante e armazene em uma variável chamada categoria.
"""

categoria = Restaurante.categoria

"""
Altere o valor do atributo nome para 'Bistrô'.
"""

restaurante_praca.nome = 'Bistrô'

"""
Crie uma nova instância da classe Restaurante chamada restaurante_pizza com o nome 'Pizza Place' e categoria 'Fast Food'.
"""

restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'

"""
Verifique se a categoria da instância restaurante_pizza é 'Fast Food'.
"""

if restaurante_pizza.categoria == 'Fast Food':
    print(True)
else:
    print(False)

"""
Mude o estado da instância restaurante_pizza para ativo.
"""

restaurante_pizza.ativo = True
print(restaurante_pizza.ativo)

"""
Imprima no console o nome e a categoria da instância restaurante_praca.
"""
print(vars(restaurante_praca))