from typing import List, Any
import pygame
from pygame.locals import*
from sys import exit
from random import randint

# Iniciando o pygame
pygame.init()

# tamanho da tela
lar = 500
alt = 400

# Tamanho da cobra
x_cobra = lar / 2
y_cobra = alt / 2

# Tamanho da maça
x_maca = randint(40, 400)
y_maca = randint(50, 300)

# Fonte aplicada nos textos
font = pygame.font.SysFont("arial", 20, True, True)
nome_do_game = pygame.font.SysFont("arial", 20, True, True)

lista_cobra = []
comprimento_inicial = 1

# Função para aumentar a cobra
def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        # XeY = [x, y]
        # XeY[0] = x
        # XeY[1] = y
        pygame.draw.rect(tela, (0, 255, 0), (XeY[0], XeY[1], 10, 10))


# Variavel ponto
pts = 0

# Definição da tela
tela = pygame.display.set_mode((lar, alt))
pygame.display.set_caption("::::GAME DO MISAEL::::")

# Laços de repetição para nspecionar a tela
while True:
    tela.fill((2, 2, 2))
    msg2 = f'game do misa'
    msg = f'pontos: {pts}'

# Mensagens na tela
    texto_form2 = font.render(msg2, True, (100, 100, 0))
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

# Definindo objeto cobra e maça
    cobra = pygame.draw.rect(tela, (0, 255, 0), (x_cobra, y_cobra, 10, 10))
    maca = pygame.draw.rect(tela, (255, 0, 0), (x_maca, y_maca, 10, 10))
    

# Se acontecer a colição, maça se movimenta aleatoriamente
# e agrecenta um na variavel ponto
    if cobra.colliderect(maca):
        x_maca = randint(40, 400)
        y_maca = randint(50, 300)
        pts = pts + 1

    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)

    lista_cobra.append(lista_cabeca)

    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]

    aumenta_cobra(lista_cobra)

# Exibe as mensagens na tela
    tela.blit(texto_form, (340, 50))
    tela.blit(texto_form2, (340, 10))
    pygame.display.update()
