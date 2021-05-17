numero_materias = int(input("Digite o número de matérias: "))

notas = []

for materia in range(numero_materias):
    nota = float(input("Digite as notas dx alunx: ").replace("," , "."))
    notas.append(nota)

print(notas)

media_geral = sum(notas)/numero_materias

print("A média dx alunx é:", round(media_geral , 2))



