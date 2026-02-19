import pygame
from pygame.locals import *
from sys import exit
from random import randint  # gera números aleatórios


pygame.init()


# músicas e sons do jogo
musica_fundo = pygame.mixer.music.load('sons/Lobo Loco - Power Hopping.mp3')
pygame.mixer.music.play(-1)           # toca em loop
pygame.mixer.music.set_volume(0.25)   # volume 25%


# som de coleta
som_coleta = pygame.mixer.Sound('sons/coleta1.wav')
som_coleta.set_volume(0.7)
#som de game over
som_game_over = pygame.mixer.Sound('sons/game_over.wav')
som_game_over.set_volume(0.7)
#som de vitória
som_vitoria = pygame.mixer.Sound('sons/vitoria.ogg')
som_vitoria.set_volume(0.7)

# configurações da tela do jogo
largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo do Sapo')


# fonte para exibir a pontuação e o tempo
fonte = pygame.font.SysFont('arial', 30, True, False)


# imagem de vitória
imagem_vitoria = pygame.image.load('fundos/voce_venceu.jpg')
imagem_vitoria = pygame.transform.scale(imagem_vitoria, (largura, altura))
#imagem de derrota
imagem_derrota = pygame.image.load('fundos/voce_perdeu.jpg')
imagem_derrota = pygame.transform.scale(imagem_derrota, (largura, altura))


# classe base para objetos que caem
class ObjetoCaindo(pygame.sprite.Sprite):
    def __init__(self, imagem, largura_obj, altura_obj, velocidade):
        pygame.sprite.Sprite.__init__(self)
        self.image_original = pygame.image.load(imagem)
        self.image = pygame.transform.scale(self.image_original, (largura_obj, altura_obj))
        self.rect = self.image.get_rect()
        self.velocidade = velocidade
        self.resetar_posicao()


    def resetar_posicao(self):
        self.rect.x = randint(40, 760)
        self.rect.y = -50


    def update(self):
        self.rect.y += self.velocidade
        if self.rect.y > altura:
            self.resetar_posicao()



class Fruta(ObjetoCaindo):
    def __init__(self):
        super().__init__('sprites/maca.png', 20 * 3, 20 * 3, velocidade=5)



class Mosquito(ObjetoCaindo):
    def __init__(self):
        super().__init__('sprites/mosquito.png', 20 * 3, 20 * 3, velocidade=7)



# classe do sapo
class Sapo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)


        self.sprites = [
            pygame.image.load('sprites/attack_1.png'),
            pygame.image.load('sprites/attack_2.png'),
            pygame.image.load('sprites/attack_3.png'),
            pygame.image.load('sprites/attack_4.png'),
            pygame.image.load('sprites/attack_5.png'),
            pygame.image.load('sprites/attack_6.png'),
            pygame.image.load('sprites/attack_7.png'),
            pygame.image.load('sprites/attack_8.png'),
            pygame.image.load('sprites/attack_9.png'),
            pygame.image.load('sprites/attack_10.png')
        ]


        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (128 * 3, 64 * 3))
        self.rect = self.image.get_rect()
        self.rect.topleft = (largura // 2 - 100, altura - 300)
        self.animar = False
        self.velocidade = 10


        # índice do frame attack_7 na lista (0-based)
        self.frame_ataque_valido = 6


    def atacar(self):
        self.animar = True
        self.atual = 0  # começa sempre do primeiro frame do ataque


    def mover(self, dx, dy):
        if dx != 0 or dy != 0:
            # se quiser animação só quando atacar, comente a linha abaixo
            self.animar = True


        self.rect.x += dx * self.velocidade
        self.rect.y += dy * self.velocidade


        # limita dentro da tela
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > largura:
            self.rect.right = largura
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > altura:
            self.rect.bottom = altura


    def update(self):
        if self.animar:
            self.atual += 0.2
            if self.atual >= len(self.sprites):
                self.atual = 0
                self.animar = False


            self.image = self.sprites[int(self.atual)]
            self.image = pygame.transform.scale(self.image, (128 * 3, 64 * 3))


    def esta_no_frame_ataque(self):
        # True quando o frame atual é exatamente o attack_7.png
        return int(self.atual) == self.frame_ataque_valido and self.animar



# grupo de sprites
todas_as_sprites = pygame.sprite.Group()


fruta = Fruta()
mosquito = Mosquito()
sapo = Sapo()


todas_as_sprites.add(fruta)
todas_as_sprites.add(mosquito)
todas_as_sprites.add(sapo)


imagem_fundo = pygame.image.load('fundos/fundo_ceu1.jpg')
imagem_fundo = pygame.transform.scale(imagem_fundo, (largura, altura))


relogio = pygame.time.Clock()


pontos = 0


# controle de tempo
tempo_limite = 60  # segundos
tempo_inicial = pygame.time.get_ticks()  # milissegundos
jogo_rodando = True
jogador_venceu = False


while True:
    relogio.tick(60)


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()


        if jogo_rodando:
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    sapo.atacar()


    if jogo_rodando:
        # cálculo do tempo decorrido em segundos
        tempo_atual_ms = pygame.time.get_ticks() - tempo_inicial
        tempo_segundos = tempo_atual_ms // 1000


        teclas = pygame.key.get_pressed()
        dx = 0
        dy = 0
        if teclas[K_LEFT]:
            dx = -1
        if teclas[K_RIGHT]:
            dx = 1
        if teclas[K_UP]:
            dy = -1
        if teclas[K_DOWN]:
            dy = 1
        sapo.mover(dx, dy)


        todas_as_sprites.update()


        # colisões só contam se estiver no frame attack_7
        if sapo.esta_no_frame_ataque():
            # fruta: perde 1 ponto
            if sapo.rect.colliderect(fruta.rect):
                pontos -= 1
                som_coleta.play()
                fruta.resetar_posicao()


            # mosquito: ganha 1 ponto
            if sapo.rect.colliderect(mosquito.rect):
                pontos += 1
                som_coleta.play()
                mosquito.resetar_posicao()


        # verifica condição de vitória
        if pontos >= 10 and tempo_segundos <= tempo_limite:
            jogo_rodando = False
            jogador_venceu = True


        # se o tempo acabou e ainda não venceu, apenas trava o jogo (pode tratar como derrota)
        if tempo_segundos >= tempo_limite and not jogador_venceu:
            jogo_rodando = False


        # desenho normal do jogo
        tela.fill((255, 255, 255))
        tela.blit(imagem_fundo, (0, 0))
        todas_as_sprites.draw(tela)


        # pontuação
        texto_pontos = fonte.render(f'Pontos: {pontos}', True, (0, 0, 0))
        tela.blit(texto_pontos, (10, 10))


        # tempo
        texto_tempo = fonte.render(f'Tempo: {tempo_segundos}s', True, (0, 0, 0))
        tela.blit(texto_tempo, (10, 40))


    else:
        # jogo parado: mostra tela de vitória ou derrota
        if jogador_venceu:
            pygame.mixer.music.stop()
            som_vitoria.play()
            tela.blit(imagem_vitoria, (0, 0))
        else:
            pygame.mixer.music.stop()
            som_game_over.play()
            tela.blit(imagem_derrota, (0, 0))
            '''
            texto_fim = fonte.render('Tempo esgotado!', True, (255, 0, 0))
            tela.blit(texto_fim, (largura // 2 - 100, altura // 2))
            '''
    

    pygame.display.flip()