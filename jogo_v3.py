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
font = pygame.font.SysFont(None, 48)
fundo = pygame.image.load('imagens/ceu_azul.jpg').convert()
fundo = pygame.transform.scale(fundo, (700, 850))
passaro_img = pygame.image.load('imagens/passaro.gif').convert_alpha()
passaro_img = pygame.transform.scale(passaro_img, (passaro_largura, passaro_altura))


class Passaro(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, largura-passaro_largura)
        self.rect.y = random.randint (-100, -passaro_altura)
        self.speedx = random.randint(-3, 3)
        self.speedy = random.randint(2,9)
    
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.top > altura or self.rect.right < 0 or self.rect.left > largura:
            self.rect.x = random.randint(0, largura-passaro_largura)
            self.rect.y = random.randint (-100, -passaro_altura)
            self.speedx = random.randint(-3, 3)
            self.speedy = random.randint(2,9)


#inicia estruturas
game = True

clock = pygame.time.Clock()
FPS = 30

passaro1 = Passaro(passaro_img)
passaro2 = Passaro(passaro_img)

while game:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    
    passaro1.update()
    passaro2.update()


#gera fundo

    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(fundo, (0, 0))
    window.blit(passaro1.image, passaro1.rect)
    window.blit(passaro2.image, passaro2.rect)

    pygame.display.update()



pygame.quit()


