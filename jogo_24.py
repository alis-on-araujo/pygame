import pygame
import random
from config import YELLOW, WHITE

pygame.init()
pygame.mixer.init()

# Gerar tela principal
largura = 700
altura = 850
window = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('UP Challenge')


font = pygame.font.SysFont(None, 48)

#Assets
passaro_largura = 30
passaro_altura = 20
casa_largura = 80
casa_altura = 80
baloes_largura= 80
baloes_altura=120
estrela_largura = 40
estrela_altura = 40
assets = {}
assets['background'] = pygame.image.load('imagens/ceu_azul1.jpg').convert()
assets['background'] = pygame.transform.scale(assets['background'], (700, 850))
assets['passaros_img'] = pygame.image.load('imagens/passaro.gif').convert_alpha()
assets['passaros_img'] = pygame.transform.scale(assets['passaros_img'], (passaro_largura, passaro_altura))
assets['casa_img'] = pygame.image.load('imagens/casa_sem_balões.png').convert_alpha()
assets['casa_img'] = pygame.transform.scale(assets['casa_img'], (casa_largura, casa_altura))
assets['baloes_img1'] = pygame.image.load('imagens/balões.png').convert_alpha()
assets['baloes_img1'] = pygame.transform.scale(assets['baloes_img1'], (baloes_largura, baloes_altura))
assets['baloes_img2'] = pygame.image.load('imagens/Balões_Vida_1.png').convert_alpha()
assets['baloes_img2'] = pygame.transform.scale(assets['baloes_img2'], (baloes_largura, baloes_altura))
assets['baloes_img3'] = pygame.image.load('imagens/Balões_Vida_2.png').convert_alpha()
assets['baloes_img3'] = pygame.transform.scale(assets['baloes_img3'], (baloes_largura, baloes_altura))
assets['estrela_img'] = pygame.image.load('imagens/estrela.png').convert_alpha()
assets['estrela_img'] = pygame.transform.scale(assets['estrela_img'], (estrela_largura, estrela_altura))
assets['vida_baloes'] = pygame.image.load('imagens/balão.png').convert_alpha()
assets['vida_baloes'] = pygame.transform.scale(assets['vida_baloes'], (50, 50))
assets['score_font'] = pygame.font.Font('assets/font/PressStart2P.ttf', 28)

fundo_rect = assets['background'].get_rect()

#Carrega sons
som_fundo = pygame.mixer.Sound('audio/Married Life.mp3')
som_fundo.set_volume(0.5) 
som_fundo.play(loops=-1)
som_estrela = pygame.mixer.Sound('audio/estrela_som.mp3')
som_estrela.set_volume(0.5) 
som_balao = pygame.mixer.Sound('audio/balaosom.mp3')
som_balao.set_volume(0.5) 
som_pegavida = pygame.mixer.Sound('audio/somvida.mp3')

class Casa(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets['casa_img']
        self.rect = self.image.get_rect()
        self.rect.centerx = largura / 2
        self.rect.bottom = altura - 10
        self.speedx = 0
        self.speedy = 0
        self.groups = groups
        self.assets = assets

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if contador < 4:

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

        if contador < 4:

            # Mantem dentro da tela
            if self.rect.right > largura:
                self.rect.right = largura

            if self.rect.left < 0:
                self.rect.left = 0

            if self.rect.top < 0:
                self.rect.top = 0

            if self.rect.bottom > altura - 55:
                self.rect.bottom = altura - 55
        
class Vidas(pygame.sprite.Sprite):
    def __init__(self, assets):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets['vida_baloes']
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
            self.rect.x = random.randint(0, largura-10)  
            self.rect.y = random.randint(-500, -50)  
            self.speedy = random.randint(6, 10)  
            self.visible = True
            self.cooldown = False


class Passaro(pygame.sprite.Sprite):
    def __init__(self, asstes):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets['passaros_img']
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
    def __init__(self, assets):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets['estrela_img']
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, largura)  # Posição x aleatória dentro da largura da tela
        self.rect.y = random.randint(-500, -50)  # Posição y aleatória acima da tela
        self.speedx = 0
        self.speedy = random.randint(6, 10)  # Velocidade vertical aleatória para a estrela cair
       

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.top > altura:  
            self.rect.x = random.randint(0, largura-10)  
            self.rect.y = random.randint(-500, -50)  
            self.speedy = random.randint(6, 10)  
            self.visible = True
            self.cooldown = False
  
