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

consolas = pygame.font.match_font('consolas')
times = pygame.font.match_font('times')
arial  = pygame.font.match_font('arial')
courier = pygame.font.match_font('courier')

pygame.mixer.init()
pygame.mixer.Sound('sonido/laser.wav')
laser = pygame.mixer.Sound('sonido/laser.wav')

explosiones_random =[pygame.mixer.Sound('sonido/explosion1.wav'),
                                     pygame.mixer.Sound('sonido/explosion2.wav'),
                                     pygame.mixer.Sound('sonido/explosion3.wav'),
                                     pygame.mixer.Sound('sonido/explosion4.wav')]

ambiente = pygame.mixer.Sound('sonido/space_ambient.ogg')

ambiente.play()

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
    bala = Disparos(self.rect.centerx, self.rect.top +20)
    balas.add(bala)
    laser.play()
  '''def disparo2(self):
    bala = Disparos(self.rect.centerx + 23, self.rect.top + 30)
    balas.add(bala)
  def disparo3(self):
    bala = Disparos(self.rect.centerx - 23, self.rect.top + 30)
    balas.add(bala)'''

class EnemigosAmarillos(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.image = pygame.image.load("imagenes/enemigo1.png").convert()
    
    self.rect = self.image.get_rect()
    self.image.set_colorkey(negro)
    self.radius = 48
    self.rect.x = random.randrange(ancho - self.rect.width)
    self.rect.y = random.randrange(alto - self.rect.height)
    self.velocidad_x = random.randrange(1,3)
    self.velocidad_y = random.randrange(1,3)

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

class EnemigosVerdes(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.image = pygame.image.load("imagenes/enemigo2.png").convert()
    
    self.rect = self.image.get_rect()
    self.image.set_colorkey(negro)
    self.radius = 48
    self.rect.x = random.randrange(ancho - self.rect.width)
    self.rect.y = random.randrange(alto - self.rect.height)
    self.velocidad_x = random.randrange(3,5)
    self.velocidad_y = random.randrange(3,5)

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

class EnemigosAzules(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.image = pygame.image.load("imagenes/enemigo3.png").convert()
    
    self.rect = self.image.get_rect()
    self.image.set_colorkey(negro)
    self.radius = 48
    self.rect.x = random.randrange(ancho - self.rect.width)
    self.rect.y = random.randrange(alto - self.rect.height)
    self.velocidad_x = random.randrange(5,10)
    self.velocidad_y = random.randrange(5,10)

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

class EnemigosRojos(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.image = pygame.image.load("imagenes/enemigo4.png").convert()
    
    self.rect = self.image.get_rect()
    self.image.set_colorkey(negro)
    self.radius = 48
    self.rect.x = random.randrange(ancho - self.rect.width)
    self.rect.y = random.randrange(alto - self.rect.height)
    self.velocidad_x = random.randrange(10,15)
    self.velocidad_y = random.randrange(10,15)

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

puntuacion = 0

def muestra_texto(pantalla, fuente, texto, color, dimensiones, x, y):
  tipo_letra = pygame.font.Font(fuente, dimensiones)
  superficie = tipo_letra.render(texto, True, color)
  rectangulo = superficie.get_rect()
  rectangulo.center = (x, y)
  pantalla.blit(superficie, rectangulo)



pygame.display.set_caption("Trabajando con sprites")
clock = pygame.time.Clock()

sprites =pygame.sprite.Group()
enemigos_amarillos=pygame.sprite.Group()
enemigos_verdes=pygame.sprite.Group()
enemigos_azules=pygame.sprite.Group()
enemigos_rojos=pygame.sprite.Group()
balas = pygame.sprite.Group()
meteoritos = pygame.sprite.Group()


jugador = Jugador()
sprites.add(jugador)

'''for x in range (10):
  meteorito = Meteoritos()
  meteoritos.add(meteorito)'''

ejecutando = True

while ejecutando:
  clock.tick(fps)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      ejecutando = False

  sprites.update()
  enemigos_amarillos.update()
  enemigos_azules.update()
  enemigos_verdes.update()
  enemigos_rojos.update()
  balas.update()
  meteoritos.update()

  colision_disparos_amarillos = pygame.sprite.groupcollide(enemigos_amarillos, balas, True, True, pygame.sprite.collide_circle)
  colision_disparos_verdes = pygame.sprite.groupcollide(enemigos_verdes, balas, True, True, pygame.sprite.collide_circle)
  colision_disparos_azules = pygame.sprite.groupcollide(enemigos_azules, balas, True, True, pygame.sprite.collide_circle)
  colision_disparos_rojos= pygame.sprite.groupcollide(enemigos_rojos, balas, True, True, pygame.sprite.collide_circle)

  if colision_disparos_amarillos:
    puntuacion += 10
    explosiones_random[random.randrange(0,3)].play()

  if colision_disparos_verdes:
    puntuacion += 25
    explosiones_random[random.randrange(0,3)].play()

  if colision_disparos_azules:
    puntuacion += 50
    explosiones_random[random.randrange(0,3)].play()

  if colision_disparos_rojos:
    puntuacion += 100
    explosiones_random[random.randrange(0,3)].play()

  if not enemigos_amarillos and not enemigos_verdes and not enemigos_azules and not enemigos_rojos:
    enemigo1 = EnemigosAmarillos()
    enemigos_amarillos.add(enemigo1)

    enemigo2 = EnemigosVerdes()
    enemigos_verdes.add(enemigo2)

    enemigo3 = EnemigosAzules()
    enemigos_azules.add(enemigo3)

    enemigo4 = EnemigosRojos()
    enemigos_rojos.add(enemigo4)

  
  pantalla.fill(negro)
  sprites.draw(pantalla)
  enemigos_amarillos.draw(pantalla)
  enemigos_verdes.draw(pantalla)
  enemigos_azules.draw(pantalla)
  enemigos_rojos.draw(pantalla)
  balas.draw(pantalla)
  meteoritos.draw(pantalla)
  muestra_texto(pantalla, consolas, str(puntuacion).zfill(7), rojo, 40,700, 50)
  pygame.display.flip()
  


pygame.quit()
