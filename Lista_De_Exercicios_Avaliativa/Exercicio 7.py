 def par_impar(numero):
     situacao = " "
     if numero % 2 == 0:
         situacao = "par"
     else:
         situacao = "ímpar"
     return situacao

print("*=*"*10)
print("CADÊ OS PARES E OS ÍMPARES?")
print("*=*"*10)
print("Digite 7 números e descubra quais são os pares e os ímpares")
print("*=*"*10)

pares = []
impares = []

for i in range(7):
    numero = (int(input("Digite um número inteiro: ").replace("," , ".")))
    condicao = par_impar(numero)
    if condicao == "par":
        pares.append(numero)
    else:
        impares.append(numero)


print("*=*"*10)
pares_crescente = sorted(pares)
impares_crescente = sorted(impares)
print(f"Os valores pares em ordem crescente são: {pares_crescente}.")
print(f"Os valores ímpares em ordem crescente são: {impares_crescente}.")


