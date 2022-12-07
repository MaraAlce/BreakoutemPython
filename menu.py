import pygame
import pygame.locals
from pygame import mixer
from settings import Settings
import os
import sys

class Main:

    def __init__(self):

        pygame.init()
        mixer.init()
        self.load_screen = False
        self.size = (800,600)
        self.window = pygame.display.set_mode((self.size))
        self.fps = 60
        #inserindo a imagem
        self.back = pygame.image.load(r'data/images/mymelody.png')
        self.back = pygame.transform.scale(self.back,(330,350))
        #som de navegação 
        self.nav_mus = mixer.Sound(r"data/music/navigation.wav")
        self.played = False
        self.load_settings = False
        pygame.display.set_caption("Jogo Breakout <3")
        self.clock = pygame.time.Clock()
        self.colors = {
        "white" : (255,255,255),
        "fundoBtn" : (255,111,156),
        "black" : (0,0,0),
        "fundo" : (255,203,219),
        "ROSA_ESCURO" : (242,167,187) #coração
    
        }

        self.locations = [
            (100,340,200,410),
            (100,430,200,500),
            (100,520,200,590)            
        ]

        self.append_rect()
        self.btn_clr = [
            self.colors["ROSA_ESCURO"],
            self.colors["ROSA_ESCURO"],
            self.colors["ROSA_ESCURO"]
        ]

        self.cpy = self.btn_clr.copy()

        self.game_loop()

    def text(self,Text,color,x,y,s):
        font = pygame.font.Font(r"data\fonts\love.ttf",s)
        Txt = font.render(Text,True,self.colors[color])
        self.window.blit(Txt,(x,y))

    def append_rect(self):
        self.rects = {
        "play_Rect" : pygame.Rect(100,320,180,70),
        "settings_Rect" : pygame.Rect(100,410,180,70),
        "exit_Rect" : pygame.Rect(100,500,180,70)
        }
        self.len = len(self.rects)

    def chng_clr(self,locs,color1,color2,para = None):
        if not para:
            if self.pos_x > locs[0] and self.pos_x < locs[2]:
                if self.pos_y > locs[1] and self.pos_y < locs[3]:
                    color1 = color2
        elif para:
            if self.pos_x > 20 and self.pos_x < locs[2]:
                if self.pos_y > locs[1] and self.pos_y < locs[3]:
                    return True

    def check_mouse_pos(self):
        if self.chng_clr(self.locations[0],None,None,para=True):
            self.btn_clr[0] = (255,111,156)
            self.mus_play()

        elif self.chng_clr(self.locations[1],None,None,para=True):
            self.btn_clr[1] = (255,111,156)
            self.mus_play()

        elif self.chng_clr(self.locations[2],None,None,para=True):
            self.btn_clr[2] = (255,111,156)
            self.mus_play()

        else:
            self.btn_clr = self.cpy.copy()
            self.played = False
    def draw_rects(self):
        pygame.draw.rect(self.window,self.btn_clr[0],self.rects["play_Rect"])
        pygame.draw.rect(self.window,self.btn_clr[1],self.rects["settings_Rect"])
        pygame.draw.rect(self.window,self.btn_clr[2],self.rects["exit_Rect"])
        
    def blit_texts(self):
        self.text("Jogar","white",150,335,34)
        self.text("Forma","white",145,425,34)
        self.text("Sair","white",160,515,34)
        
    def mus_play(self):
        if not self.played:
            self.nav_mus.play()
            self.played = True

    def game_loop(self):
        while True:
            self.pos_x , self.pos_y = pygame.mouse.get_pos()
            self.window.fill(self.colors["fundo"])
            for self.event in pygame.event.get():
                if self.event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif self.event.type == pygame.MOUSEBUTTONDOWN:
                    if self.pos_x > 20 and self.pos_x < 220:
                        #clique do botão sair
                        if self.pos_y > 520 and self.pos_y < 590:
                            pygame.quit()
                            sys.exit()
                    if self.pos_x > 20 and self.pos_x < 220:
                        #clique do jogar
                        if self.pos_y > 340 and self.pos_y < 410:
                            self.load_screen = True
                            break
                    if self.pos_x >20 and self.pos_x<200:
                        #clique das configurações
                        if self.pos_y > 430 and self.pos_y < 500:
                            self.load_settings = True
            if self.load_screen:
                self.load_screen = False
                os.system('main.py')


            elif self.load_settings:
                break
            self.clock.tick(self.fps)
            self.check_mouse_pos()
            self.draw_rects()
            self.blit_texts()
            self.window.blit(self.back,(400,240))
            pygame.display.update()

main = Main()

if main.load_settings:
    settings = Settings(main)