from bloco import Bloco
from random import random

class Tabuleiro():
	def __init__(self, tamanho, probabilidade):
		self.tamanho = tamanho
		self.probabilidade = probabilidade
		self.perdeu = False
		self.numCliques = 0
		self.numSemBomba = 0
		self.definirTabuleiro()


	def definirTabuleiro(self):
		self.tabuleiro = []
		for fileira in range(self.tamanho[0]):
			fileira = []
			for coluna in range(self.tamanho[1]):
				temBomba = random() < self.probabilidade
				if (not temBomba):
					self.numSemBomba += 1
				bloco = Bloco(temBomba)
				fileira.append(bloco)
			self.tabuleiro.append(fileira)
		self.definirVizinhos()

	def definirVizinhos(self):
		for fileira in range(self.tamanho[0]):
			for coluna in range(self.tamanho[1]):
				bloco = self.getBloco((fileira,coluna))
				vizinhos = self.getListaDeVizinhos((fileira, coluna))
				bloco.definirVizinhos(vizinhos)

	def getListaDeVizinhos(self, indice):
		vizinhos = []
		for fileira in range(indice [0] - 1, indice [0] + 2):
			for coluna in range(indice [1] - 1, indice [1] + 2):
				foraDosLimites = fileira < 0 or fileira >= self.tamanho[0] or coluna < 0 or coluna >= self.tamanho[1]
				igual = fileira == indice[0] and coluna == indice [1]
				if (igual or foraDosLimites):
					continue
				vizinhos.append(self.getBloco((fileira, coluna)))
		return vizinhos

	def getTamanho(self):
		return self.tamanho

	def getBloco(self, indice):
		return self.tabuleiro[indice[0]][indice[1]]

	def Clicado(self, bloco, bandeira):
		if (bloco.getClicou() or (bloco.getBandeira() and not bandeira)):
			return
		if (bandeira):
			bloco.selecionarBandeira()
			return
		bloco.clique()
		if(bloco.getTemBomba()):
			self.perdeu = True
			return
		self.numCliques += 1
		if (bloco.getBombasAoRedor()!= 0):
			return
		for vizinhos in bloco.getVizinhos():
			if (not vizinhos.getTemBomba() and not vizinhos.getClicou()):
				self.Clicado(vizinhos, False)


	def getPerdeu(self):
		return self.perdeu

	def getGanhou(self):
		return self.numSemBomba == self.numCliques
	

	
