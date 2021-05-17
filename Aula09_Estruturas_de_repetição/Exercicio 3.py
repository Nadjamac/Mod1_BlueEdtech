preco = float(input("Preço do pão: R$").replace("," , "."))

for item in range(1 , 51):
    precopao = round(item * preco, 2)
    print(item , "- R$", precopao)

