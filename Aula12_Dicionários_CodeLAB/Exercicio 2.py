
lista = range(1, 11)
tuplas = ()

dicionario = []
for n in lista:
    tupla = (n , n**2)
    dicionario.append(tupla)

dicionario_final = dict(dicionario)

print(dicionario_final)