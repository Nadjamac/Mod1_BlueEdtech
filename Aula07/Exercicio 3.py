def somaImposto(taxaImposto, custo):
    novo_custo = custo + taxaImposto*custo
    return novo_custo

custo = float(input("Digite o custo do produto: "))
taxaImposto = input("Digite a taxa de imposto: ").replace("," , ".")

taxaImp = float(taxaImposto)

taxa = 0.01 * taxaImp

print("O novo preço é:", somaImposto(taxa , custo ), "reais.")