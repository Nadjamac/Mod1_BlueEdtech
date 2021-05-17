frase = input("Digite uma frase: ")

for letra in frase:
    if letra in "aeiouAEIOUÁÀÃÂáàâãÉÈÊêéèÓÒÔÕóòõôÚÙÛúùûÍÌÎíìî":
        frase = frase.replace(letra , " ")

print(frase)

