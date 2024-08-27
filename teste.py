import pygame
import random
import sys

pygame.init()

pygame.display.set_caption("Jogo Snake Python")

largura, altura = 640, 480

tela = pygame.display.set_mode((largura, altura))

relogio = pygame.time.Clock()

imagem_fundo = pygame.image.load("imagens/fundoTeste.png")
imagem_fundo = pygame.transform.scale(imagem_fundo, (largura, altura))

# Cores RGB
preta = (0, 0, 0)
branca = (255, 255, 255)
vermelha = (255, 0, 0)
verde = (0, 255, 0)
cor_borda = (255, 255, 255)  # Cor da borda (amarelo)
espessura_borda = 20  # Espessura da borda

# Parâmetros da cobrinha
tamanho_quadrado = 20
velocidade_jogo = 10

# Carrega a imagem da cobra
imagem_cobra = pygame.image.load("imagens/file.png")  # Substitua pelo caminho da sua imagem
imagem_cobra = pygame.transform.scale(imagem_cobra, (tamanho_quadrado, tamanho_quadrado))

def gerar_comida():
    comida_x = round(random.randrange(espessura_borda, largura - espessura_borda - tamanho_quadrado) / float(tamanho_quadrado)) * float(tamanho_quadrado)
    comida_y = round(random.randrange(espessura_borda, altura - espessura_borda - tamanho_quadrado) / float(tamanho_quadrado)) * float(tamanho_quadrado)
    return comida_x, comida_y

def desenhar_comida(tamanho, comida_x, comida_y):
    imagem_comida = pygame.image.load("imagens/maça.png")
    imagem_comida = pygame.transform.scale(imagem_comida, (tamanho, tamanho))
    tela.blit(imagem_comida, (comida_x, comida_y))

def desenhar_cobra(imagem_cobra, segmentos):
    for segmento in segmentos:
        tela.blit(imagem_cobra, (segmento[0], segmento[1]))

def desenhar_pontuacao(pontuacao):
    fonte = pygame.font.SysFont("Helvetica", 15)
    texto = fonte.render(f"Pontos: {pontuacao}", True, preta)
    tela.blit(texto, [10, 4])  # Posiciona a pontuação na borda superior, acima da borda amarela

def desenhar_borda():
    pygame.draw.rect(tela, cor_borda, [0, 0, largura, espessura_borda])  # Topo
    pygame.draw.rect(tela, cor_borda, [0, altura - espessura_borda, largura, espessura_borda])  # Base
    pygame.draw.rect(tela, cor_borda, [0, 0, espessura_borda, altura])  # Esquerda
    pygame.draw.rect(tela, cor_borda, [largura - espessura_borda, 0, espessura_borda, altura])  # Direita

def selecionar_velocidade(tecla):
    if tecla == pygame.K_DOWN:
        velocidade_x = 0
        velocidade_y = tamanho_quadrado
    elif tecla == pygame.K_UP:
        velocidade_x = 0
        velocidade_y = -tamanho_quadrado
    elif tecla == pygame.K_RIGHT:
        velocidade_x = tamanho_quadrado
        velocidade_y = 0
    elif tecla == pygame.K_LEFT:
        velocidade_x = -tamanho_quadrado
        velocidade_y = 0
    return velocidade_x, velocidade_y

def rodar_jogo():
    fim_jogo = False
    x = largura / 2
    y = altura / 2
    velocidade_x = 0
    velocidade_y = 0
    tamanho_cobra = 1
    segmentos_cobra = []
    comida_x, comida_y = gerar_comida()

    while not fim_jogo:
        tela.blit(imagem_fundo, (0,0))

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                velocidade_x, velocidade_y = selecionar_velocidade(evento.key)
        
        # Atualiza a posição da cobra
        x += velocidade_x
        y += velocidade_y
        nova_cabeca = [x, y]
        segmentos_cobra.append(nova_cabeca)

        if len(segmentos_cobra) > tamanho_cobra:
            del segmentos_cobra[0]

        # Verifica colisão com a comida
        if x == comida_x and y == comida_y:
            tamanho_cobra += 1
            comida_x, comida_y = gerar_comida()

        # Verifica colisão com as bordas da tela (considerando a espessura da borda) ou com o próprio corpo
        if (
            x < espessura_borda or x >= largura - espessura_borda or
            y < espessura_borda or y >= altura - espessura_borda or
            nova_cabeca in segmentos_cobra[:-1]
        ):
            fim_jogo = rodar_jogo()

        # Desenha a comida
        desenhar_comida(tamanho_quadrado, comida_x, comida_y)

        # Desenha a cobra
        desenhar_cobra(imagem_cobra, segmentos_cobra)

        # Desenha a borda
        desenhar_borda()

        # Desenha a pontuação por cima da borda
        desenhar_pontuacao(tamanho_cobra - 1)

        # Atualiza a tela
        pygame.display.update()

        # Controla a taxa de quadros
        relogio.tick(velocidade_jogo)

rodar_jogo()
pygame.quit()
sys.exit()