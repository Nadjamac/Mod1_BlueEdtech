import datetime

continua = True #Definindo uma variável de continuação (ou não) do programa

lista = [] #Defininfo uma variável que para receber as listas com os cadastros

cadastro = dict() # Definindo uma variável para receber os cadastros em formato de dicionário

while continua :
    nome = input("Nome: ") #Variável recebe um nome do usuário
    nascimento = int(input("Ano de nascimento (AAAA): ")) #Variável recebe o ano de nascimento
    hoje = datetime.datetime.now().year #calculando o ano atual
    idade =  hoje - nascimento #variável recebendo idadeca
    ctps = input("Digite o número CTPS: ")
    if ctps == "0":
        cadastro[nome] = [idade , "Não tem CTPS"] #incluindo um item ao dicionário
        parada = input("Deseja acrescentar outro nome na lista? (S - sim/ N - não) ").upper() #Usuário definindo se a listagem deve continuar
        if parada == "N":
            continua = False #condição de parada do programa
        print()
    else:
        contratacao = int(input("Ano de contratação: "))
        salario = int(input("Digite o valor do último salário: "))
        aposent = idade + 35 - hoje  + contratacao
        cadastro[nome] = [idade, ctps , aposent]
        parada = input("Deseja acrescentar outro nome na lista? (S - sim/ N - não) ").upper()
        if parada == "N":
            continua = False
        print()


print(cadastro)






