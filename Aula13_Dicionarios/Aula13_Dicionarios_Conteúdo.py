#Ciriando um dicionário
atores_vingadores = {"Chris Evans" : "Capitão América" , "MArk Ruffalo" : "Hulk" , "Tom Hiddeltston" : "Loki" , "Chris Hemworth" : "Thor" , "Robert Downey Jr" : "Homem de Ferro" , "Scarlett Johansson" : "Viúva Negra"}

#Adicionando novos valores a um dicionário

atores_vingadores ["Michael Mayers"] = "Coringa"
atores_vingadores ["Xuxa"] = "Mulher Maravilha"
atores_vingadores ["Lady Gaga"] = "Vingadora Suprema"
atores_vingadores ["Sandy"] = "Wanda"
atores_vingadores ["Michael Jr"] = "Batman"

print(atores_vingadores)

#Removendo itens de um dicionário
del atores_vingadores["Michael Mayers"]
print(atores_vingadores)

#Removendo um item do dicionario com pop, o programa volta o valor removido e pode ter uma msg em caso de erro
print(atores_vingadores.pop("Xuxa", "Ator não encontrado"))

print(atores_vingadores)

atores_vingadores.pop("Chris Evans")
atores_vingadores.pop("Sandy")

print(atores_vingadores)

#Unindo dicionário usand for
animais = {"Cachorro" : "Vira Lata Caramelo" , "Cavalo" : "Mangalarga" , "gato" : "Siamês"}

for item in animais:
     print(item)
     atores_vingadores[item] = animais [item]

print(atores_vingadores)

#Unindo dicionários com função update

atores_vingadores.update(animais)

print(atores_vingadores)