def calculadora_verdade(x , y , limite):
    if (x + y) > limite:
        print(True)
    else:
        print(False)


numero1 = float(input("Digite um número: ").replace("," , "."))
numero2 = float(input("Digite um número: ").replace("," , "."))
limite = float(input("Digite um número: ").replace("," , "."))

calculadora_verdade(numero1 , numero2, limite)