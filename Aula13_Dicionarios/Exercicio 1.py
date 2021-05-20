
aniversario = dict()


while True:
    nome = input("Digite o nome da celebridade ou 0 para sair: ")
    if nome == "0": break
    data_aniversario = input("Digite a data de nascimento da celebridade (dd/mm/yyy): ")
    aniversario [nome] = data_aniversario

print("Seja bem-vindo ao nosso calendário. Sabemos a data de nascimento das seguintes celebridades: ")

for item in aniversario:
    print(item)

print()
nome = input("Digite um nome de uma celebridade para saber sua data de nascimento: ")

print(aniversario.get(nome , "Nome não encontrado!"))