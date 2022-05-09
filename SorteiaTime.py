import random
import PySimpleGUI

listaJogadores = []
listaTime = []

resposta = ""
while resposta != "N" and resposta!="n":
    jogadores = input("Digite o nome do jogador: ")
    listaJogadores.append(jogadores)
    resposta = input("Deseja adicionar mais jogadores? [N]ão / [S]im ?")
#laço add jogadores na lista jogadores
for i in range(len(listaJogadores)):
    print(listaJogadores[i])
    listaTime = listaJogadores
#shuffle embaralha
print('Essa é a lista de jogadores{}'.format(listaJogadores))
listaTime = random.shuffle(listaJogadores)

print('Essa é a lista do Time sorteado{}'.format(listaJogadores))
#lista do time que recebeu os jogadores da lista jogadores
listaTime = len(listaJogadores)
for i in range(0, listaTime, 5):
    print('Time 5 e 5:{}'.format(listaJogadores[i:i+5]))
