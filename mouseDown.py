import pygame
from setup import *

def mouseDown(botoesMouse):
	#print(botoesMouse)
	if(botoesMouse[0] == True):
		plantas.append(Planta(larguraTela, alturaTela, pygame.mouse.get_pos()))

	if(botoesMouse[2] == True):
		bacterias.append(Bacteria(larguraTela, alturaTela, pygame.mouse.get_pos(),plantas))
	