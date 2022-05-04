from jogo import Jogo
from tabuleiro import Tabuleiro
tamanho = (9,9)
probabilidade = 0.1
tabuleiro = Tabuleiro(tamanho, probabilidade)
tamanhoTela = (500, 500) 
jogo = Jogo(tabuleiro, tamanhoTela)
jogo.iniciar()
