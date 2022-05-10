import random
import PySimpleGUI

listaJogadores = []
listaTime = []

resposta = ""
while resposta != "N":  # and resposta != "n"#:não é necessário o ''AND" pois passou o upper
    jogadores = input("\nDigite o nome do jogador: ")
    listaJogadores.append(jogadores)

    # upper deixa tudo maiusculo
    resposta = input("\nDeseja adicionar mais jogadores [N] / [S] ?").upper()

# laço add na lista jogadores
for i in range(len(listaJogadores)):
    print(listaJogadores[i])
    listaTime = listaJogadores
# random dos nomes
print('\nEssa é a lista de jogadores{}'.format(listaJogadores))
listaTime = random.shuffle(listaJogadores)

print('\nEssa é a lista sorteada{}'.format(listaJogadores))

# Divide o time de 5 em 5
listaTime = len(listaJogadores)
for i in range(0, listaTime, 5):
    print('\nTime de 5 em 5:{}'.format(listaJogadores[i:i+5]))
