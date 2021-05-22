def menor(x , y):
    if x > y:
        print("O valor", y, "é o menor.")
    elif x < y:
        print("O valor", x, "é o menor.")
    else:
        print("Os valores são iguais.")


numero1 = float(input("Digite um número: ").replace("," , "."))
numero2 = float(input("Digite um número: ").replace("," , "."))

menor(numero1 , numero2)

        