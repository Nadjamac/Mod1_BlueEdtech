def IMC(peso, altura):
    return peso / (altura ** 2)

pes = input("Digite seu peso (em kg): ").replace(",", ".")
altur = input("Digite sua altura (em metros): ").replace(",", ".")

peso = float(pes)
altura = float(altur)

imc = IMC(peso , altura)

#O termo ":.2f" determina o número de casas decimais a ser printado. Ideal para casos envolvendo valores monetários!!
print(f"Seu IMC é {imc:.2f}.")