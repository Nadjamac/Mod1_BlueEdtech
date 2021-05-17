lista = ["Telefonou para a vítima? " , "Esteve no local do crime? ", "Mora perto da vítima? ", "Devia para a vítima? " , "Já trabalhou com a vítima ?"]

contador = 0

for pergunta in lista:
    a = input(pergunta)
    if a == "sim" or "s":
        contador += 1

if contador == 2:
    print("A pessoa é suspeita!")
elif 3 >= contador >= 4:
    print("A pessoa é cúmplice!")
elif contador == 5:
    print("A pessoa é culpada!")
else:
    print("A pessoa é inocente") 
