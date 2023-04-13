import pygame
from pygame.locals import*
from sys import exit
from random import randint
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

# Variavel ponto
pts = 0

# Definição da tela
tela = pygame.display.set_mode((lar, alt))
pygame.display.set_caption("::::GAME DO MISAEL::::")

# Função para aumentar a cobra
def aum_cobra():
    for XeY in lista_cobra:
        pygame.draw.rect(tela (0, 255, 0), (XeY[0],XeY[1], 10, 10))


# Inspecionando tela
while True:
    tela.fill((255, 255, 255))
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

# Armazenando posição da cobra
    lista_cbc= [x_cobra, y_cobra]
# Crescendo a cobra
    lista_cobra= []
    lista_cobra.append(lista_cbc)


# Exibe as mensagens na tela
    tela.blit(texto_form, (340, 50))
    tela.blit(texto_form2, (340, 10))
    pygame.display.update()
