import time
import datetime

def calcuradora_idade(nascimento):
    hoje = datetime.datetime.now().year
    idade = hoje - nascimento
    return idade

dicionario = {}

parada = "C"

while parada == "C":
    nome = input("Digite o nome: ")
    ano_nascimento = int(input("Digite o ano de nascimento: "))
    idade = calcuradora_idade(ano_nascimento)
    contratacao = " "
    CTPS = input("Digite o CTPS (Aperte 0 caso não tenha trabalhos antecedentes): ")
    if CTPS != "0":
        contratacao = int(input("Digite o ano da última contratação: "))
        salario = float(input("Digite o último salário: "))
        aposentadoria = idade + (35 - (datetime.datetime.now().year - contratacao))
        dicionario[nome] = [idade, aposentadoria, salario, contratacao]
    else:
        contratacao = ()
        dicionario[nome] = [idade, aposentadoria]

dicionario = dict(lista)
print(lista)
print(dicionario)

if parada == "S":
    print()
    for i , j in dicionario.items():
        print('O candidato', i, "tem", j[0], "anos e vai se aposentar com", j[1], 'anos.')







