import pygame as pg
BLACK = (0,0,0)
 
class Tijolinho(pg.sprite.Sprite):
    #Esta classe é o nosso tijolinho
 
    def __init__(self, color, width, height):
        super().__init__()
 
        # Passando cor, altura e largura do tijolinho
        self.image = pg.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
 
        # Desenha o tijolinho
        pg.draw.rect(self.image, color, [0, 0, width, height])
 
        self.rect = self.image.get_rect()