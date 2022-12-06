import pygame, sys
from pygame.locals import *

pygame.init()

w,h= 1000,600

pantalla = pygame.display.set_mode((w,h))

fps = 60
reloj = pygame.time.Clock()

pygame.display.set_caption("Exterminator")

icono = pygame.image.load("imagenes/gunner.png")
fondo = pygame.image.load("imagenes/ciudad.png").convert()
x=0

pygame.display.set_icon(icono)

while True:
    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        sys.exit()
    x_relativa= x % fondo.get_rect().width
    pantalla.blit(fondo, (x_relativa - fondo.get_rect().width ,0))
    if x_relativa < w:
      pantalla.blit(fondo,(x_relativa,0))
    x-=1
    pygame.display.update()
    reloj.tick(fps
    
    )
    