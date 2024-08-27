import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Define o tamanho da tela
largura_tela, altura_tela = 640, 480
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Desenhando Cobra com Imagem")

# Cores
branca = (255, 255, 255)

# Carrega a imagem da cobra
imagem_cobra = pygame.image.load("imagens/file.png")  # Substitua pelo caminho da sua imagem

# Define o tamanho da imagem
tamanho = 20  # O tamanho da imagem deve corresponder ao tamanho que você quer para cada 'pixel' da cobra

# Redimensiona a imagem, se necessário
imagem_cobra = pygame.transform.scale(imagem_cobra, (tamanho, tamanho))

def desenhar_cobra(tamanho, pixels):
    for pixel in pixels:
        tela.blit(imagem_cobra, (pixel[0], pixel[1]))  # Desenha a imagem na posição (pixel[0], pixel[1])

# Lista de posições para a cobra
pixels = [(10, 100), (120, 100), (140, 100)]  # Exemplo de posições

# Loop principal do programa
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Preenche o fundo da tela
    tela.fill((0, 0, 0))  # Cor de fundo preta

    # Desenha a cobra na tela
    desenhar_cobra(tamanho, pixels)

    # Atualiza a tela
    pygame.display.flip()
