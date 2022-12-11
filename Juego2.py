import pygame
import random
import os

carpeta_juego = os.path.dirname(__file__)

carpeta_imagenes = os.path.join(carpeta_juego, "imagenes")
carpeta_imagenes_enemigos = os.path.join(carpeta_imagenes, "enemigos")
carpeta_imagenes_fondos = os.path.join(carpeta_imagenes, "fondos")
carpeta_imagenes_jugador = os.path.join(carpeta_imagenes, "jugador")

carpeta_sonidos= os.path.join(carpeta_juego, "sonidos")

carpeta_sonidos_ambiente = os.path.join(carpeta_sonidos, "ambiente")
carpeta_sonidos_armas = os.path.join(carpeta_sonidos, "armas")
carpeta_sonidos_explosiones = os.path.join(carpeta_sonidos, "explosiones")

carpeta_imagenes_explosiones = os.path.join(carpeta_imagenes, "explosiones")


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
pygame.mixer.Sound(os.path.join(carpeta_sonidos_armas,'laser.wav'))
laser = pygame.mixer.Sound(os.path.join(carpeta_sonidos_armas, 'laser.wav'))


explosiones_random =[pygame.mixer.Sound(os.path.join(carpeta_sonidos_explosiones, 'explosion1.wav')),
                                     pygame.mixer.Sound(os.path.join(carpeta_sonidos_explosiones,'explosion2.wav')),
                                     pygame.mixer.Sound(os.path.join(carpeta_sonidos_explosiones, 'explosion3.wav')),
                                     pygame.mixer.Sound(os.path.join(carpeta_sonidos_explosiones, 'explosion4.wav'))]

ambiente = pygame.mixer.Sound(os.path.join(carpeta_sonidos_ambiente, 'space_ambient.ogg'))

ambiente.play()

