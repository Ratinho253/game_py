import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Define o tamanho da tela
largura_tela, altura_tela = 640, 480
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Imagem de Fundo")

# Carrega a imagem de fundo
imagem_fundo = pygame.image.load("imagens/fundoTeste.png")  # Certifique-se de que o caminho da imagem esteja correto
imagem1 = pygame.image.load("imagens/maça.png")

# Redimensiona a imagem de fundo para preencher a tela
imagem_fundo = pygame.transform.scale(imagem_fundo, (largura_tela, altura_tela))

# Loop principal do programa
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Desenha a imagem de fundo na tela
    tela.blit(imagem_fundo, (0, 0))  # Desenha a imagem na posição (0, 0)

    # Desenhe outros conteúdos sobre o fundo aqui (opcional)
    # Por exemplo, desenhar um retângulo ou texto
    tela.blit(imagem1, (100,100))

    # Atualiza a tela
    pygame.display.flip()