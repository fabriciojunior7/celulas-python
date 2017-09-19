import random
from multimethods import multimethod
import Entidade, cores

class Bacteria(Entidade.Entidade):
	#Atributos
	@multimethod(int, int, list)
	def __init__(self, larguraTela, alturaTela, plantas):
		x = random.randint(0, larguraTela)
		y = random.randint(0, alturaTela)
		largura = random.randint(5, 20)
		altura = random.randint(5, 20)
		raio = random.randint(5, 20)
		self.larguraTela = larguraTela
		self.alturaTela = alturaTela
		r = random.randint(0, len(plantas)-1)
		self.plantaTarget = plantas[r]
		self.xTarget = self.plantaTarget.x+self.plantaTarget.largura/2
		self.yTarget = self.plantaTarget.y+self.plantaTarget.altura/2
		self.energiaMaxima = random.randint(5, 50)
		self.energia = random.randint(5, self.energiaMaxima)
		self.carregando = False
		self.velocidadeX = 0.0
		self.velocidadeY = 0.0
		self.aceleracao = random.randint(1, 5)/10.0
		self.desaceleracao = 0.1
		self.velocidadeMaxima = random.randint(1, 5)*1.0
		self.r = random.randint(0, len(plantas)-1)
		self.tempoVidaMaximo = random.randint(2, 10)
		self.tempoVida = 0

		Entidade.Entidade.__init__(self, x, y, raio, raio)
		#self.cor = cores.vermelho
		self.cor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

	@multimethod(int, int, tuple, list)
	def __init__(self, larguraTela, alturaTela, mousePos, plantas):
		largura = random.randint(5, 20)
		altura = random.randint(5, 20)
		raio = random.randint(5, 20)
		x = mousePos[0]-raio/2
		y = mousePos[1]-raio/2
		self.larguraTela = larguraTela
		self.alturaTela = alturaTela
		r = random.randint(0, len(plantas)-1)
		self.plantaTarget = plantas[r]
		self.xTarget = self.plantaTarget.x+self.plantaTarget.largura/2
		self.yTarget = self.plantaTarget.y+self.plantaTarget.altura/2
		self.energiaMaxima = random.randint(5, 50)
		self.energia = random.randint(5, self.energiaMaxima)
		self.carregando = False
		self.velocidadeX = 0.0
		self.velocidadeY = 0.0
		self.aceleracao = random.randint(1, 5)/10.0
		self.desaceleracao = 0.1
		self.velocidadeMaxima = random.randint(1, 5)*1.0
		self.r = random.randint(0, len(plantas)-1)
		self.tempoVidaMaximo = random.randint(2, 10)
		self.tempoVida = 0

		Entidade.Entidade.__init__(self, x, y, raio, raio)
		#self.cor = cores.vermelho
		self.cor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

	#Metodos
	def mover(self, plantas):
		self.verificarParedes()
		self.checarDestino(plantas)
		if(self.carregando == False):
			self.andar()
			
		elif(self.carregando == True):
			self.carregar()

		if(self.energia <= 0 and self.carregando == False):
			self.switch()



	def andar(self):
		#X
		if(self.x > -50 and self.x < self.larguraTela-self.largura+50):
			if(self.x < self.xTarget):
				if(self.velocidadeX < self.velocidadeMaxima):
					self.velocidadeX += self.aceleracao
				self.x += self.velocidadeX

			elif(self.x > self.xTarget):
				if(self.velocidadeX > -self.velocidadeMaxima):
					self.velocidadeX -= self.aceleracao
				self.x += self.velocidadeX

			self.energia -= 1

		#Y
		if(self.y > -50 and self.y < self.alturaTela-self.altura+50):
			if(self.y < self.yTarget):
				if(self.velocidadeY < self.velocidadeMaxima):
					self.velocidadeY += self.aceleracao
				self.y += self.velocidadeY

			elif(self.y > self.yTarget):
				if(self.velocidadeY > -self.velocidadeMaxima):
					self.velocidadeY -= self.aceleracao
				self.y += self.velocidadeY

			self.energia -= 1



	def carregar(self):
		self.energia += 0.5
		if(self.energia >= self.energiaMaxima):
			self.carregando = False
		#X
		if(self.velocidadeX > 0):
			self.velocidadeX -= self.desaceleracao
			self.x += self.velocidadeX
		elif(self.velocidadeX < 0):
			self.velocidadeX += self.desaceleracao
			self.x += self.velocidadeX

		if(self.velocidadeX < 0.5 and self.velocidadeX > -0.5):
			self.velocidadeX = 0
		#Y
		if(self.velocidadeY > 0):
			self.velocidadeY -= self.desaceleracao
			self.y += self.velocidadeY
		elif(self.velocidadeY < 0):
			self.velocidadeY += self.desaceleracao
			self.y += self.velocidadeY

		if(self.velocidadeY < 0.5 and self.velocidadeY > -0.5):
			self.velocidadeY = 0



	def switch(self):
		self.carregando = True
		#pass


	def checarDestino(self, plantas):
		if(self.corpo.colliderect(self.plantaTarget.corpo)):
			r = self.r
			self.r = random.randint(0, len(plantas)-1)
			while(self.r == r):
				self.r = random.randint(0, len(plantas)-1)

			self.plantaTarget = plantas[r]
			self.xTarget = self.plantaTarget.x+self.plantaTarget.largura/2
			self.yTarget = self.plantaTarget.y+self.plantaTarget.altura/2

			#self.cor = cores.azul
			#self.cor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


	def verificarParedes(self):
		#X
		if(self.x < 0):
			self.x += 5
		elif(self.x > self.larguraTela-self.largura):
			self.x -= 5
		#Y
		if(self.y < 0):
			self.y += 5
		elif(self.y > self.alturaTela-self.altura):
			self.y -= 5


	def reproduzir(self, plantas):
		filha = Bacteria(self.larguraTela, self.alturaTela, (self.x, self.y), plantas)
		filha.cor = self.cor
		filha.largura = self.largura
		filha.altura = self.altura
		filha.energiaMaxima = self.energiaMaxima
		filha.velocidadeMaxima = self.velocidadeMaxima
		filha.aceleracao = self.aceleracao
		filha.r = self.r
		filha.checarDestino(plantas)
		return filha


	def viver(self):
		self.tempoVida += 1
		

