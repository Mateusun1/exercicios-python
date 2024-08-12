"""
Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. 
Crie uma instância dessa classe e atribua valores aos seus atributos.
"""
class Carro:
    
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano


carro_vermelho = Carro('BMW M3', 'Vermelho', 1985)

"""
Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. 
Instancie um restaurante e atribua valores aos seus atributos.
Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como parâmetros e inicia ativo como False por padrão. 
Crie uma instância utilizando o construtor.
Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância, seja exibida uma mensagem formatada com o nome e a categoria. 
Exiba essa mensagem para uma instância de restaurante.
"""
class Restaurante:
    def __init__(self, nome, categoria, avaliacao, valor):
        self.nome = nome
        self.categoria = categoria
        self.avaliacao = avaliacao
        self.valor = valor
        self.ativo = False

    def __str__(self):
        return f'|{self.nome} | {self.categoria} | {self.avaliacao} | {self.valor} | {self.ativo} |'
restaurante_pizza = Restaurante('Eki Pizza', 'Pizzaria', '5', '1200.99')

"""
Crie uma classe chamada Cliente e pense em 4 atributos. 
Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos 
através de um método construtor.
"""

class Cliente:
    clientes = []

    def __init__(self, nome, idade, genero, cidade):
        self.nome = nome
        self.idade = idade
        self.genero = genero
        self.cidade = cidade
        Cliente.clientes.append(self)

    def listar_clientes():
        for cliente in Cliente.clientes:
            print(f'| {cliente.nome} | {cliente.idade} | {cliente.genero} | {cliente.cidade} |')

cliente1 = Cliente('Matheus', 21, 'Masculino', 'Caxias do Sul')
cliente2 = Cliente('Pedro', 16, 'Masculino', 'Caxias do Sul')
cliente3 = Cliente('Noé', 44, 'Masculino', 'Caxias do Sul')

Cliente.listar_clientes()