class Jugador(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.image = pygame.image.load(os.path.join(carpeta_imagenes_jugador, "nave.png")).convert()
    
    self.image.set_colorkey(azul2)

    self.rect = self.image.get_rect()
    self.radius = 22
    self.rect.center = (400,600)
    self.velocidad_x = 0 
    self.velocidad_y = 0
    self.retraso = 750
    self.ultimo_disparo = pygame.time.get_ticks()
    self.hp = 100
    self.vidas = 3


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
       ahora = pygame.time.get_ticks()
       if ahora - self.ultimo_disparo > self.retraso:
        self.disparo()
        self.disparo2()
        self.disparo3()
        self.ultimo_disparo = ahora
        
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
  def disparo2(self):
    bala = Disparos(self.rect.centerx + 23, self.rect.top + 30)
    balas.add(bala)
  def disparo3(self):
    bala = Disparos(self.rect.centerx - 23, self.rect.top + 30)
    balas.add(bala)

class EnemigosAmarillos(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.image = pygame.image.load(os.path.join(carpeta_imagenes_enemigos, 'enemigo1.png')).convert()
    
    self.rect = self.image.get_rect()
    self.image.set_colorkey(negro)
    self.radius = 48
    self.rect.x = random.randrange(ancho - self.rect.width)
    self.rect.y = random.randrange(alto - self.rect.height)
    self.velocidad_x = random.randrange(1,3)
    self.velocidad_y = random.randrange(1,3)
    self.hp = 15

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
    self.image = pygame.image.load(os.path.join(carpeta_imagenes_enemigos, 'enemigo2.png')).convert()
    
    self.rect = self.image.get_rect()
    self.image.set_colorkey(negro)
    self.radius = 48
    self.rect.x = random.randrange(ancho - self.rect.width)
    self.rect.y = random.randrange(alto - self.rect.height)
    self.velocidad_x = random.randrange(3,5)
    self.velocidad_y = random.randrange(3,5)
    self.hp = 30

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
    self.image = pygame.image.load(os.path.join(carpeta_imagenes_enemigos, 'enemigo3.png')).convert()
    
    self.rect = self.image.get_rect()
    self.image.set_colorkey(negro)
    self.radius = 48
    self.rect.x = random.randrange(ancho - self.rect.width)
    self.rect.y = random.randrange(alto - self.rect.height)
    self.velocidad_x = random.randrange(5,10)
    self.velocidad_y = random.randrange(5,10)
    self.hp = 45

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
    self.image = pygame.image.load(os.path.join(carpeta_imagenes_enemigos, 'enemigo4.png')).convert()
    
    self.rect = self.image.get_rect()
    self.image.set_colorkey(negro)
    self.radius = 48
    self.rect.x = random.randrange(ancho - self.rect.width)
    self.rect.y = random.randrange(alto - self.rect.height)
    self.velocidad_x = random.randrange(10,15)
    self.velocidad_y = random.randrange(10,15)
    self.hp = 75

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
    self.image = pygame.transform.scale(pygame.image.load(os.path.join(carpeta_imagenes_jugador, 'disparo.png')).convert(),(10,20))
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
      self.image = pygame.transform.scale(pygame.image.load(os.path.join(carpeta_imagenes_enemigos, 'meteorito.png')).convert(), (100,100))
      self.radius = 50
    if self.img_aleatoria == 1:
      self.image = pygame.transform.scale(pygame.image.load(os.path.join(carpeta_imagenes_enemigos, 'meteorito.png')).convert(), (50,50))
      self.radius = 25
    if self.img_aleatoria == 2:
      self.image = pygame.transform.scale(pygame.image.load(os.path.join(carpeta_imagenes_enemigos, 'meteorito.png')).convert(), (25,25))
      self.radius = 12
    self.image.set_colorkey(negro)
    self.rect = self.image.get_rect()
    self.rect.x = random.randrange(ancho - self.rect.width)
    self.rect.y = -self.rect.width
    self.velocidad_y = random.randrange(1,10)

  def update(self):
    self.rect.y += self.velocidad_y
    if self.rect.top > alto:
      self.rect.x = random.randrange(ancho - self.rect.width)
      self.rect.y = -self.rect.width
      self.velocidad_y = random.randrange(1,10)

class Explosiones(pygame.sprite.Sprite):
  def __init__(self, centro, dimensiones):
    pygame.sprite.Sprite.__init__(self)
    self.dimensiones = dimensiones
    self.image = animacion_explosion1[self.dimensiones][0]
    self.rect = self.image.get_rect()
    self.rect.center = centro
    self.fotograma = 0
    self.frecuencia_fotograma = 35
    self.actualizacion = pygame.time.get_ticks()

  def update(self):
    ahora = pygame.time.get_ticks()
    if ahora - self.actualizacion > self.frecuencia_fotograma:
      self.actualizacion = ahora
      self.fotograma += 1
      if self.fotograma == len(animacion_explosion1[self.dimensiones]):
          self.kill()
      else:
        centro = self.rect.center
        self.image = animacion_explosion1[self.dimensiones][self.fotograma]
        self.rect = self.image.get_rect()
        self.rect.center = centro





pygame.init()
pantalla = pygame.display.set_mode((ancho, alto))

puntuacion = 0

animacion_explosion1 = {'t1': [], 't2': [], 't3': [], 't4': []}

for x in range(24):
  archivo_explosiones = f'expl_01_{x:04d}.png'
  imagenes = pygame.image.load(os.path.join(carpeta_imagenes_explosiones, archivo_explosiones)).convert()
  imagenes.set_colorkey(negro)
  imagenes_t1 = pygame.transform.scale(imagenes, (32, 32))
  animacion_explosion1['t1'].append(imagenes_t1)
  imagenes_t2 = pygame.transform.scale(imagenes, (64,64))
  animacion_explosion1['t2'].append(imagenes_t2)
  imagenes_t3 = pygame.transform.scale(imagenes, (128, 128))
  animacion_explosion1['t3'].append(imagenes_t3)
  imagenes_t4 = pygame.transform.scale(imagenes, (256, 256))
  animacion_explosion1['t4'].append(imagenes_t4)


def barra_hp(pantalla, x, y, hp):
  largo = 200
  ancho = 25
  calculo_barra = int((jugador.hp/ 100) * largo)
  borde = pygame.Rect(x, y, largo, ancho)
  rectangulo = pygame.Rect(x, y, calculo_barra, ancho)
  pygame.draw.rect(pantalla, azul2, borde, 3)
  pygame.draw.rect(pantalla, h_50d2fe, rectangulo)
  


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
explosiones = pygame.sprite.Group()
meteoritos = pygame.sprite.Group()



jugador = Jugador()
sprites.add(jugador)

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
  explosiones.update()

  r = random.randrange(1, 4)
  
  if not meteoritos:
    for x in range(5):
      meteorito = Meteoritos()
      meteoritos.add(meteorito)

  colision_disparos_meteoritos = pygame.sprite.groupcollide(meteoritos, balas, True, True, pygame.sprite.collide_circle)

  if colision_disparos_meteoritos:
    puntuacion += 25

  colision_nave1 = pygame.sprite.spritecollide(jugador, enemigos_amarillos, True, pygame.sprite.collide_circle)
  if colision_nave1:
    explosiones_random[random.randrange(0,3)].play()
    explosion = Explosiones(enemigo1.rect.center, f't{r}')
    explosiones.add(explosion)
    jugador.hp -= 15
    if puntuacion >= 0:
      puntuacion -= 100
      if puntuacion < 0:
        puntuacion = 0
    else:
      puntuacion = puntuacion

  colision_nave2 = pygame.sprite.spritecollide(jugador, enemigos_verdes, True, pygame.sprite.collide_circle)
  if colision_nave2:
    explosiones_random[random.randrange(0,3)].play()
    explosion = Explosiones(enemigo2.rect.center, f't{r}')
    explosiones.add(explosion)
    jugador.hp -= 25
    if puntuacion >= 0:
      puntuacion -= 75
      if puntuacion < 0:
        puntuacion = 0
    else:
      puntuacion = puntuacion

  colision_nave3 = pygame.sprite.spritecollide(jugador, enemigos_azules, True, pygame.sprite.collide_circle)
  if colision_nave3:
    explosiones_random[random.randrange(0,3)].play()
    explosion = Explosiones(enemigo3.rect.center, f't{r}')
    explosiones.add(explosion)
    jugador.hp -= 35
    if puntuacion >= 0:
      puntuacion -= 50
      if puntuacion < 0:
        puntuacion = 0
    else:
      puntuacion = puntuacion


  colision_nave4 = pygame.sprite.spritecollide(jugador, enemigos_rojos, True, pygame.sprite.collide_circle)
  if colision_nave4:
    explosiones_random[random.randrange(0,3)].play()
    explosion = Explosiones(enemigo4.rect.center, f't{r}')
    explosiones.add(explosion)
    jugador.hp -= 50
    if puntuacion >= 0:
      puntuacion -= 25
      if puntuacion < 0:
        puntuacion = 0
    else:
      puntuacion = puntuacion

  colision_disparos_amarillos = pygame.sprite.groupcollide(enemigos_amarillos, balas, False, True, pygame.sprite.collide_circle)

  if colision_disparos_amarillos:
    puntuacion += 10
    explosiones_random[random.randrange(0,3)].play()
    explosion = Explosiones(enemigo1.rect.center, 't1')
    explosiones.add(explosion)
    enemigo1.hp -= 5
    if enemigo1.hp <= 0:
      enemigo1.kill()

  colision_disparos_verdes = pygame.sprite.groupcollide(enemigos_verdes, balas, False, True, pygame.sprite.collide_circle)

  if colision_disparos_verdes:
    puntuacion += 25
    explosiones_random[random.randrange(0,3)].play()
    explosion = Explosiones(enemigo2.rect.center, 't2')
    explosiones.add(explosion)
    enemigo2.hp -= 5
    if enemigo2.hp <= 0:
      enemigo2.kill()

  colision_disparos_azules = pygame.sprite.groupcollide(enemigos_azules, balas, False, True, pygame.sprite.collide_circle)

  if colision_disparos_azules:
    puntuacion += 50
    explosiones_random[random.randrange(0,3)].play()
    explosion = Explosiones(enemigo3.rect.center, 't3')
    explosiones.add(explosion)
    enemigo3.hp -= 5
    if enemigo3.hp <= 0:
      enemigo3.kill()

  colision_disparos_rojos= pygame.sprite.groupcollide(enemigos_rojos, balas, False, True, pygame.sprite.collide_circle)

  if colision_disparos_rojos:
    puntuacion += 100
    explosiones_random[random.randrange(0,3)].play()
    explosion = Explosiones(enemigo4.rect.center, 't4')
    explosiones.add(explosion)
    enemigo4.hp -= 5
    if enemigo4.hp <= 0:
      enemigo4.kill()
  

  warning = pygame.image.load(os.path.join(carpeta_imagenes_jugador, 'warning.png')).convert()
  muerte_3 = pantalla.blit(pygame.transform.scale(jugador.image,(25,25)), (510,15))
  muerte_2 = pantalla.blit(pygame.transform.scale(jugador.image,(25,25)), (475,15))
  muerte_1 = pantalla.blit(pygame.transform.scale(jugador.image,(25,25)), (440,15))
  cruz = pygame.image.load(os.path.join(carpeta_imagenes_jugador, 'cruz.png')).convert()

  if jugador.hp < 30:
    pantalla.blit(pygame.transform.scale(warning, (25,25)), (545, 15))

  
  if jugador.hp <= 0 and jugador.vidas == 3:
    jugador.kill()
    jugador = Jugador()
    sprites.add(jugador)
    jugador.vidas = 2
  
  if jugador.vidas == 2:
    if jugador.hp <= 0:
      jugador.kill()
      jugador = Jugador()
      sprites.add(jugador)
      jugador.vidas = 1
    muerte_1 = pantalla.blit(pygame.transform.scale(cruz, (25,25)), (510, 15))
  
  if jugador.vidas == 1:
    if jugador.hp <= 0:
      jugador.kill()
      jugador = Jugador()
      sprites.add(jugador)
      jugador.vidas = 0
    muerte_1 = pantalla.blit(pygame.transform.scale(cruz, (25,25)), (510, 15))
    muerte_2 = pantalla.blit(pygame.transform.scale(cruz, (25,25)), (475, 15))

  if jugador.vidas == 0:
    if jugador.hp <= 0:
      jugador.kill()
      jugador.hp = 0
    muerte_1 = pantalla.blit(pygame.transform.scale(cruz, (25,25)), (510, 15))
    muerte_2 = pantalla.blit(pygame.transform.scale(cruz, (25,25)), (475, 15))
    muerte_3 = pantalla.blit(pygame.transform.scale(cruz, (25,25)), (440, 15))


  colision_nave_meteoritos = pygame.sprite.spritecollide(jugador, meteoritos, pygame.sprite.collide_circle)
  if colision_nave_meteoritos:
    explosiones_random[random.randrange(0,3)].play()
    explosiones.add(explosiones)
    jugador.hp -= 15
    if puntuacion >= 0:
      puntuacion -= 10
      if puntuacion <0:
        puntuacion =0

  if jugador.hp <= 0:
    ejecutando = False

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
  explosiones.draw(pantalla)
  muestra_texto(pantalla, consolas, str(puntuacion).zfill(7), rojo, 40,680, 60)
  barra_hp(pantalla, 580, 15, jugador.hp)
  pygame.display.flip()
  


pygame.quit()
