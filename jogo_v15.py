import pygame
import random
import time
from config import YELLOW

pygame.init()
pygame.mixer.init()

# Gerar tela principal
largura = 700
altura = 850
window = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('UP Challenge')

font = pygame.font.SysFont(None, 48)

#Carrega sons
som_fundo = pygame.mixer.Sound('audio/Married Life.mp3')
som_fundo.set_volume(0.5) 
som_fundo.play(loops=-1)
som_estrela = pygame.mixer.Sound('audio/estrela_som.mp3')

# Gera passaros
passaro_largura = 30
passaro_altura = 20
passaro_img = pygame.image.load('imagens/passaro.gif').convert_alpha()
passaro_img = pygame.transform.scale(passaro_img, (passaro_largura, passaro_altura))

# Gera casa
casa_largura = 80
casa_altura = 80
casa_img = pygame.image.load('imagens/casa_sem_balões.png').convert_alpha()
casa_img = pygame.transform.scale(casa_img, (casa_largura, casa_altura))

#Gera Balões
balões_largura= 80
balões_altura=120
balões_img = pygame.image.load('imagens/balões.png').convert_alpha()
balões_img = pygame.transform.scale(balões_img, (balões_largura, balões_altura))

#Gera Estrelas:
estrela_largura = 40
estrela_altura = 40
estrela_img = pygame.image.load('imagens/estrela.png').convert_alpha()
estrela_img = pygame.transform.scale(estrela_img, (estrela_largura, estrela_altura))

# Gera fundo
fundo = pygame.image.load('imagens/ceu_azul1.jpg').convert()
fundo = pygame.transform.scale(fundo, (700, 850))
fundo_rect = fundo.get_rect()

#Fonte de score
scorefont = pygame.font.SysFont('cooper', 48)

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
        if self.rect.top < 100:
            self.rect.top = 100
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
        if self.rect.top < 100:
            self.rect.top = 100
        if self.rect.bottom > altura:
            self.rect.bottom = altura

class Estrela(pygame.sprite.Sprite):
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
        if self.rect.top < 100:
            self.rect.top = 100
        if self.rect.bottom > altura:
            self.rect.bottom = altura

def exibir_tela_inicio():
    tela_inicio = pygame.image.load('imagens/inicio.jpg').convert_alpha()
    window.blit(tela_inicio, (-600, 0))
    pygame.display.flip()

def exibir_tela_pausa():
    tela_pausa = pygame.image.load('imagens/pausa.png').convert_alpha()
    window.blit(tela_pausa, (0, 0))
    pygame.display.flip()

def exibir_tela_final():
    tela_final = pygame.image.load('imagens/final.jpg').convert_alpha()
    window.blit(tela_final, (0, 0))
    pygame.display.flip()

# Função para criar balões
def criar_balões():
    balões = Balões(balões_img)
    all_sprites.add(balões)
    balões_list.add(balões)

# Função para criar estrelas
def criar_estrela():
    estrela = Estrela(estrela_img)
    all_sprites.add(estrela)
    estrela_list.add(estrela)

all_sprites = pygame.sprite.Group()
balões_list = pygame.sprite.Group()
estrela_list = pygame.sprite.Group()

casa = Casa(casa_img)
all_sprites.add(casa)

score = 0

clock = pygame.time.Clock()

game = True
estado_jogo = "inicio"
tecla_pressionada = False

while game:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                tecla_pressionada = True

    if estado_jogo == "inicio":
        exibir_tela_inicio()

        if tecla_pressionada:
            estado_jogo = "jogando"

    elif estado_jogo == "jogando":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    casa.speedx = -5
                elif event.key == pygame.K_RIGHT:
                    casa.speedx = 5
                elif event.key == pygame.K_UP:
                    casa.speedy = -5
                elif event.key == pygame.K_DOWN:
                    casa.speedy = 5
                elif event.key == pygame.K_p:
                    estado_jogo = "pausa"

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    casa.speedx = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    casa.speedy = 0

        all_sprites.update()

        # Colisão entre balões e casa
        balões_hit = pygame.sprite.spritecollide(casa, balões_list, True)

        for balões in balões_hit:
            score += 1
            som_estrela.play()

        # Colisão entre estrelas e casa
        estrela_hit = pygame.sprite.spritecollide(casa, estrela_list, True)

        for estrela in estrela_hit:
            score += 10
            som_estrela.play()

        # Gera balões aleatoriamente
        if random.randint(1, 100) < 2:
            criar_balões()

        # Gera estrelas aleatoriamente
        if random.randint(1, 100) < 1:
            criar_estrela()

        window.blit(fundo, fundo_rect)

        all_sprites.draw(window)

        score_text = scorefont.render("Score: " + str(score), True, YELLOW)
        window.blit(score_text, [10, 10])

        pygame.display.flip()

    elif estado_jogo == "pausa":
        exibir_tela_pausa()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    estado_jogo = "jogando"

    if estado_jogo == "final":
        exibir_tela_final()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    estado_jogo = "inicio"

pygame.quit()
