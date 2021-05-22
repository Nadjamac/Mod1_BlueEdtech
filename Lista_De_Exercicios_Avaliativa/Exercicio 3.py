import random
print("*=*"*10)
print("JOGO DA ADIVINHAÇÃO")
print("*=*"*10)

senha = "jogo2021"
senha_usuario = input("Digite sua senha: ").lower()

print("*=*"*10)
if senha_usuario == senha:
    print("BEM VINDO AO JOGO")
else:
    print("Você errou! Tente novamente.")
    senha_usuario = input("Digite sua senha: ").lower()
print("*=*"*10)
print("Tente adivinhar o número inteiro entre 0 e 20 que o computador sortear!")
print("Aperte enter para sortear um número:")
input()
print("*=*"*10)
numero = random.randint(0,20)
numero_usuario = int(input("Qual o número sorteado? "))
palpite = 0

while numero_usuario != numero:
    palpite += 1
    print("Você errou, tente novamente!")
    if numero_usuario > numero:
        print("O número correto é menor que seu palpite!")
    else:
        print("O número correto é maior que seu palpite!")
    numero_usuario = int(input("Qual o número sorteado? "))
else:
    print("*=*"*10)
    print("PARABÉNS, VOCÊ ACERTOU!!")
    print(f"Foram necessários {palpite} tentativas para zerar o jogo.")
    