# Inicia jogo
game = True

# Tempo jogo
clock = pygame.time.Clock()
tempo_atual = pygame.time.get_ticks()
tempo_anterior = tempo_atual
tempo_anterior_estrela = tempo_atual
tempo_anterior_vida = tempo_atual
tempo_anterior_imune = tempo_atual
FPS = 30

# Criando grupo de passaros
todos_sprites = pygame.sprite.Group()
todos_passaros = pygame.sprite.Group()
todas_estrelas = pygame.sprite.Group()
todos_baloes = pygame.sprite.Group()
groups = {}

groups['todos_sprites'] = todos_sprites
groups['todos_passaros'] = todos_passaros
groups['todas_estrelas'] = todas_estrelas
groups['todos_baloes'] = todos_baloes

# criando jogador
jogador = Casa(groups, assets)
todos_sprites.add(jogador)

# criando passaros
for i in range (5):
    passaro = Passaro(assets)
    todos_sprites.add(passaro)
    todos_passaros.add(passaro)

#verifica se pegou vida ou estrela (para não adiconar mais de 1)
pegou_estrela = True
pegou_vida = True

score = 0
contador = 0
contador_estrelas = 0

pode_cair_estrela = True
pode_cair_vida = True

# LOOP PRINCIPAL
som_fundo.play(loops=-1)
while game:

    clock.tick(FPS)
    tempo_atual = pygame.time.get_ticks()

    # Criando 1º balão (balão grande)
    if contador == 0:
        jogador_balões = Balões(assets['baloes_img1'])
        todos_sprites.add(jogador_balões)

        contador += 1


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
            
    jogador.rect.x += jogador.speedx
    jogador.rect.y += jogador.speedy 

    jogador_balões.rect.x += jogador_balões.speedx
    jogador_balões.rect.y += jogador_balões.speedy 

    # atualiza
    todos_sprites.update()


    # adicionando estrela a cada 10 segundos
    if pode_cair_estrela and tempo_atual - tempo_anterior_estrela >= 1000:
        tempo_anterior_estrela = tempo_atual
        pode_cair_estrela = False

        estrela = Estrela(assets)
        todos_sprites.add(estrela)
        todas_estrelas.add(estrela)


    # adicionando balões (vidas) a cada 25 segundos
    if pode_cair_vida and tempo_atual - tempo_anterior_vida >= 25000:
        tempo_anterior_vida = tempo_atual
        pode_cair_vida = False

        vida = Vidas(assets)
        todos_sprites.add(vida)
        todos_baloes.add(vida)

    # Verifica se a casa está imune (se estiver, ficar só por 5 segundos):
    #if contador_estrelas >= 5:
        #tempo_imune = tempo_atual - tempo_anterior_imune
        #if tempo_imune >= 5000:
            #contador_estrelas = 0
            #tempo_anterior_imune = tempo_atual



    if contador_estrelas < 5:
        hits = pygame.sprite.spritecollide(jogador_balões, todos_passaros, True)

    for passaro in hits:
        p = Passaro(assets)
        todos_sprites.add(p)
        todos_passaros.add(p)

    casax = jogador.rect.x
    casay = jogador.rect.y


    if len(hits) > 0 and contador == 1:
        jogador_balões.kill()
        som_balao.play()
        jogador_balões = Balões(assets['baloes_img2'])
        jogador_balões.rect.x = casax
        jogador_balões.rect.y = casay - 100
        jogador_balões.speedx = jogador.speedx
        jogador_balões.speedy = jogador.speedy
        todos_sprites.add(jogador_balões)
        contador += 1

    elif len(hits) > 0 and contador == 2:
        jogador_balões.kill()
        som_balao.play()
        jogador_balões = Balões(assets['baloes_img3'])
        jogador_balões.rect.x = casax
        jogador_balões.rect.y = casay - 100
        jogador_balões.speedx = jogador.speedx
        jogador_balões.speedy = jogador.speedy
        todos_sprites.add(jogador_balões)
        contador += 1

    elif len(hits) > 0 and contador == 3:
         jogador_balões.kill()
         som_balao.play()

         jogador.speedy += 10
         contador += 1


    hits_2 = pygame.sprite.spritecollide(jogador_balões, todas_estrelas, True)
    
    for hit in hits_2:
        som_estrela.play()
        contador_estrelas += 1

    if len(todas_estrelas) == 0:
        pode_cair_estrela = True

    hits_3 = pygame.sprite.spritecollide(jogador_balões, todos_baloes, True)

    for hit in hits_3:
        som_pegavida.play()
        contador -= 1

    if len(hits_3) > 0 and contador == 1:
        jogador_balões.kill()
        jogador_balões = Balões(assets['baloes_img1'])
        jogador_balões.rect.x = casax
        jogador_balões.rect.y = casay - 100
        jogador_balões.speedx = jogador.speedx
        jogador_balões.speedy = jogador.speedy
        todos_sprites.add(jogador_balões)

    elif len(hits_3) > 0 and contador == 2:
        jogador_balões.kill()
        jogador_balões = Balões(assets['baloes_img2'])
        jogador_balões.rect.x = casax
        jogador_balões.rect.y = casay - 100
        jogador_balões.speedx = jogador.speedx
        jogador_balões.speedy = jogador.speedy
        todos_sprites.add(jogador_balões)

    elif len(hits_3) > 0 and contador == 0:
        jogador_balões.kill()
        jogador_balões = Balões(assets['baloes_img1'])
        jogador_balões.rect.x = casax
        jogador_balões.rect.y = casay - 100
        jogador_balões.speedx = jogador.speedx
        jogador_balões.speedy = jogador.speedy
        todos_sprites.add(jogador_balões)

        contador += 1

    

    if len(todos_baloes) == 0:
        pode_cair_vida = True

    

    # Movimento do fundo
    
    fundo_rect.y += 2

    # Se o fundo saiu da janela, faz ele voltar para cima
    if fundo_rect.top > altura:
        fundo_rect.y -= fundo_rect.height

    # Desenha o fundo e uma cópia para baixo
    window.blit(assets['background'], fundo_rect)
    fundo_rect2 = fundo_rect.copy()
    fundo_rect2.y -= fundo_rect2.height
    window.blit(assets['background'], fundo_rect2)

    # Score

    if tempo_atual - tempo_anterior >= 100:
        score += 10
        tempo_anterior = tempo_atual

    text_surface = font.render('{:06d}'.format(score), True, WHITE)

    text_rect = text_surface.get_rect()
    text_rect.midtop = (largura/2, 30)
    window.blit(text_surface, text_rect)
    todos_sprites.draw(window)

    
    
    # Vidas
    vida1 = assets['vida_baloes'].get_rect()
    vida1.bottomleft = (10, altura - 10)

    vida2 = assets['vida_baloes'].get_rect()
    vida2.bottomleft = (40, altura - 10)

    vida3 = assets['vida_baloes'].get_rect()
    vida3.bottomleft = (70, altura - 10)

    if contador == 1:
        window.blit(assets['vida_baloes'], vida1)
        window.blit(assets['vida_baloes'], vida2)
        window.blit(assets['vida_baloes'], vida3)

    elif contador == 2:
        window.blit(assets['vida_baloes'], vida1)
        window.blit(assets['vida_baloes'], vida2)

    elif contador == 3:
        window.blit(assets['vida_baloes'], vida1)

    if casay > 1100:
        game = False
    
    
    posicaoestrela = assets['estrela_img'].get_rect()
    posicaoestrela.topleft = (20, altura-825)
    score_estrela = contador_estrelas 
    text_surface = font.render('{:02d}'.format(score_estrela), True, YELLOW)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (largura-610, 30)
    window.blit(text_surface, text_rect)
    todos_sprites.draw(window)
    window.blit(assets['estrela_img'], posicaoestrela)


    score += 10
    

    
    pygame.display.flip()

pygame.quit()


