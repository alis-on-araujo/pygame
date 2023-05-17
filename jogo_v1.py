import pygame
import random

pygame.init()

#Gerar tela principal
largura = 700
altura = 850
window = pygame.display.set_mode ((largura, altura))
pygame.display.set_caption('UP Challenge')

#Gera passaros
passaro_largura = 50
passaro_altura = 38
passaro_img = pygame.image.load('imagens/passaro.gif').convert_alpha()
passaro_img_small = pygame.transform.scale(passaro_img, (passaro_largura, passaro_altura))

#inicia estruturas
game = True
passaro_x = random.randint (0, largura-passaro_largura)
passaro_y = random.randint (-100, -passaro_altura)
passaro_speedx = random.randint(-3,3)
passaro_speedy = random.randint(2,9)

image = pygame.image.load('imagens/ceu_azul.jpg').convert()
image = pygame.transform.scale(image, (700, 850))

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False


    passaro_x += passaro_speedx
    passaro_y += passaro_speedy

    if passaro_y > altura or passaro_x + passaro_largura < 0 or passaro_x > largura:
        passaro_x = random.randint (0, largura-passaro_largura)
        passaro_y = random.randint (-100, -passaro_altura)
        passaro_speedx = random.randint(-3,3)
        passaro_speedy = random.randint(2,9)
#gera fundo

    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(image, (0, 0))

    window.blit(passaro_img_small, (passaro_x, passaro_y))



    pygame.display.update()

pygame.quit()
