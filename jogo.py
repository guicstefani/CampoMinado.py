import pygame # é preciso baixar o pygame no cmd
import os # precisamos para colocar as imagens da nossa pasta no jogo
from time import sleep

class Jogo():
	def __init__(self, tabuleiro, telaTamanho):
		self.tabuleiro  = tabuleiro
		self.telaTamanho = telaTamanho
		self.blocoTamanho = self.telaTamanho[0] // self.tabuleiro.getTamanho()[1], self.telaTamanho[1] // self.tabuleiro.getTamanho()[0]
		self.abrirImagens()

	def iniciar(self):
		pygame.init()
		self.tela = pygame.display.set_mode(self.telaTamanho)
		rodando = True
		while rodando:
			for event in pygame.event.get():
				if (event.type == pygame.QUIT):
					rodando = False
				if (event.type == pygame.MOUSEBUTTONDOWN):
					posicao = pygame.mouse.get_pos()
					botaoDireito = pygame.mouse.get_pressed()[2]
					self.Clicado(posicao, botaoDireito)
			self.desenhar()
			pygame.display.flip()
			if (self.tabuleiro.getGanhou()):
				musicaVitoria = pygame.mixer.Sound("som-vitoria.wav")
				musicaVitoria.play()
				sleep(3)
				rodando = False
		pygame.quit()

	def desenhar(self):
		topoEsquerdo = (0,0)
		for fileira in range(self.tabuleiro.getTamanho()[0]):
			for coluna in range(self.tabuleiro.getTamanho()[1]):
				bloco = self.tabuleiro.getBloco((fileira, coluna))
				imagem = self.getImagem(bloco)
				self.tela.blit(imagem, topoEsquerdo)
				topoEsquerdo = topoEsquerdo[0] + self.blocoTamanho[0], topoEsquerdo[1] 
			topoEsquerdo = 0, topoEsquerdo[1] + self.blocoTamanho[1]

	def abrirImagens(self):
		self.imagens = {}
		for nomePasta in os.listdir("Imagens"):
			if (not nomePasta.endswith(".png")):
				continue
			imagem = pygame.image.load(r"Imagens/" + nomePasta)
			imagem = pygame.transform.scale (imagem, self.blocoTamanho)
			self.imagens[nomePasta.split(".")[0]] = imagem

	def getImagem(self, bloco):
		string = None
		if(bloco.getClicou()):
			string = "bomba-exprudiu" if bloco.getTemBomba() else str(bloco.getBombasAoRedor())
		else:
			string = "bandeira" if bloco.getBandeira() else "bloco-vazio"
		return self.imagens[string]

	def Clicado(self, posicao, botaoDireito):
		if (self.tabuleiro.getPerdeu()):
			return
		indice = posicao[1] // self.blocoTamanho[1], posicao[0] // self.blocoTamanho[0]
		bloco = self.tabuleiro.getBloco(indice)
		self.tabuleiro.Clicado(bloco, botaoDireito)
	
	


