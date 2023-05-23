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

        if self.rect.top < 0:
            self.rect.top = 0

        if self.rect.bottom > altura - 55:
            self.rect.bottom = altura - 55


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


class Estrela(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, largura)  # Posição x aleatória dentro da largura da tela
        self.rect.y = random.randint(-500, -50)  # Posição y aleatória acima da tela
        self.speedx = 0
        self.speedy = random.randint(6, 10)  # Velocidade vertical aleatória para a estrela cair
        self.visible = True
        self.cooldown = False

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.top > altura:  
            self.rect.x = random.randint(0, largura)  
            self.rect.y = random.randint(-500, -50)  
            self.speedy = random.randint(6, 10)  
            self.visible = True
            self.cooldown = False

# Inicia estruturas
game = True

clock = pygame.time.Clock()
FPS = 30



todospassaros = pygame.sprite.Group()
todospassaros2 = pygame.sprite.Group()
todasestrelas = pygame.sprite.Group()

jogador = Casa(casa_img)
jogador_balões = Balões(balões_img)
todospassaros.add(jogador)
todospassaros.add(jogador_balões)


timer = 0
timer_started = False
start_time = time.time()  # Tempo inicial do jogo
score = 0


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
                jogador_balões.speedy -= 6
            if event.key == pygame.K_DOWN:
                jogador_balões.speedy += 10
         

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                jogador_balões.speedx += 10
            if event.key == pygame.K_RIGHT:
                jogador_balões.speedx -= 10
            if event.key == pygame.K_UP:
                jogador_balões.speedy += 6
            if event.key == pygame.K_DOWN:
                jogador_balões.speedy -= 10
         

        
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                jogador.speedx -= 10
            if event.key == pygame.K_RIGHT:
                jogador.speedx += 10
            if event.key == pygame.K_UP:
                jogador.speedy -= 6
            if event.key == pygame.K_DOWN:
                jogador.speedy += 10
            

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                jogador.speedx += 10
            if event.key == pygame.K_RIGHT:
                jogador.speedx -= 10
            if event.key == pygame.K_UP:
                jogador.speedy += 6
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

            for i in range(1):
                estrela = Estrela(estrela_img)
                todospassaros.add(estrela)
                todasestrelas.add(estrela)


            timer += 1

        if current_time >= 1:
                    score += 10

        if current_time < 0:
                game = False
    

    

    
    jogador.rect.x += jogador.speedx
    jogador.rect.y += jogador.speedy 

    jogador_balões.rect.x += jogador_balões.speedx
    jogador_balões.rect.y += jogador_balões.speedy 

    todospassaros.update()

    hits = pygame.sprite.spritecollide(jogador_balões, todospassaros2, True)
    if len(hits) > 0:
        game = False

    hits_2 = pygame.sprite.spritecollide(jogador_balões, todasestrelas, True)
    for hit in hits_2:
        for i in range(1):
            estrela = Estrela(estrela_img)
            todospassaros.add(estrela)
            todasestrelas.add(estrela)
        som_estrela.play()
   

    # Movimento do fundo
    fundo_rect.y += 2

    # Se o fundo saiu da janela, faz ele voltar para cima
    if fundo_rect.top > altura:
        fundo_rect.y -= fundo_rect.height

    # Desenha o fundo e uma cópia para baixo
    window.blit(fundo, fundo_rect)
    fundo_rect2 = fundo_rect.copy()
    fundo_rect2.y -= fundo_rect2.height
    window.blit(fundo, fundo_rect2)

    text_surface = font.render('{:06d}'.format(score), True, YELLOW)

    text_rect = text_surface.get_rect()
    text_rect.midtop = (largura/2, 30)
    window.blit(text_surface, text_rect)
    todospassaros.draw(window)

    pygame.display.flip()

pygame.quit()
