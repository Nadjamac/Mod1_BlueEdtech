situacao = " "

tupla = ()

lista_situacao = []

for n in range(1000):
    nome = input("Digite o nome dx alunx ou '0' para terminar:  ")
    if nome == "0":
        print("\nA situação dos alunos já está calculada e pronta para impressão.")
        break
    else:
        media = float(input("Digite a média dx alunx: ").replace("," , "."))
        if media >= 7:
            situacao = "Aprovado"
            tupla = (nome , situacao)
            lista_situacao.append(tupla)
        elif 5 <= media < 6.9:
            situacao = "De recuperação"
            tupla = (nome , situacao)
            lista_situacao.append(tupla)
        else:
            situacao = "Reprovado"
            tupla = (nome , situacao)
            lista_situacao.append(tupla)

print(lista_situacao)
        
        

lista_dicionario = dict(lista_situacao)

print(lista_dicionario)

for aluno, situ in lista_dicionario.items():
    print(f"A situação do aluno {aluno} é: {situ}")



