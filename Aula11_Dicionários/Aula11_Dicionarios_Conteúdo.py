#Criando uma lista de tuplas -> estrutura de dados que associa um elemento a outro
# lista = [("Ana" , "123-456") , ("Bruno" , "321-654") , ("Cris" , "213 - 546") , ("Daniel" , "231 - 564") , ("Elen" , "111-222")]


#Sintaxe de um dicionário

# dicionario = {"Ana" : "123-456"}

#Criando um dicionário

# lista_dicionario = dict(lista)
# print(lista_dicionario)

# Acessando um valor dentro de um dicionário
#O valor é acessado pela chave do dicionário
# print(lista_dicionario["Ana"])
# print(lista_dicionario.get("Ana"))

# nome = input("Digite um nome: ")
# print(lista_dicionario.get(nome , "Valor não encontrado!")

atores_vingadores = {"Chris Evans" : "Capitão América" , "MArk Ruffalo" : "Hulk" , "Tom Hiddeltston" : "Loki" , "Chris Hemworth" : "Thor" , "Robert Downey Jr" : "Homem de Ferro" , "Scarlett Johansson" : "Viúva Negra"}

ator = input("Digite o nome do ator: ")

print(atores_vingadores.get(ator , "O nome não existe!")) 

#interagindo com chave e valor

for chave , valor in atores_vingadores.items():
    print(f"O valor da chave {chave} é: {valor}")