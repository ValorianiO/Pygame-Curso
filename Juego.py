import pygame, sys
from pygame.locals import *

pygame.init()

pantalla = pygame.display.set_mode((500,400))
pygame.display.set_caption("Mi primer juego :P")

while True:
    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        sys.exit()
