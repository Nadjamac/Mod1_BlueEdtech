lista = []

for item in range (1, 1000):
    preco = float(input("Digite o preço do produto ou 0 para finalizar compra: ").replace("," , "."))
    if preco == 0:
        break
    else:
        lista.append(preco)
        print("PRODUTO", item, ": R$", preco)

total = round(sum(lista) , 2)  
print("TOTAL:", total, "R$")
valor = float(input("DINHEIRO: R$"))
troco = valor - total
print("TROCO: R$", troco)


        




