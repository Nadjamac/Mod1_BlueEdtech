nomes = []

for item in range(1000):
    a = input("Digite um nome a acrescentar na lista ou 0 para encerrar: \n").lower()
    if a == "0":
        print("Lista Encerrada.")
        break
    else:
        nomes.append(a)

nome_verificacao = input("Digite um nome para ser verificado: \n").lower()

if nome_verificacao in nomes:
    print("Este nome está na lista!")
else:
    print("Este nome não está na lista!")