import pygame, sys
from pygame.locals import *

pygame.init()

w,h= 1000,600

pantalla = pygame.display.set_mode((w,h))

pygame.display.set_caption("Exterminator")

icono = pygame.image.load("imagenes/gunner.png")
fondo = pygame.image.load("imagenes/ciudad.png")

pygame.display.set_icon(icono)
quieto = pygame.image.load('imagenes/idle1.png')

caminaDerecha =[pygame.image.load('imagenes/run1.png'),
                             pygame.image.load('imagenes/run2.png'),
                             pygame.image.load('imagenes/run3.png'),
                             pygame.image.load('imagenes/run4.png'),
                             pygame.image.load('imagenes/run5.png'),
                             pygame.image.load('imagenes/run6.png') ]

caminaIzquierda = [pygame.image.load('imagenes/run1-izq.png'),
                                pygame.image.load('imagenes/run2-izq.png'),
                                pygame.image.load('imagenes/run3-izq.png'),
                                pygame.image.load('imagenes/run4-izq.png'),
                                pygame.image.load('imagenes/run5-izq.png'),
                                pygame.image.load('imagenes/run6-izq.png') ]

salta =[pygame.image.load('imagenes/jump1.png'),
            pygame.image.load('imagenes/jump2.png') ]
x = 0
px =50
py= 200
ancho = 40
velocidad = 10
reloj = pygame.time.Clock()
salto = False
cuentaSalto = 10
izquierda = False
derecha = False
cuentaPasos = 0

def recargaPantalla():
    global cuentaPasos
    global x

    x_relativa = x % fondo.get_rect().width
    pantalla.blit(fondo, (x_relativa - fondo.get_rect().width, 0))
    if x_relativa < w:
      pantalla.blit(fondo, (x_relativa, 0))
    x -= 5

    if cuentaPasos + 1 >= 6:
      cuentaPasos = 0
    
    if izquierda:
      pantalla.blit(caminaIzquierda[cuentaPasos // 1], (int(px), int(py)))
      cuentaPasos += 1

    elif derecha:
      pantalla.blit(caminaDerecha[cuentaPasos // 1], (int(px), int(py)))
      cuentaPasos += 1

    else:
      pantalla.blit(quieto, (int(px), int(py)))

    pygame.display.update()

ejecuta = True



while ejecuta:
    reloj.tick(18)

    for event in pygame.event.get():
      if event.type == QUIT:
        ejecuta = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and px > velocidad:
      px -= velocidad
      izquierda = True
      derecha = False

    elif keys[pygame.K_d] and px < 900 - velocidad - ancho:
      px += velocidad
      izquierda = False
      derecha = True

    else:
      izquierda = False
      derecha = False
      cuentaPasos = 0

    if keys[pygame.K_w] and py >100:
      py -= velocidad

    if keys[pygame.K_s] and py <300:
      py += velocidad

    if not (salto):
      if keys [pygame.K_SPACE]:
        salto = True
        izquierda = False
        derecha = False
        cuentaPasos = 0
      
    else:
      if cuentaSalto >= -10:
        py -= (cuentaSalto * abs(cuentaSalto)) * 0.5
        cuentaSalto -= 1
      else:
        cuentaSalto = 10
        salto = False
    
    recargaPantalla()

pygame.quit()
