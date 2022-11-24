#Importando a biblioteca pygame  
import pygame as pg
from jogador import Jogador #importando a classe jogador
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

#abrindo a tela do jogo
size = (800, 600)  #tamanho da janela
screen = pg.display.set_mode(size) 
pg.display.set_caption("Jogo Breakout <3") 

#lista de sprites
lista_sprites = pg.sprite.Group()

#criando e posicionando o jogador
jogador = Jogador(ROSA_ESCURO, 100,10)
jogador.rect.x = 350
jogador.rect.y = 560

#adiciona o jogador na lista de sprites
lista_sprites.add(jogador)

#o loop continua até o jogador sair do jogo
jogando = True

#tempo de atualização da tela
cronometro = pg.time.Clock()

'''Loop principal <3'''
while jogando:
    '''Evnto principal'''
    for event in pg.event.get(): #usuaro fez algo
        if event.type == pg.QUIT: #se fechar
                jogando = False 
        elif event.type==pg.KEYDOWN:
                if event.key==pg.K_x: #Pressionar o X vai sair do jogo
                     jogando = False

    # Mover o jogador quando usar as teclas de setas
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        pg.irEsquerda(5)
    if keys[pg.K_RIGHT]:
        pg.irDireita(5)  

    # --- logica do jogo...
    lista_sprites.update()

    #limpa a tela e define a cor de fundo
    screen.fill( FUNDO)
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

    #atualiza a tela
    pg.display.flip()

    #limite de 60 frames por segundo
    cronometro.tick(60)

#quando sair do loop, termina o programa
pg.quit()



