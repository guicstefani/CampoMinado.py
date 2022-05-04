class Bloco():
	def __init__(self, temBomba):
		self.temBomba = temBomba
		self.clicou = False
		self.bandeira = False

	def getTemBomba(self):
		return self.temBomba

	def getClicou(self):
		return self.clicou

	def getBandeira(self):
		return self.bandeira

	def definirVizinhos(self, vizinhos):
		self.vizinhos = vizinhos 
		self.definirBombasAoRedor()

	def definirBombasAoRedor(self):
		self.BombasAoRedor = 0
		for bloco in self.vizinhos:
			if (bloco.getTemBomba()):
				self.BombasAoRedor += 1

	def getBombasAoRedor(self):
		return self.BombasAoRedor

	def selecionarBandeira(self):
		self.bandeira = not self.bandeira

	def clique(self):
		self.clicou = True

	def getVizinhos(self):
		return self.vizinhos
