#01 - Utilizando estruturas condicionais faça um programa que pergunte ao usuário dois números e mostre:
   # A soma deles;
   # A multiplicação entre eles;
   # A divisão inteira deles;
   # Mostre na tela qual é o maior;
   # Verifique se o resultado da soma é par ou impar e mostre na tela;
   # Se a multiplicação entre eles for maior que 40, divida pelo resultado da divisão inteira e mostre o resultado na tela. Se não, mostre que a multiplicação não foi maior que 40.

numero1 = float(input("Digite um número: "))
numero2 = float(input("Digite outro número: "))

soma = numero1 + numero2
print(f"A soma dos números é: {soma}")
print()
produto = numero1 * numero2
print(f"O produto dos números é: {produto}")
print()
divisao = numero1 // numero2
print(f"A divisão inteira entre os números é: {divisao}")
print()
if numero1 > numero2:
    print(f"O número {numero1} é o maior.")
else:
    print(f"O número {numero2} é o maior.")
print()
if soma % 2 == 0:
    print("A soma é par!")
else:
    print("A soma é ímpar!")
print()
if produto > 40:
    resultado = produto / divisao
    print(f"A divisão entre o produto entre os número e a divisão entre os números é: {resultado}")
else:
    print("O produto não é maior que 40!")




