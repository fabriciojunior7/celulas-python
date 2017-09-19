import pygame
import cores
from setup import *

def render():
	#Ajustes
	pygame.display.update()
	relogio.tick(frameRate)

	#Outros
	tela.fill(cores.preto)

	for p in plantas:
		p.desenhar(tela)

	for b in bacterias:
		b.desenhar(tela)
