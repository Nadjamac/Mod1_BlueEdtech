chaves = [1 , 4 , 5 , 6 , 7 , 9]

tuplas = ()

dicionario = []
for n in chaves:
    tupla = (n , n**2)
    dicionario.append(tupla)

dicionario_final = dict(dicionario)

print(dicionario_final)
