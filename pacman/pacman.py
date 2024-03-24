import pygame

AMARELO = (255,255,0)
PRETO = (0,0,0)
LARGURA_TELA = 600
ALTURA_TELA = 480
RUNNING = True
RAIO = 30
x = 10
y = 10
velocidade = 0.1
vel_x = velocidade
vel_y = velocidade
pygame.init()

tela = pygame.display.set_mode((LARGURA_TELA,ALTURA_TELA),0)

while RUNNING:
    #Calcular as regras 
    x = x  + vel_x
    y = y + vel_y
    if x + RAIO > LARGURA_TELA:
        vel_x = -velocidade
    if x - RAIO < 0:
        vel_x = velocidade
    if y + RAIO > ALTURA_TELA:
        vel_y = -velocidade
    if y - RAIO < 0:
        vel_y = velocidade
    #Pintar 
    tela.fill(PRETO)
    pygame.draw.circle(tela, AMARELO, (int(x),int(y)), RAIO, 0)
    pygame.display.update()
    #Evento
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()