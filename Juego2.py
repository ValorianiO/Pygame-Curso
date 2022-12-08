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
    self.radius = 22
    self.rect.center = (400,600)
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
    self.radius = 48
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

class  Meteoritos(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.img_aleatoria = random.randrange(3)
    if self.img_aleatoria == 0:
      self.image = pygame.transform.scale(pygame.image.load("imagenes/meteorito.png").convert(), (100,100))
      self.radius = 50
    if self.img_aleatoria == 1:
      self.image = pygame.transform.scale(pygame.image.load("imagenes/meteorito.png").convert(), (50,50))
      self.radius = 25
    if self.img_aleatoria == 2:
      self.image = pygame.transform.scale(pygame.image.load("imagenes/meteorito.png").convert(), (25,25))
      self.radius = 12
    self.image.set_colorkey(negro)
    self.rect = self. image.get_rect()
    self.rect.x = random.randrange(ancho - self.rect.width)
    self.rect.y = -self.rect.width
    self.velocidad_y = random.randrange(1,10)

  def update(self):
    self.rect.y += self.velocidad_y
    if self.rect.top > alto:
      self.rect.x = random.randrange(ancho - self.rect.width)
      self.rect.y = -self.rect.width
      self.velocidad_y = random.randrange(1,10)



pygame.init()
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Trabajando con sprites")
clock = pygame.time.Clock()

sprites =pygame.sprite.Group()
enemigos =pygame.sprite.Group()
balas = pygame.sprite.Group()
meteoritos = pygame.sprite.Group()


enemigo = Enemigos()
enemigos.add(enemigo)



jugador = Jugador()
sprites.add(jugador)

for x in range (10):
  meteorito = Meteoritos()
  meteoritos.add(meteorito)

ejecutando = True

while ejecutando:
  clock.tick(fps)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      ejecutando = False

  sprites.update()
  enemigos.update()
  balas.update()
  meteoritos.update()

  colision_nave = pygame.sprite.spritecollide(jugador, meteoritos, False, pygame.sprite.collide_circle)
  colision_disparos = pygame.sprite.groupcollide(meteoritos, balas, False, False)

  if colision_nave or colision_disparos:
    enemigo.image = pygame.image.load("imagenes/explosion.png")
    enemigo.velocidad_y += 20
  elif enemigo.rect.top > alto:
    enemigo.kill()


  pantalla.fill(negro)
  sprites.draw(pantalla)
  enemigos.draw(pantalla)
  balas.draw(pantalla)
  meteoritos.draw(pantalla)
  pygame.display.flip()
  

pygame.quit()
