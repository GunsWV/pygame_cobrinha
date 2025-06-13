import pygame
pygame.init() #inicia o pygame

largura = 800 #Define a largura
altura = 600 #Define a altura da tela

tela = pygame.display.set_mode((largura, altura)) #Cria a tela em dimensões especificas
pygame.display.set_caption('Exemplo de jogo') #Define o titulo da janela
rodando = True #variavel para controlar o joop principal
while rodando: #loop principal do jogo
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    tela.fill((255,255,255)) #preenche a tela
    pygame.display.update() #atualiza a tela

pygame.quit()  #encerrando a tela