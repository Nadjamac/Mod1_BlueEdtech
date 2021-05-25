class Herói(): #definindo uma classe
    def __init__(self, nome, idade, peso): #definindo método construtor - que vai definir os parâmetros necessários para um objeto pertencer a essa classe
        self.nome = nome
        self.idade = idade
        self.peso = peso
    
    def engordar(self, peso): #definindo um método para a classe
        self.peso += peso

a = Herói("Capitão América" , 30 , 85) #Criando um objeto
b = Herói("Alerquina" , 27, 75)
print(vars(a))
print(vars(b))

a.engordar(10) #Aplicando um método ao objeto - 'objeto'.'nome'
print(vars(a))

b.peso = a.peso #relacionando um parâmetro de um objeto e outro

print()
print(vars(b))