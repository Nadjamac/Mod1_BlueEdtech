#01
"""
class pessoa():
    def __init__(self, nome , sobrenome , idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
    
    def mostra_idade(self):
        print(f"A idade de {self.nome} é {self.idade}")
    
pessoa1 = pessoa("Lucas" , "Saraiva" , 19) #Criando um objeto

print(vars(pessoa1))  #imprimindo todas os parâmetros/características do objeto

print()

pessoa1.mostra_idade()  #Aplicando no objeto um dos métodos que pertencem à classe

"""

#02

from time import sleep

class Conta():
    def __init__(self, titular , saldo):
        self.titular = titular
        self.saldo = saldo
    
    def sacar(self):
        print('*=*'*10)
        valor = int(input("Qual valor deseja sacar?: "))
        print('*=*'*10)
        if valor > self.saldo:
            sleep(1)
            print("SALDO INSUFICIENTE!")
        else:
            sleep(1)
            print("RETIRE O VALOR SOLICITADO")
            print('*=*'*10)
            self.saldo = self.saldo - valor
            print(f'Saldo na conta: {self.saldo}')
    
    def depositar(self):
        print('*=*'*10)
        valor = int(input("Qual valor deseja depositar?: "))
        print('*=*'*10)
        sleep(1)
        print("DEPÓSITO REALIZADO COM SUCESSO!")
        print('*=*'*10)
        self.saldo = self.saldo + valor
        print(f'Saldo na conta: {self.saldo}')

conta1 = Conta("Julia" , 500)

print(vars(conta1))

conta1.sacar()

conta1.depositar()
        