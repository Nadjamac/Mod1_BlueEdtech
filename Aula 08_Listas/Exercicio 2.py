#Recebdno um arquivo de texto

arquivo = open(r'C:\Users\Cliente\Google Drive\BLUE\M1_Logica de Programação\Lista Palavras.txt')

#Lendo um arquivo de texto em formato string para o python
palavras = arquivo.read().replace("\n" , " ")

#Limpando a string
palavras2 = palavras.split(" ")


print("As palavras do jogo são países latino-americanos:")
print(palavras2)


#Sorteando uma palavra

print("\n\nAperte enter para sortear uma palavra para o jogo.")
input()

import random


palavraescolhida = random.choice(palavras2).upper()

palavra_forca = ["_" for i in palavraescolhida]

maximo = len(palavraescolhida) + 6
chance = 0
#Criando o jogo da Forca

for i in range(maximo):
    if palavra_forca.count('_') == 0 or chance == 6: break
    letra = input('Digite uma letra: ').upper()
    if letra in palavra_forca:
        print('Você já digitou essa letra antes.\nA palavra é: ', end = '')
        print(' '.join(palavra_forca))
        continue
    if letra in palavraescolhida:
        print('A palavra é: ', end = '')
        for n in range(len(palavraescolhida)):
            if letra == palavraescolhida[n]:
                del palavra_forca[n]
                palavra_forca.insert(n, letra)        
        print(' '.join(palavra_forca))        

    else:
        chance += 1
        if chance != 6:
            print('Você errou pela', str(chance), 'ª vez. Tente novamente!')

if palavra_forca.count('_') == 0:
    print('Parabéns! Você acertou a palavra!')
else:
    print('Você errou pela 6ª vez.\nFORCA!!! VOCÊ PERDEU!!!')


