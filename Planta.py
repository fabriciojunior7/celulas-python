import random
from multimethods import multimethod
import Entidade, cores

class Planta(Entidade.Entidade):
	#Atributos
	@multimethod(int, int)
	def __init__(self, larguraTela, alturaTela):
		largura = random.randint(20, 30)
		altura = random.randint(20, 30)
		raio = random.randint(20, 30)
		x = random.randint(0, larguraTela-raio)
		y = random.randint(0, alturaTela-raio)
		Entidade.Entidade.__init__(self, x, y, raio, raio)
		self.cor = cores.verde

	@multimethod(int, int, tuple)
	def __init__(self, larguraTela, alturaTela, mousePos):
		largura = random.randint(20, 30)
		altura = random.randint(20, 30)
		raio = random.randint(20, 30)
		x = mousePos[0]-raio/2
		y = mousePos[1]-raio/2
		Entidade.Entidade.__init__(self, x, y, raio, raio)
		self.cor = cores.verde
