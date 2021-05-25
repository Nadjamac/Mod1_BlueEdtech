# Testando o tipo de uma range
"""
b = range(5)
print(type(b))
print(b)
"""


# Usando o print sem pular linha
"""
lista2 = ["Tomate","Cerveja","Coca","Baralho"]
for l in lista2:
    print(l, end=", ") #end por padrão é = \n

for l in lista2:
    print(l)
"""

#Lista de compras com quantidade de elementos
"""
lista = []
quantidade = int(input("Quantos elementos você vai adicionar?\n"))
for a in range(quantidade):
    elemento = input("Digite o elemento")
    q_elemento = int(input("Quantos desse elemento?"))
    for i in range(q_elemento):
        lista.append(elemento)
    print("A lista está assim:")
    print(lista)
"""

# Criando uma lilsta de compras com número de itens
"""
lista = []
quantidade = int(input("Quantos elementos você vai adicionar?\n"))
for a in range(quantidade):
    lista.append(input("Quanto itens?"))
    lista.append(input("Digite o elemento"))
    print("A lista está assim:")
    print(lista)
"""

# Percorrendo com incremento 2 para listar números pares
"""
lista_pares = []
numeros = int(input("Até qual número? "))
for n in range(1,numeros,2):
    print(n+1)
"""