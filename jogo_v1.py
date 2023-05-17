import pygame

pygame.init()

#Gerar tela principal

window = pygame.display.set_mode ((700, 850))
pygame.display.set_caption('UP Challenge')

game = True

image = pygame.image.load('imagens/ceu_azul.jpg').convert()
image = pygame.transform.scale(image, (700, 850))

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

#gera fundo

    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(image, (0, 0))

    pygame.display.update()

pygame.quit()
