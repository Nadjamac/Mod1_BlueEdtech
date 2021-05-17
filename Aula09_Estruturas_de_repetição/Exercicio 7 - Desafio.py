import random

print("O JOGO DOS NUMEROS!\n")

print("Aperte enter para escolher um número entre 0 e 100 e tente acertá-lo!")
input()

chance = 0
numero_alvo = random.randint(1, 101)

for n in range (10):
    numero = input("\nDigite um número inteiro: ")
    if numero != numero_alvo:
        print("\nVocê errou. Tente Novamente!")
        chance += 1
    else:
        print("\nParabéns, você acertou!!")
    if chance == 10: 
        print("Você errou pela 10ª vez. End Game!")
        break