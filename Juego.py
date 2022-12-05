import pygame, sys
from pygame.locals import *

pygame.init()

pantalla = pygame.display.set_mode((500,400))

pygame.display.set_caption("Exterminator")

icono = pygame.image.load("imagenes/gunner.png")
fondo = pygame.image.load("imagenes/ciudad.png")

pantalla.blit(fondo, (0,0))
pygame.display.set_icon(icono)

while True:
    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        sys.exit()
    pygame.display.update()
