def calcSalario(salario_h, horas):
    if horas > 40:
        salario_h = salario_h*1.5
    salario = salario_h*horas
    return salario

salario_h = float(input("Digite o salário do colaborador: "))
horas = int(input("Digite as horas trabalhadas pelo colaborador: "))

print("O salário do colaborador é:", calcSalario(salario_h , horas), "reais.")

