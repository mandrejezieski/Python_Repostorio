import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

largura = 1000
altura = 700

x_cobra = int(largura / 2)
y_cobra = int(altura / 2)

velocidade = 10
x_controle = velocidade
y_controle = 0
vel = 10
x_maca = randint(40, 980)
y_maca = randint(50, 680)

pontos = 0
fonte = pygame.font.SysFont('arial', 40, bold=True, italic=True)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption(':::: GAME DO MISA ::::')
relogio = pygame.time.Clock()
lista_cobra = []
comprimento_inicial = 5
morreu = False

def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        # XeY = [x, y]
        # XeY[0] = x
        # XeY[1] = y
        pygame.draw.rect(tela, (0, 255, 0), (XeY[0], XeY[1], 10, 10))

### REINICIO DO JOGO APÓS O GAME OVER
def reiniciar_jogo():
    global pontos, comprimento_inicial, x_cobra, y_cobra, lista_cobra, lista_cabeca, x_maca, y_maca, morreu
    pontos = 0
    comprimento_inicial = 1
    x_cobra = int(largura / 2)
    y_cobra = int(altura / 2)
    lista_cobra = []
    lista_cabeca = []
    x_maca = randint(40, 980)
    y_maca = randint(50, 680)
    morreu = False


while True:
    relogio.tick(vel)
    tela.fill((0, 0, 0))

    mensagem = f'Pontos: {pontos}'
    mensagem2 = f':::: GAME DO MISA ::::'
    texto_formatado = fonte.render(mensagem, True, (255, 0, 0))
    texto_formatado2 = fonte.render(mensagem2, True, (255, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0
            if event.key == K_d:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0
            if event.key == K_w:
                if y_controle == velocidade:
                    pass
                else:
                    y_controle = -velocidade
                    x_controle = 0
            if event.key == K_s:
                if y_controle == -velocidade:
                    pass
                else:
                    y_controle = velocidade
                    x_controle = 0

    x_cobra = x_cobra + x_controle
    y_cobra = y_cobra + y_controle

    cobra = pygame.draw.rect(tela, (0, 255, 0), (x_cobra, y_cobra, 10, 10))
    maca = pygame.draw.cir
        #(tela, (0, 0, 255), (x_maca, y_maca, 40, 40))

    if cobra.colliderect(maca):
        x_maca = randint(40, 980)
        y_maca = randint(50, 680)
        pontos += 1
        vel += 1
        #barulho_colisao.play()
        comprimento_inicial = comprimento_inicial + 1

    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)

    lista_cobra.append(lista_cabeca)

    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]

    aumenta_cobra(lista_cobra)

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

    tela.blit(texto_formatado2, (180, 20))
    tela.blit(texto_formatado, (400, 80))

    pygame.display.update()