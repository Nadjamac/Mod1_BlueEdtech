print("*=*"*10)
print("\tDESCUBRA SE VOCÊ É O CULPADO!")
print("*=*"*10)
print("\tResponda as perguntas e veja se você é o culpado.")
print("*=*"*10)


contador = 0
print("Telefonou para a vítima?")
resposta1 = input("S - sim / N - não: "). lower()
if resposta1 == "s":
    contador += 1
print("Esteve no local do crime?")
resposta2 = input("S - sim / N - não: "). lower()
if resposta2 == "s":
    contador += 1
print("Mora perto da vítima?")
resposta3 = input("S - sim / N - não: "). lower()
if resposta3 == "s":
    contador += 1
print("Devia para a vítima?")
resposta4 = input("S - sim / N - não: "). lower()
if resposta4 == "s":
    contador += 1       
print("Já trabalhou com a vítima?")
resposta5 = input("S - sim / N - não: "). lower()
if resposta5 == "s":
    contador += 1

print("*=*"*10)

if contador == 2: 
    print("Você é SUSPEITO!")
elif 3 <= contador <= 4:
    print("Você é CÚMPLICE!")
elif contador == 5:
    print("Opa! VOCÊ É O ASSASSINO!")
else:
    print("Você é INOCENTE!")
 