import pygame as pg
BLACK = (0,0,0)
 
class Jogador(pg.sprite.Sprite):
    #Esta é a classe jogador
 
    def __init__(self, color, width, height):
        # Chama a sprite
        super().__init__()
 
        # Passa a cor, altura e largura do jogador
        self.image = pg.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
 
        # Desenha o jogador
        pg.draw.rect(self.image, color, [0, 0, width, height])
 
        self.rect = self.image.get_rect()
 
    
    def irEsquerda(self, pixels):
        self.rect.x -= pixels
	    #Verifica se foi muito para a esquerda
        if self.rect.x < 0:
          self.rect.x = 0
 
    def irDireita(self, pixels):
        self.rect.x += pixels
        #verifica se foi muito para a direita
        if self.rect.x > 700:
          self.rect.x = 700