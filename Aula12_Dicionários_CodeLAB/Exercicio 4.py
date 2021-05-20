import random
import operator
import time

print("JOGO DOS DADOS: ")
tuplas = ()
lista = []
for n in range(4):
    jogador = input("Digite seu nome: ")
    print("DIGITE ENTER PARA SORTEAR O DADO")
    input() 
    numero = random.randint(1,10)
    tuplas = (jogador , numero)
    lista.append(tuplas)

lista_dict = dict(lista)
lista_ordem = sorted(lista_dict.items(), key=operator.itemgetter(1))

vencedor = max(lista_dict.items(), key=operator.itemgetter(1))[0]
print("O vencedor é: ")
time.sleep(1.5)
print(vencedor)
time.sleep(0.5)
print("\nRESULTADO FINAL: \n")
for nome , valor in lista_dict.items():
    print(f"O valor do dado para {nome} foi: {valor}")
