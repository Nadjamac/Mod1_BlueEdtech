cartola = dict()

gol_por_partida = []


while True:
    nome_jogador = input("Digite o nome do jogador ou 0 para terminar: ")
    if nome_jogador == "0": break
    partidas = int(input("Digite a quantidades "))
    for n in range(partidas):
       gol_por_partida.append(int(input(f"Digite a quantidade de gols marcados no jogo {n+1}: ")))
    gols = sum(gol_por_partida)
    aproveitamento = round(((gols / partidas)*100) , 2)
    cartola[nome_jogador] = [gols , aproveitamento]
    
print(cartola)

for key , values in cartola.items():
    print(f"O jogador {key} tem aproveitamento de {values[1]}%.")







