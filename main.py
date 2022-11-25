#Importando biblioteca pygame
import pygame as pg
#importando classe jogador
from jogador import Jogador
#importando classe bolinha
from bolinha import Bolinha
#importando classe tijolinho
from tijolinho import Tijolinho
 
pg.init()
 
#Definindo cores
ROSA_ESCURO = (242,167,187) #coração
ROSA_CLARO = (242,220,242) #barrinha
BEGE = (242,237,213) #tijolo 1
LARANJA = (242,168,141) #tijolo 2
CORAL = (242,197,187) #tijolo 3
FUNDO = (135,206,250) #fundo
BRANCO = (255,255,255)
 
pontos = 0 #pontuação se inicia em zero!!
vidas = 5 #jogador começa com cinco vidas
 
# abrindo tela do jogo
size = (800, 600) #tamanho da janela
screen = pg.display.set_mode(size)
pg.display.set_caption("Jogo Breakout <3")
 
#lista de sprites
lista_sprites = pg.sprite.Group()
 
#Criando e posicionando jogador
jogador = Jogador(ROSA_CLARO, 100, 10)
jogador.rect.x = 350
jogador.rect.y = 560
 
#Criando e posicionando a bolinha
bolinha = Bolinha(ROSA_ESCURO,10,10)
bolinha.rect.x = 345
bolinha.rect.y = 195
 
todos_tijolinhos = pg.sprite.Group()
for i in range(7):
    tijolinho = Tijolinho(LARANJA,80,30)
    tijolinho.rect.x = 60 + i* 100
    tijolinho.rect.y = 60
    lista_sprites.add(tijolinho)
    todos_tijolinhos.add(tijolinho)
for i in range(7):
    tijolinho = Tijolinho(CORAL,80,30)
    tijolinho.rect.x = 60 + i* 100
    tijolinho.rect.y = 100
    lista_sprites.add(tijolinho)
    todos_tijolinhos.add(tijolinho)
for i in range(7):
    tijolinho = Tijolinho(BEGE,80,30)
    tijolinho.rect.x = 60 + i* 100
    tijolinho.rect.y = 140
    lista_sprites.add(tijolinho)
    todos_tijolinhos.add(tijolinho)
 
# Adiciona jogador na lista de sprites
lista_sprites.add(jogador)
# Adiciona bolinha na lista de sprites
lista_sprites.add(bolinha)
 
# loop continua até o jogador sair do jogo
jogando = True
 
# Tempo de atualização da tela
cronometro = pg.time.Clock()
 
# -------- Loop principal -----------
while jogando:
    # --- evento principal
    for event in pg.event.get(): # jogador faz algo
        if event.type == pg.QUIT: # se fechar
              jogando = False # loop acaba
 
    #Move o jogador quando precionar teclas de seta
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        jogador.irEsquerda(5)
    if keys[pg.K_RIGHT]:
        jogador.irDireita(5)
 
    # --- lógica do jogo
    lista_sprites.update()
 
    #Verifica se a bolinha está batendo em uma das quatro paredes
    if bolinha.rect.x>=790:
        bolinha.velocity[0] = -bolinha.velocity[0]
    if bolinha.rect.x<=0:
        bolinha.velocity[0] = -bolinha.velocity[0]
    if bolinha.rect.y>590:
        bolinha.velocity[1] = -bolinha.velocity[1]
        vidas -= 1
        if vidas == 0:
            #mensagem de fim de jogo
            font = pg.font.Font(None, 74)
            text = font.render("MORREU :(", 1, BRANCO)
            screen.blit(text, (250,300))
            pg.display.flip()
            pg.time.wait(3000)
 
            #para o jogo
            jogando=False
 
    if bolinha.rect.y<40:
        bolinha.velocity[1] = -bolinha.velocity[1]
 
    #Detectando colisoes entre a bolinha e o jogador
    if pg.sprite.collide_mask(bolinha, jogador):
      bolinha.rect.x -= bolinha.velocity[0]
      bolinha.rect.y -= bolinha.velocity[1]
      bolinha.bounce()
 
    #Verifica se a bolinha colidiu em algum tijolinho
    lista_colisao_tijolinhos = pg.sprite.spritecollide(bolinha,todos_tijolinhos,False)
    for tijolinho in lista_colisao_tijolinhos:
      bolinha.bounce()
      pontos += 1
      tijolinho.kill()
      if len(todos_tijolinhos)==0:
           #mostra mensagem de nivel concluído
            font = pg.font.Font(None, 74)
            text = font.render("MANDOU MUITO :)", 1, BRANCO)
            screen.blit(text, (200,300))
            pg.display.flip()
            pg.time.wait(3000)
 
            #para o jogo
            jogando=False
 
    # --- limpa tela e define cor de fundo
    screen.fill(FUNDO)
    #desenha a linha que separa os placares
    pg.draw.line(screen, BRANCO, [0, 38], [800, 38], 2)
 
    #placar de pontuação
    font = pg.font.Font(None, 34)
    text = font.render("Pontos: " + str(pontos), 1, BRANCO)
    screen.blit(text, (20,10))
    #placar de vidas
    text = font.render("Vidas: " + str(vidas), 1, BRANCO)
    screen.blit(text, (650,10))
 
    #desenha sprites de uma vez só
    lista_sprites.draw(screen)
 
    # --- atualiza a tela
    pg.display.flip()
 
    # ---limite de 60 frames por segundo
    cronometro.tick(60)
 
#quando sair do loop, acaba o programa
pg.quit()