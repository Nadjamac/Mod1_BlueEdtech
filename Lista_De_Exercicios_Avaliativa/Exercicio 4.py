data = input("Digite uma data (dd/mm/aaaa): ")

dia = int(data[:2])
mes= int(data[3:5])
ano = int(data[6:])

if mes == 1:
    if dia > 31:
        print("NULL")
    else:
        print(f"{dia} de Janeiro de {ano} ")
elif mes == 3:
    if dia > 31:
        print("NULL")
    else:
        print(f"{dia} de Março de {ano} ")
elif mes == 5:
    if dia > 31:
        print("NULL!")
    else:
        print(f"{dia} de Maio de {ano} ")
elif mes == 7:
    if dia > 31:
        print("NULL!")
    else:
        print(f"{dia} de Julho de {ano} ")
elif mes == 8:
    if dia > 31:
        print("NULL!")
    else:
        print(f"{dia} de Agosto de {ano} ")
elif mes == 10:
    if dia > 31:
        print("NULL!")
    else:
        print(f"{dia} de Outubro de {ano} ")
elif mes == 12:
    if dia > 31:
        print("NULL!")
    else:
        print(f"{dia} de Dezembro de {ano} ")
elif mes == 4:
    if dia > 30:
        print("NULL!")
    else:
        print(f"{dia} de Abril de {ano} ")
elif mes == 6:
    if dia > 30:
        print("NULL!")
    else:
        print(f"{dia} de Junho de {ano} ")
elif mes == 9:
    if dia > 30:
        print("NULL!")
    else:
        print(f"{dia} de Setembro de {ano} ")
elif mes == 11:
    if dia > 30:
        print("NULL!")
    else:
        print(f"{dia} de Novembro de {ano} ")
elif mes == 2: 
    if (ano % 4 == 0 or ano % 100 != 0) or ano % 400 == 0:
        if dia > 29:
            print("NULL!")
        else:
            print (f"{dia} de Fevereiro de {ano}.")
    else:
        if dia > 28:
            print("NULL!")
        else:
            print (f"{dia} de Fevereiro de {ano}.")

