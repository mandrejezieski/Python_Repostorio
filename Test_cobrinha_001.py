import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

#pygame.mixer.music.set_volume(0.1)
#musica_de_fundo = pygame.mixer.music.load('BoxCat_Games_-_08_-_CPU_Talk (1).mp3')
#pygame.mixer.music.play(-1)

#barulho_colisao = pygame.mixer.Sound('smw_coin (1).wav')

largura = 700
altura = 500

x_cobra = int(largura / 2)
y_cobra = int(altura / 2)

velocidade = 10
x_controle = velocidade
y_controle = 0
vel = 10
x_maca = randint(40, 600)
y_maca = randint(50, 400)

pontos = 0
fonte = pygame.font.SysFont('arial', 40, bold=True, italic=True)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption(':::: GAME DO MISA ::::')
relogio = pygame.time.Clock()
lista_cobra = []
comprimento_inicial = 100


def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        # XeY = [x, y]
        # XeY[0] = x
        # XeY[1] = y
        pygame.draw.rect(tela, (0, 255, 0), (XeY[0], XeY[1], 10, 10))

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
    maca = pygame.draw.rect(tela, (0, 0, 255), (x_maca, y_maca, 40, 40))

    if cobra.colliderect(maca):
        x_maca = randint(40, 600)
        y_maca = randint(50, 400)
        pontos += 1
      #  vel += 1
        #barulho_colisao.play()
        comprimento_inicial = comprimento_inicial + 1

    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)

    lista_cobra.append(lista_cabeca)

    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]

    aumenta_cobra(lista_cobra)

    tela.blit(texto_formatado2, (180, 20))
    tela.blit(texto_formatado, (400, 80))

    pygame.display.update()