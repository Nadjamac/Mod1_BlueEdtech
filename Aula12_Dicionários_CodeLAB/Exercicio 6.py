from numpy import mean

parada = True
lista = []
idades = []
mulheres=[]

while parada:
    nome = input("Digite o nome: ")
    sexo = input("Digite o sexo (F- Feminino / M - Masculino): ").lower()
    if sexo != "f" or sexo != "m":
        print("Sexo não encontrado")
        sexo = input("Digite o sexo (F- Feminino / M - Masculino): ").lower()
        if sexo == "f":
            mulheres.append(nome)
    idade = int(input("Digite sua idade: "))
    dicionario = {"nome": nome , "sexo": sexo , "idade": idade}
    lista.append(dicionario)
    idades.append(idade)
    parada = input("Uma nova pessoa irá se cadastrar? (S-Sim / N - Não): ").lower()
    if parada not in "sn":
        print("Opção não existente!")
        parada = input("Uma nova pessoa irá se cadastrar? (S-Sim / N - Não): ").lower()
    if parada == "n":
        parada = False

print("A Quantidade de pessoas é:" , len(lista))
print()
media = sum(idades) / len(idades)
print(f"A média da idade é: {media}")
print("As mulheres são:")
for i in mulheres:
    print(i)
print()
print("Idades acima da média: ")
for i in range(len(idades)):
    if idades[i] > media:
        print(idades[i])
   







