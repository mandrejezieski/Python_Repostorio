import pygame
from pygame.locals import*
from sys import exit
from random import randint
pygame.init()

# tamanho da tela
lar = 500
alt = 400

# tamanho da cobra
x_cobra = lar / 2
y_cobra = alt / 2


x_maca = randint(40, 400)
y_maca = randint(50, 300)

font = pygame.font.SysFont("arial", 20, True, True)
nome_do_game = pygame.font.SysFont("arial", 20, True, True)
pts = 0

# Definição da tela
tela = pygame.display.set_mode((lar, alt))
pygame.display.set_caption("::::GAME DO MISAEL::::")

# Inspecionando tela
while True:
    tela.fill((255, 255, 255))
    msg2 = f'game do misa'
    msg = f'pontos: {pts}'

# Mensagens na tela
    texto_form2 = font.render(msg2, True, (0, 255, 0))
    texto_form = font.render(msg, True, (0, 0, 255))

# Condições de saida
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

# controle da cobra
    if pygame.key.get_pressed()[K_a]:
        x_cobra= x_cobra - 0.2
    if pygame.key.get_pressed()[K_d]:
        x_cobra = x_cobra + 0.2
    if pygame.key.get_pressed()[K_w]:
        y_cobra = y_cobra - 0.2
    if pygame.key.get_pressed()[K_s]:
        y_cobra = y_cobra + 0.2

#Colição da cobra com a maça
    cobra = pygame.draw.rect(tela, (0, 255, 0), (xcobra, ycobra, 10, 10))

# Se acontecer a colição maça se movimenta aleatoriamente
# e agrecenta um na variavel ponto
    if cobra.colliderect(maca):
        x_maca = randint(40, 400)
        y_maca = randint(50, 300)
        pts = pts + 1

# Exibe as mensagens na tela
    tela.blit(texto_form, (340, 50))
    tela.blit(texto_form2, (340, 10))
    pygame.display.update()
