def data_escrita(data):  
#Dividindo a string para analisar mês, dia e ano
    dia = int(data[:2])
    mes = data[3:5]
    ano = int(data[6:])
#Caso a pessoa coloque um mês acima de 13
    if mes > "12" or mes == "00":
        print("Data Inválida!")
#Teste para os dias dos meses. Alguns tem que ter até 31 dias, outros até 30
    if mes == "01":
        if dia > 31:
            print ("Data Inválida!")
        else:
            print (f"{dia} de Janeiro de {ano}.")
    elif mes == "03":
        if dia > 31:
            print ("Data Inválida!")
        else:
            print (f"{dia} de Março de {ano}.")
    elif mes == "05":
        if dia > 31:
            print ("Data Inválida!")
        else:
            print (f"{dia} de Maio de {ano}.")
    elif mes == "07":
        if dia > 31:
            print ("Data Inválida!")
        else:
            print (f"{dia} de Julho de {ano}.")
    elif mes == "08":
        if dia > 31:
            print ("Data Inválida!")
        else:
            print (f"{dia} de Agosto de {ano}.")
    elif mes == "10":
        if dia > 31:
            print ("Data Inválida!")
        else:
            print (f"{dia} de Dezembro de {ano}.")
    elif mes == "12":
        if dia > 31:
            print ("Data Inválida!")
        else:
            print (f"{dia} de Janeiro de {ano}.")
    elif mes == "04":
        if dia > 30:
                print("Data Inválida!")
        else:
            print (f"{dia} de Abril de {ano}.")
    elif mes == "06":
        if dia > 30:
                print("Data Inválida!")
        else:
                print (f"{dia} de Junho de {ano}.")
    elif mes == "09":
        if dia > 30:
                print("Data Inválida!")
        else:
                print (f"{dia} de Setembro de {ano}.")
    elif mes == "11":
        if dia > 30:
                print("Data Inválida!")
        else:
                print (f"{dia} de Novembro de {ano}.")
#O mês de Fevereiro é especial pq depende se o ano é bissexto ou não.
#O ano é bissexto quando é divisivel por 4 ou 400 mas não divisivel por 100
    elif mes == "02": 
        if (ano % 4 == 0 or ano % 100 != 0) or ano % 400 == 0:
            if dia > 29:
                print("Data Inválida!")
            else:
                print (f"{dia} de Fevereiro de {ano}.")
        else:
            if dia > 28:
                print("Data Inválida!")
            else:
                print (f"{dia} de Fevereiro de {ano}.")
            
  
data = input("Digite uma data (Formato DD/MM/AAA): ")

data_escrita(data)