import pygame as pg
ROSA_ESCURO = (242,167,187) #coração

class Jogador(pg.sprite.Sprite):
    #essa classe é o jogador

    def __init__(self, color, width, height):
        #chama a sprite

        super().__init__()

        #passa a cor, altura e largura do contensor (jogador)
        #muda o fundo 
        self.image = pg.Surface([width, height])
        self.image.fill(ROSA_ESCURO)
        self.image.set_colorkey(ROSA_ESCURO)

        #desenha a contenção (jogador)
        pg.draw.rect(self.image, color, [0,0,width,height])

        #imagem
        self.rect = self.image.get_rect()

    def irEsquerda(self, pixels): #self = objeto atual, pixels = n° de pixels
        self.rect.x -= pixels
        #confere se o jogador está indo muito para a esquerda
        if self.rect.x < 0:
            self.rect.x = 0
    
    def irDireita(self, pixels): #self = objeto atual, pixels = n° de pixels
        self.rect.x += pixels
        #confere se o jogador está indo muito para a direita
        if self.rect.x > 700:
            self.rect.x = 700