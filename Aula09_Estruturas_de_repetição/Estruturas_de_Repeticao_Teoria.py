#Sintaxe para aplicação do comando for - quando você quer aplicar uma repetição
lista = ["Ana" , "Bernardo" , "Carlos" , "Daniel" , "Eurico" , "Filipe" , "Gabriel"]

#Quero dizer, para cada elemento da lista, execute um comando, no caso, printar o elemento
for elemento in lista:
     print(elemento)

#A função "range" cria uma lista de n-1 elementtos
#Printando números pares de uma determinada lista 
for item in range(11):
     if (item % 2 == 0):
         print(item)

#O comando "break" para a execução do comando for
#Por exemplo, quero que o programa pare no primeiro 10 que ele achar, apenas para detectar o valor
lista2 = [10 , 20 , 30 , 10 , 40 , 50 , 60]

for item in lista2:
     if item == 10:
         print ("existe 10")
#Parando a estrutura de repetição
         break

lista3 = [10 , 20 , 30 , 10 , 40 , 10 , 60, 10]

for item in lista3:
    contador = 0
    if item == 10:
        contador += 1
    if contador > 3:
        print("Tem mais de 3 números 10.")
    break