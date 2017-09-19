#Fabricio Vidal da Costa Junior
#Inicio: 11/09/2017
#Ultima Atualizacao: 11/09/2017
#Fim: ?

from setup import *
from draw import *

def main():

	global frameCount
	frameCount = 0

	while(True):
		frameCount += 1
		draw(frameCount)

main()