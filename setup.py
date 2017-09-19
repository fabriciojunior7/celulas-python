import pygame
from Bacteria import *
from Planta import *

global larguraTela, alturaTela, frameRate, relogio
larguraTela = 900
alturaTela = 600
frameRate = 60
relogio = pygame.time.Clock()

pygame.init()
tela = pygame.display.set_mode((larguraTela, alturaTela))
pygame.display.set_caption("Junior Teste")

numBacterias = 3
numPlantas = 2

global bacterias, plantas
bacterias = []
plantas = []

for p in range(numPlantas):
	plantas.append(Planta(larguraTela, alturaTela))

for b in range(numBacterias):
	bacterias.append(Bacteria(larguraTela, alturaTela, plantas))