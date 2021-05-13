import time
from datetime import date

def voto(nascimento):
    atual = date.today().year
    idade = atual - nascimento
    voto = "Obrigatório"
    if idade < 16:
        voto = "Negado"
    elif 16 <= idade < 18 and idade > 65:
        voto = "Opcional" 
    return voto

eleitor = int(input("Qual seu ano de nascimento?: "))

situacao = voto(eleitor)

print(f"Voto {situacao}")

