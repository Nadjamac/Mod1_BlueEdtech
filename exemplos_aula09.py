lista = ['Ana', 'Bernardo', 'Carlos', 'Daniel', 'Eurico', 'Filipe', 'Gabriel']
# ITERAR

for nome in lista:
    for letra in nome:
        print(letra)
 
#print(lista)
# PARA CADA ELEMENTO DA LISTA:
#for item in lista:
#    print(item)

# range(5) -> [0, 1, 2, 3, 4]:
# for item in range(5) -> for item in [0, 1, 2, 3 ,4]:
# a = range(6,21,2)
# a = [6, 8, 10, 12, 14, 16, 18, 20]
"""for item in range(11):
    if (item % 2 == 0 and item != 0):
        print(item)
"""
"""
lista = [10, 20, 10, 30, 10, 40, 10, 50, 10, 10, 10]
contador = 0
for item in lista:
    if item == 10:
        contador += 1 # contador = contador + 1
        print(item)
    if contador > 3:
        print("existem mais do que 3 itens iguais a 10")
        break # PARE!
"""

# lista = [10, 20, 10, 30, 10, 40, 10, 50, 10, 10, 10, 20, 10, 10, 10, 20, 2, 3, 4, 5, 56, 11]
# lista[0] = 10
# lista[8] = 10
# lista[7] = 50
# max(lista) -> 56
# min(lista) -> 2
# len(lista) -> 22
"""
tamanho = len(lista)
for i in range(tamanho):
    print(lista[i])
"""

lista = [10, 20, 10, 30, 10, 40, 10, 50, 10, 10, 10, 20, 10, 10, 10, 20, 2, 3, 4, 5, 56, 11]
lista.insert(8,500)
print(lista)
lista2 = []
for item in lista:
    if item not in lista2:
        lista2.append(item)
lista2.sort()
print(lista2)




"""
nome = "Eurico Nicacio"
for letra in nome:
    if (letra != ' '):
        print(letra)
"""

