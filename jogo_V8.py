import pygame
import random
import time

pygame.init()

# Gerar tela principal
largura = 700
altura = 850
window = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('UP Challenge')

# Gera passaros
passaro_largura = 30
passaro_altura = 20
casa_largura = 60
casa_altura = 80
balões_largura= 60
balões_altura=120
font = pygame.font.SysFont(None, 48)
fundo = pygame.image.load('imagens/ceu_azul.jpg').convert()
fundo = pygame.transform.scale(fundo, (700, 850))
passaro_img = pygame.image.load('imagens/passaro.gif').convert_alpha()
passaro_img = pygame.transform.scale(passaro_img, (passaro_largura, passaro_altura))
casa_img = pygame.image.load('imagens/casa_sem_balões.png').convert_alpha()
casa_img = pygame.transform.scale(casa_img, (casa_largura, casa_altura))
balões_img = pygame.image.load('imagens/balões.png').convert_alpha()
balões_img = pygame.transform.scale(balões_img, (balões_largura, balões_altura))

class Casa(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = largura / 2
        self.rect.bottom = altura - 10
        self.speedx = 0
        self.speedy = 0

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        # Mantem dentro da tela
        if self.rect.right > largura:
            self.rect.right = largura

        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.top < 0:
            self.rect.top = 0

        if self.rect.bottom > altura:
            self.rect.bottom = altura

class Balões(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = largura / 2
        self.rect.bottom = altura - 65
        self.speedx = 0
        self.speedy = 0

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        # Mantem dentro da tela
        if self.rect.right > largura:
            self.rect.right = largura

        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.top < 0:
            self.rect.top = 0

        if self.rect.bottom > altura:
            self.rect.bottom = altura


class Passaro(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = largura
        self.rect.y = random.randint(5, 750)
        self.speedx = random.randint(-10, -6)
        self.speedy = 0

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.right < 0 or self.rect.left > largura:
            self.rect.x = largura
            self.rect.y = random.randint(5, 750)
            self.speedx = random.randint(-10, -6)
            self.speedy = 0


# Inicia estruturas
game = True

clock = pygame.time.Clock()
FPS = 30

todospassaros = pygame.sprite.Group()
todospassaros2 = pygame.sprite.Group()

jogador = Casa(casa_img)
jogador_balões = Balões(balões_img)
todospassaros.add(jogador)
todospassaros.add(jogador_balões)

timer = 0 
timer_started = False
start_time = time.time()  # Tempo inicial do jogo

while game:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                jogador_balões.speedx -= 10
            if event.key == pygame.K_RIGHT:
                jogador_balões.speedx += 10
            if event.key == pygame.K_UP:
                jogador_balões.speedy -= 10
            if event.key == pygame.K_DOWN:
                jogador_balões.speedy += 10

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                jogador_balões.speedx += 10
            if event.key == pygame.K_RIGHT:
                jogador_balões.speedx -= 10
            if event.key == pygame.K_UP:
                jogador_balões.speedy += 10
            if event.key == pygame.K_DOWN:
                jogador_balões.speedy -= 10

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                jogador.speedx -= 10
            if event.key == pygame.K_RIGHT:
                jogador.speedx += 10
            if event.key == pygame.K_UP:
                jogador.speedy -= 10
            if event.key == pygame.K_DOWN:
                jogador.speedy += 10

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                jogador.speedx += 10
            if event.key == pygame.K_RIGHT:
                jogador.speedx -= 10
            if event.key == pygame.K_UP:
                jogador.speedy += 10
            if event.key == pygame.K_DOWN:
                jogador.speedy -= 10

    # Verifica o tempo decorrido
    current_time = time.time() - start_time

    if current_time >= 1 and not timer_started:
        timer_started = True
        start_time = time.time()

    if timer_started:
        if current_time >= 1 and timer == 0:
            # Cria um novo pássaro a cada 2 segundos
            for i in range(5):
                passaro = Passaro(passaro_img)
                todospassaros.add(passaro)
                todospassaros2.add(passaro)
            timer += 1
    
    jogador.rect.x += jogador.speedx
    jogador.rect.y += jogador.speedy 

    jogador_balões.rect.x += jogador_balões.speedx
    jogador_balões.rect.y += jogador_balões.speedy 

    todospassaros.update()

    hits = pygame.sprite.spritecollide(jogador_balões, todospassaros2, True)
    if len(hits)>0:
        game = False

    window.blit(fundo, (0, 0))
    todospassaros.draw(window)
    pygame.display.flip()

pygame.quit()