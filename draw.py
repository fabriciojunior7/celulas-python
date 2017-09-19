import pygame, sys
from setup import *
from eventos import *
from render import *

def draw(frameCount):

	pygame.display.set_caption("Junior Teste - %.1f" % relogio.get_fps())

	for event in pygame.event.get():
		eventos(event)

	processamentos(frameCount)
	render()