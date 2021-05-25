a = int(input("Diigite um número: "))

# #Enquando uma condição é verdadeira ele faz um determinado comando  
#  while a != 8:
#      print(f"{a} não é 8")
#      a = int(input("Diigite um número: "))
#  print("Agora é 8")

# #É possível criar uma iteração infinita com while true
# numero = 0
# while True:
#     print(numero)
#     numero += 1

#O comando continue para a execução e retorna
lista = []
elemento = "elemento"
while elemento.upper != FIM:
    elemento = input("Digite um elemento ou FIM para sair: ")
    if elemento.upper() == "CERVEJA":
        continue
    else:
        lista.append(elemento)

print(lista)
