import pygame
from pygame.locals import*
from sys import exit
from random import randint
pygame.init()


lar = 500
alt = 400
x = lar / 2
y = alt / 2
x_amer = randint(40, 400)
y_amer = randint(50, 300)

font = pygame.font.SysFont("arial", 20, True, True)
nome_do_game = pygame.font.SysFont("arial", 20, True, True)
pts = 0

tela = pygame.display.set_mode((lar, alt))
pygame.display.set_caption("::::GAME DO MISAEL::::")

while True:
    tela.fill((0, 0, 0))
    msg2 = f'game do misa'
    msg = f'pontos: {pts}'

    texto_form2 = font.render(msg2, True, (0, 255, 0))
    texto_form = font.render(msg, True, (0, 0, 255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    if pygame.key.get_pressed()[K_a]:
        x = x - 0.2
    if pygame.key.get_pressed()[K_d]:
        x = x + 0.2
    if pygame.key.get_pressed()[K_w]:
        y = y - 0.2
    if pygame.key.get_pressed()[K_s]:
        y = y + 0.2

    red_ver = pygame.draw.rect(tela, (255, 0, 0), (x, y, 10, 10))
    red_amer = pygame.draw.rect(tela, (255, 255, 0), (x_amer, y_amer, 50, 50))
    if red_ver.colliderect(red_amer):
        x_amer = randint(40, 400)
        y_amer = randint(50, 300)
        pts = pts + 1
    tela.blit(texto_form, (340, 50))
    tela.blit(texto_form2, (340, 10))
    pygame.display.update()
