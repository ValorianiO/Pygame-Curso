import pygame

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
    self.rect.center = (ancho//2, alto//2)
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


pygame.init()
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Trabajando con sprites")
clock = pygame.time.Clock()

sprites =pygame.sprite.Group()
jugador = Jugador()
sprites.add(jugador)

ejecutando = True

while ejecutando:
  clock.tick(fps)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      ejecutando = False

  sprites.update()

  pantalla.fill(negro)
  sprites.draw(pantalla)
  pygame.draw.line(pantalla, h_50d2fe, (400,0), (400,800), 1)
  pygame.draw.line(pantalla, azul, (0, 300), (800, 300), 1)
  pygame.display.flip()

pygame.quit()
