import pygame
from setup import *

def processamentos(frameCount):

	for b in bacterias:
		if(b.corpo.colliderect(b.plantaTarget.corpo) and len(bacterias) < 2000):
			bacterias.append(b.reproduzir(plantas))
			print(len(bacterias))

		if(frameCount % 60 == 0):
			b.viver()
			if(b.tempoVida > b.tempoVidaMaximo):
				bacterias.remove(b)

		b.mover(plantas)