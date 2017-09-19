import pygame
import cores

class Entidade(object):
	def __init__(self, x, y, largura, altura):
	#Atributos
		self.x = x
		self.y = y
		self.largura = largura
		self.altura = altura
		self.cor = cores.branco
		self.corpo = pygame.Rect(self.x, self.y, self.largura, self.altura)

	#Metodos
	def desenhar(self, tela):
		self.corpo = pygame.Rect(self.x, self.y, self.largura, self.altura)
		pygame.draw.ellipse(tela, self.cor, self.corpo)

	def seguirMouse(self, mousePosicao):
		self.x = mousePosicao[0] - self.largura/2.0
		self.y = mousePosicao[1] - self.altura/2.0

