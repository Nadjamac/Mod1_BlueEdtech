def media(n1 , n2, n3):
    media3 = (n1 + n2 + n3)/3
    media2 = 0
    menor = n3
    maior = n3
    if (n1 > n2 > n3) or (n2 > n1 > n3) :
        media2 = (n1 + n2)/2
    elif (n2 > n3 > n1) or (n3 > n2 > n1):
        media2 = (n2 + n3)/2
    else:
        media2 = (n1 + n3)/2
    if n1 < n2 and n1 < n3:
        menor = n1
    elif n2 < n1 and n2 < n3:
        menor = n2
    if n1 > n2 and n1 > n3:
        maior = n1
    elif n2 > n1 and n2 > n3:
        maior = n2
    print(f"A média com as 3 notas é: {media3:.2f}.")
    print(f"A média com as 2 maiores notas é: {media2:.2f}.")
    print(f"A maior nota é: {maior}.")
    print(f"A menor nota é: {menor}.")


n1 = float(input("Digite a N1: "))

n2 = float(input("Digite a N2: "))

n3 = float(input("Digite a N3: "))

media(n1, n2, n3)
    
    
