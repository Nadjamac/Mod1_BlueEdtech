#Função Gasto com hospedagem
def custo_hotel(noites):
    custoh = 140 * noites
    return custoh

#Função Gasto com avião
def custo_aviao(cidade):
    custoav = 0 
    if cidade == "São Paulo":
        custoav = 312
    elif cidade == "Porto Alegre":
        custoav = 447
    elif cidade == "Recife":
        custoav = 831
    elif cidade == "Manaus":
        custoav = 986
    else:
        custoav = "Não temos opções para esse destino"
    return custoav

#Função Aluguel com Carro
def custo_carro(dias):
    custocar = dias * 40
    if dias >= 7:
        custocar = (dias * 40) - 50
    elif 3 <= dias < 7:
        custocar = (dias * 40) - 20
    return custocar

#Função de custo total
def custo_total(cidade , dias):
#Se o usuário incluir uma cidade fora do escopo da questão não como calcular o valor do custo total
    if cidade == "São Paulo" or cidade == "Porto Alegre" or cidade == "Recife" or cidade == "Manaus":
        custotot = custo_hotel(dias) + custo_aviao (cidade) + custo_carro(dias)
    else:
        custotot = "Não temos opções para esse destino"
    return custotot

cidade = input("Escolha seu destino: \n")
dias = int(input("Digite a quantidade de dias da sua viagem: \n"))

#Dependendo do resultado da função custo_total(), o programa printa o preço da viagem ou que o destino é inválido
if custo_total(cidade, dias) == "Não temos opções para esse destino":
    print(custo_total(cidade , dias))
else:
    print("O custo total da viagem é:", custo_total(cidade , dias), "reais.")












