
for a in range(1000 , 10000):
    dezena1 = a // 100
    dezena2 = a % 100
    soma_dezenas = dezena1 + dezena2
    if soma_dezenas**2 == a:
        print(a)







