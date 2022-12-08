import pygame
import random

ancho = 800
alto = 600

fps = 30


blanco = (255,255,255)
negro = (0,0,0)
rojo = (255,0,0)
azul = (0,0,255)
azul2 = (64,64,255)
verde = (0,255,0)
 
h_fa2f2f= (250,47,47,)
h_50d2fe= (94,210,254)

class Jugador(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.image = pygame.image.load("imagenes/nave.png").convert()
    
    self.image.set_colorkey(azul2)

    self.rect = self.image.get_rect()
    self.rect.center = (200,200)
    self.velocidad_x = 0 
    self.velocidad_y = 0

  def update(self):

    self.velocidad_x = 0 
    self.velocidad_y = 0

    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_a]:
      self.velocidad_x = -10
    if teclas[pygame.K_d]:
       self.velocidad_x = 10
    if teclas[pygame.K_w]:
      self.velocidad_y = -10
    if teclas[pygame.K_s]:
       self.velocidad_y = 10
    if teclas[pygame.K_SPACE]:
       jugador.disparo()
       jugador.disparo2()
       jugador.disparo3()

    self.rect.x += self.velocidad_x
    self.rect.y += self.velocidad_y
  
    if self.rect.left < 0:
      self.rect.left = 0
    if self.rect.right > ancho:
      self.rect.right= ancho
    
    if self.rect.bottom > alto:
      self.rect.bottom = alto
    
    if self.rect.top < 0:
      self.rect.top = 0
          
  def disparo(self):
    bala = Disparos(self.rect.centerx, self.rect.top)
    balas.add(bala)
  def disparo2(self):
    bala = Disparos(self.rect.centerx + 23, self.rect.top + 30)
    balas.add(bala)
  def disparo3(self):
    bala = Disparos(self.rect.centerx - 23, self.rect.top + 30)
    balas.add(bala)

class Enemigos(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.image = pygame.image.load("imagenes/enemigo.png").convert()
    
    self.rect = self.image.get_rect()
    self.image.set_colorkey(negro)
    self.rect.x = random.randrange(ancho - self.rect.width)
    self.rect.y = random.randrange(alto - self.rect.height)
    self.velocidad_x = random.randrange(1,10)
    self.velocidad_y = random.randrange(1,10)

  def  update(self):
    self.rect.x += self.velocidad_x
    self.rect.y += self.velocidad_y
    if self.rect.left < 0:
      self.velocidad_x += 1
    if self.rect.right > ancho:
      self.velocidad_x -= 1
    
    if self.rect.bottom > alto:
      self.velocidad_y -= 1
    
    if self.rect.top < 0:
      self.velocidad_y += 1

class Disparos(pygame.sprite.Sprite):
  def __init__(self, x, y):
    super().__init__()
    self.image = pygame.transform.scale(pygame.image.load("imagenes/disparo.png").convert(),(10,20))
    self.image.set_colorkey(negro)
    self.rect = self.image.get_rect()
    self.rect.bottom = y
    self.rect.centerx = x
  def update(self):
    self.rect.y -= 25
    if self.rect.bottom < 0:
      self.kill()


pygame.init()
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Trabajando con sprites")
clock = pygame.time.Clock()

sprites =pygame.sprite.Group()
enemigos =pygame.sprite.Group()
balas = pygame.sprite.Group()

enemigo = Enemigos()
enemigos.add(enemigo)



jugador = Jugador()
sprites.add(jugador)


ejecutando = True

while ejecutando:
  clock.tick(fps)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      ejecutando = False

  sprites.update()
  enemigos.update()
  balas.update()
  colision = pygame.sprite.spritecollide(jugador, enemigos, False)

  if colision:
    enemigo.image = pygame.image.load("imagenes/explosion.png")
    enemigo.velocidad_y += 20
  elif enemigo.rect.top > alto:
    enemigo.kill()


  pantalla.fill(negro)
  sprites.draw(pantalla)
  enemigos.draw(pantalla)
  balas.draw(pantalla)
  pygame.draw.line(pantalla, h_50d2fe, (400,0), (400,800), 1)
  pygame.draw.line(pantalla, azul, (0, 300), (800, 300), 1)
  pygame.display.flip()
  

pygame.quit()
