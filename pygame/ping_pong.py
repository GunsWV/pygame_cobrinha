import pygame #importando o bib pygame

pygame.init() #inicializando a bib pygame

largura, altura = 800, 600 #definindo a largura e a altura da tela

tela = pygame.display.set_mode((largura, altura)) #criado a tela
clock = pygame.time.Clock() #Criando o relógio

x = 50
y = 50 #pocição inicial

velocidade_x = 5 #velocidade da cobreinha eixo horizontal
velocidade_y = 5 #velocidade da cobreinha no eixo vertical

largura_ret, altura_ret = 50, 50 # largura e altura do retângulo (PIXELS)

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
    
    #taxa de atalização da fruta
    x += velocidade_x
    y += velocidade_y

    #invertendo a direção da fruta se ela atingir as bordas da tela
    if x + largura_ret > largura or x < 0:
        velocidade_x *= -1 
    if y + altura_ret > altura or y < 0:
        velocidade_y *= -1

    tela.fill((0, 0, 0)) # verde claro em RGB a tela
    pygame.draw.rect(tela, (255,20,147), (x, y, largura_ret, altura_ret))
    pygame.display.update()
    clock.tick(60)
pygame.quit()