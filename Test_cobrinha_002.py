import pygame
from pygame.locals import *
from sys import exit
from random import randint


pygame.init()

### TAMANHO DA TELA:
largura = 600
altura = 400

### LOCAL DE SPAWN DO PERSONAGEM:
x_cobra = int(largura / 2)
y_cobra = int(altura / 2)

### CONTROLE
velocidade = 10
x_controle = 15
y_controle = 0
vel = 10

### SEGUNDO ELEMENTO DO JOGO ("O ALIMENTO"):
x_maca = randint(40, 580)
y_maca = randint(50, 380)

### CONFIGURAÇÃO DO CONTADOR DE PONTOS:
pontos = 0
fonte = pygame.font.SysFont(': GAME DA COBRINHA : ', 40, True, True)

### CONFIGURAÇÕES DA TELA:
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption(': GAME DA COBRINHA : ')
relogio = pygame.time.Clock()

### TAMANHO INICIAL DA COBRA
lista_cobra = []
comprimento_inicial = 3

morreu = False


def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        pygame.draw.rect(tela, (50, 100, 150), (XeY[0], XeY[1], 20, 20))


### REINICIO DO JOGO APÓS O GAME OVER
def reiniciar_jogo():
    global pontos, comprimento_inicial, x_cobra, y_cobra, lista_cobra, lista_cabeca, x_maca, y_maca, morreu
    pontos = 0
    comprimento_inicial = 1
    x_cobra = int(largura / 2)
    y_cobra = int(altura / 2)
    lista_cobra = []
    lista_cabeca = []
    x_maca = randint(40, 580)
    y_maca = randint(50, 380)
    morreu = False


### REPETIÇÃO DO JOGO (TODOS OS JOGOS SE PASSAM NUM LOOP INFINITO):
while True:
    relogio.tick(vel)
    tela.fill((50, 50, 50))
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        # DEFINE OS BOTÕES DE CONTROLE DE DIREÇÃO DO PERSONAGEM (W, A, S, D)
        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = - velocidade
                    y_controle = 0
            if event.key == K_d:
                if x_controle == - velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0
            if event.key == K_w:
                if y_controle == velocidade:
                    pass
                else:
                    y_controle = - velocidade
                    x_controle = 0
            if event.key == K_s:
                if y_controle == - velocidade:
                    pass
                else:
                    y_controle = velocidade
                    x_controle = 0

    x_cobra = x_cobra + x_controle
    y_cobra = y_cobra + y_controle

    ### PERSONAGENS
    cobra = pygame.draw.rect(tela, (50, 100, 150), (x_cobra, y_cobra, 20, 20))
    maca = pygame.draw.rect(tela, (255, 0, 0), (x_maca, y_maca, 20, 20))


    ### CONDIÇÃO DE COLISÃO:
    if cobra.colliderect(maca):
        x_maca = randint(40, 580)
        y_maca = randint(50, 380)
        pontos += 1
        vel += 1
        #som_da_colisao.play()
        comprimento_inicial = comprimento_inicial + 1

    ### CRIA O CORPO DA COBRA
    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)
    lista_cobra.append(lista_cabeca)

    ### APRESENTA A TELA DE "GAME OVER"
    if lista_cobra.count(lista_cabeca) > 1:
        fonte2 = pygame.font.SysFont(': GAME DA COBRINHA : ', 20, True, True)
        mensagem = 'Game Over! Sua pontuação foi {}. Pressione "R" para jogar novamente.'.format(pontos)
        texto_formatado = fonte2.render(mensagem, True, (0, 0, 0))
        ret_texto = texto_formatado.get_rect()

        morreu = True
        while morreu:
            tela.fill((20, 80, 140))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()

            ret_texto.center = (largura // 2, altura // 2)
            tela.blit(texto_formatado, ret_texto)
            pygame.display.update()

    ### FAZ COM QUE A COBRA APAREÇA NO EXTREMO OPOSTO, CASO TENTE ATRAVESSAR A TELA
    if x_cobra > largura:
        x_cobra = 0
    if x_cobra < 0:
        x_cobra = largura
    if y_cobra > altura:
        y_cobra = 0
    if y_cobra < 0:
        y_cobra = altura

    ### ESTABELECE UM COMPRIMENTO INICIAL PARA A COBRA
    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]

    aumenta_cobra(lista_cobra)

    tela.blit(texto_formatado, (400, 20))
    pygame.display.update()