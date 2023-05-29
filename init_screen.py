import pygame
import random
from os import path


BLACK = (0, 0, 0)

def init_screen(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo da tela inicial
    background = pygame.image.load(path.join(IMG_DIR, 'imagens/inicio.jpg')).convert()
    background_rect = background.get_rect()

    running = True
    while running:
        # Ajusta a velocidade do jogo.
        clock.tick(30)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYUP:
                running = False
    
        screen.fill(BLACK)
        screen.blit(background, background_rect)

        pygame.display.flip()
    return state