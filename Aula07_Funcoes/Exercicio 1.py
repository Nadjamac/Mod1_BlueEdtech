def menor(x , y):
    menor = y
    if x < y:
        menor = x
    return menor

num1 = float(input("Digite um número: ").replace("," , "."))
num2 = float(input("Digite um número: ").replace("," , "."))

minimo = menor(num1 , num2)

print(f"O menor número é o {minimo}.")
