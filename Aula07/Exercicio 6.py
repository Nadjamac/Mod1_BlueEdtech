def conceito(nota):
    conceito = "F"
    if nota >= 9:
        conceito ="A"
    elif 8 <= nota < 9:
            conceito = "B"
    elif 7 <= nota < 8:
            conceito = "C"
    elif 6 <= nota < 7:
            conceito = "D"
    elif 5 <= nota < 6:
            conceito = "E"
    else:
        conceito ="F"
    return conceito


no = input("Nota do Aluno: ").replace("," , ".")
nota = float(no)

conceit = conceito(nota)

print(f"O conceito do aluno é: {conceit}.")