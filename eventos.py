import pygame, sys
from keyDown import *
from keyUp import *
from mouseDown import *
from mouseUp import *

from processamentos import *

def eventos(event):

	if(event.type == pygame.QUIT):
		pygame.quit()
		sys.exit()

	if(event.type == pygame.KEYDOWN):
		keyDown(event.key)
	if(event.type == pygame.KEYUP):
		keyUp(event.key)

	if(event.type == pygame.MOUSEBUTTONDOWN):
		mouseDown(pygame.mouse.get_pressed())
	if(event.type == pygame.MOUSEBUTTONUP):
		mouseUp(pygame.mouse.get_pressed())