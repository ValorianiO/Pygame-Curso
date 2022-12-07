import pygame

ancho = 800
alto = 600

fps = 30


blanco = (255,255,255)
negro = (0,0,0)
rojo = (255,0,0)
azul = (0,0,255)
verde = (0,255,0)
 
h_fa2f2f= (250,47,47,)
h_50d2fe= (94,210,254)

class Jugador(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.image = pygame.Surface((200, 200))
    self.image.fill(h_fa2f2f)

    self.rect = self.image.get_rect()
    self.rect.center = (ancho//2, alto//2)

  def update(self):
    self.rect.y += 10
    if self.rect.top > alto:
      self.rect.bottom = 0

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
