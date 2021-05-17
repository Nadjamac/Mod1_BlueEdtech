n = int(input("Digite um número inteiro: \n"))

lista = range(n+1)
contador = 0
divisores = []

for numero in range(1, n+1):
    if n % numero == 0:
        contador += 1
        divisores.append(numero)
    

if contador == 2:
    print("Esse número é primo!")
else:
    print("Os divisores do número", n, "são:", divisores)
    