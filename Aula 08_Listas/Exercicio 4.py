frase = input("Digite uma frase ")

contador = 0

for letra in frase:
    if letra in "aeiouAEIOUÁÀÃÂáàâãÉÈÊêéèÓÒÔÕóòõôÚÙÛúùûÍÌÎíìî":
        contador += 1

print(f"Essa frase tem {contador} vogais.")
        