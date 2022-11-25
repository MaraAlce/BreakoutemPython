import pygame as pg
from random import randint
 
BLACK = (0, 0, 0)
 
class Bolinha(pg.sprite.Sprite):
    #Esta classe é a bolinha

    def __init__(self, color, width, height):
        super().__init__()
        
        # Definido cor, altura e largura
        self.image = pg.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
 
        # Desenha a bolinha
        pg.draw.rect(self.image, color, [0, 0, width, height])
        
        self.velocity = [randint(4,8),randint(-8,8)]
        
        self.rect = self.image.get_rect()
        
    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
          
    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8,8)