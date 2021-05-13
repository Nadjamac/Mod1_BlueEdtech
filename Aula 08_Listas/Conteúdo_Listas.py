#Definindo uma lista
lista1 = [1 , 2, 3]

# Imprimindo a lista inteira
print(lista1)

# imprimindo o primeiro item da lista
print(lista1[0])

# É possível ter listas dentro de listas
lista2 = [10, 20, [30, 40]]

print(lista2[2])

#Posso selecionar um item dentro da lista dentro da lista :p

print(lista2[2][1])

#É possível alterar os índices da lista

lista1[0] = 50

print(lista1)

#E possível remover um item de uma lista 

del(lista1[0])

print(lista1)

#Fatiamento de listas é parecido com as strings. Por exemplo: fatiando até o indice 1

print(lista1[:1])

#é possível criar uma lista usando "range"

lista3 = list(range(5))
print(lista3)

#É possível tambem criar uma lista de valores com um determinado intervalo

lista4 = list(range(3, 8, 2))
print(lista4)