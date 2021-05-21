estoque = {"tomate": [1000, 2.30], "alface": [500, 0.45], "batata": [2001, 1.20],
"feijão": [100, 1.50]}
total = 0
compras = {}

while True:
    produto = input("Digite o produto a ser vendido ou 0 para encerrar: ").lower()
    if produto == "0" : break
    if produto not in estoque.keys():
        print("Produto Inexistente!")
        continue
    else:    
        quantidade = int(input("Digite a quantidade a ser vendida: "))
        if quantidade > estoque[produto][0]:
            print("Quantidade solicitada indisponível!")
        preco_unitario = estoque[produto][1]
        custo = quantidade * preco_unitario
        print(f"\t{produto}\t{quantidade}\tx\t{preco_unitario}\t={custo:.2f}")
        estoque[produto][0] -= quantidade
        total += custo
        compras[produto] = [quantidade, custo]
    if estoque[produto][0] == 0:
        print("Produto Indisponível!")
         

print("")
print("*-=-*"*10)
print("COMPRA REALIZADA")
print("*-=-*"*10)

for k,v in compras.items():
    print(f"{k}:\t{v[0]}\tx\t{estoque[k][1]}\t={v[1]}")

print("*-=-*"*10)
print(f"Valor total da compra: R$ {total:6.2f}")  




