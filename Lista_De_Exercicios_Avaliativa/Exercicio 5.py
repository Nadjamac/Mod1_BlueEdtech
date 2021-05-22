print("*=*"*10)
print("\tCALCULADORA DE VOGAIS")
print("*=*"*10)
frase = input("Digite uma frase: ")
print()

contador_a= 0
contador_e= 0
contador_i= 0
contador_o= 0
contador_u= 0

for letra in frase:
    if letra in "aAÁÀÃÂáàâã":
        contador_a +=1
    if letra in "eEÉÈÊêéè":
        contador_e +=1
    if letra in "iIÍÌÎíìî":
        contador_i +=1
    if letra in "oOÓÒÔÕóòõô":
        contador_o +=1
    if letra in "uUÚÙÛúùû":
        contador_u +=1 

for letra in frase:
    if letra in "aeiouAEIOUÁÀÃÂáàâãÉÈÊêéèÓÒÔÕóòõôÚÙÛúùûÍÌÎíìî":
        frase = frase.replace(letra , " ")

print(f"\tQuantidade de vogais a = {contador_a}")
print(f"\tQuantidade de vogais e = {contador_e}")
print(f"\tQuantidade de vogais i = {contador_i}")
print(f"\tQuantidade de vogais o = {contador_o}")
print(f"\tQuantidade de vogais u = {contador_u}")

print("*=*"*10)

print("\tA frase sem vogais fica assim: ")
print(frase)
print("*=*"*10)
soma = contador_a + contador_e + contador_i + contador_o + contador_u
print(f"Foram retiradas {soma} letras.")
