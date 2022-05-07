import random
import PySimpleGUI
# add nome jogadores na lista time e fatia de 5 em 5 ???

listaJogadores = []
listaTime = []

# colocar N ou n
resposta = ""
while resposta != "N":
    jogadores = input("Digite o nome do jogador: ")
    listaJogadores.append(jogadores)
    resposta = input("Deseja adicionar mais jogadores?")

for i in range(len(listaJogadores)):
    print(listaJogadores[i])
    listaTime = listaJogadores

print('Essa é a lista de jogadores{}'.format(listaJogadores))
listaTime = random.shuffle(listaJogadores)

print('Essa é a lista do Time sorteado{}'.format(listaJogadores))

listaTime = len(listaJogadores)
for i in range(0, listaTime, 5):
    print('Time 5 e 5:{}'.format(listaJogadores[i:i+5]))
