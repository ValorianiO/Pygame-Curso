import pygame, sys
from pygame.locals import *

pygame.init()

pantalla = pygame.display.set_mode((500,400))

blanco = (255,255,255)
negro = (14,14,14)
rojo = (215,12,12)
azul = (0,0,190)
verde = (0,255,0)
 
c74225 = (199,66,37)
cd9135 = (97,205,53)

pantalla.fill(blanco)

pygame.display.set_caption("Mi primer juego :P")

rectangulo1= pygame.draw.rect(pantalla, rojo, (100, 50, 100, 50))
print(rectangulo1)

pygame.draw.line(pantalla, verde, (100,104), (199,104), 10)

pygame.draw.circle(pantalla, negro, (122,250),20,0)

pygame.draw.ellipse(pantalla, c74225, (275, 200, 40 ,80))

puntos = [(100,300), (100,100)]

pygame.draw.polygon(pantalla, (0,150,255), puntos, 8)
while True:
    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        sys.exit()
    pygame.display.update()
