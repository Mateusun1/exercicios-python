"""

Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo. 

Inicie o atributo ativo como False por padrão.


Na classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem formatada com o 

titular e o saldo da conta. Crie duas instâncias da classe e imprima essas instâncias.


Adicione um método de classe chamado ativar_conta à classe ContaBancaria que define o atributo ativo como True. 

Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.


Refatore a classe ContaBancaria para utilizar a abordagem "pythonica" na criação de atributos. 

Utilize propriedades, se necessário.


Crie uma instância da classe e imprima o valor da propriedade titular.

"""

class ContaBancaria:


    def __init__(self, titular, saldo):

        self._titular = titular

        self._saldo = saldo

        self._ativo = False


    def __str__(self):

        return f'{self._titular} | {self._saldo} | {self._ativo}'


    def ativar_conta(self):

        self._ativo = not self._ativo


    @property

    def ativo(self):

        return self._ativo


    def exibir_saldo(self):

        print(f'Saldo restante: {self._saldo}')


conta1 = ContaBancaria('Matheus', 1200.29)

conta1.ativar_conta()

conta1.exibir_saldo()

conta2 = ContaBancaria('Pedro', 1500.29)


"""

Crie uma classe chamada ClienteBanco com um construtor que aceita 5 atributos. 

Instancie 3 objetos desta classe e atribua valores aos seus atributos através do método construtor.


Crie um método de classe para a conta ClienteBanco.

"""

class ClienteBanco:
    clientes_ativos = []
    def __init__(self, nome, cpf, idade, cidade, estado_civil):
        self._nome = nome
        self._cpf = cpf
        self._idade = idade
        self._cidade = cidade
        self._estado_civil = estado_civil
        ClienteBanco.clientes_ativos.append(self)

    @classmethod
    def exibir_clientes(cls):
        for cliente in cls.clientes_ativos:
            print(f'{cliente._nome} | {cliente._cpf} | {cliente._idade} | {cliente._cidade} | {cliente._estado_civil}')

    
cliente1 = ClienteBanco('Matheus', '11122233344', 21, 'Caxias do Sul', 'Solteiro')
cliente2 = ClienteBanco('Pedro', '11122233344', 16, 'Caxias do Sul', 'Solteiro')
cliente3 = ClienteBanco('Joao', '11122233344', 31, 'Caxias do Sul', 'Solteiro')

ClienteBanco.exibir_clientes()