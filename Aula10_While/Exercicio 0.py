numero1 = ()
numero2 = ()

soma = numero1 + numero2

while soma != 50:
    numero1 = float(input("Digite um número: "))
    numero2 = float(input("Digite um número: "))
    soma = numero1 + numero2
    if soma != 50:
        print ("A soma ainda não é 50!")
    else:
        print("A soma é 50!")
        break

 