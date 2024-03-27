import pygame

AMARELO = (255,255,0)
PRETO = (0,0,0)
LARGURA_TELA = 800
ALTURA_TELA = 600
RUNNING = True
pygame.init()

tela = pygame.display.set_mode((LARGURA_TELA,ALTURA_TELA),0)

class Pacman:
    def __init__(self):
        self.coluna = 1
        self.linha = 1
        self.centro_x = 400
        self.centro_y = 300
        self.vel_x = 1
        self.vel_y = 1
        self.tamanho = LARGURA_TELA // 30
        self.raio = int(self.tamanho / 2)

    def calcular_regras(self):
        self.coluna = self.coluna + self.vel_x
        self.linha = self.linha + self.vel_y
        self.centro_x = int(self.coluna * self.tamanho + self.raio)
        self.centro_y = int(self.linha * self.tamanho + self.raio)

        if (self.centro_x + self.raio) > LARGURA_TELA:
            self.vel_x = -self.vel_x
        if (self.centro_x - self.raio) < 0:
            self.vel_x = abs(self.vel_x)
        if (self.centro_y + self.raio) > ALTURA_TELA:
            self.vel_y = -self.vel_y
        if (self.centro_y - self.raio) < 0:
            self.vel_y = abs(self.vel_y)
        

    def pintar(self, tela):
        #Desenha corpo pacman
        pygame.draw.circle(tela,AMARELO,(self.centro_x,self.centro_y),self.raio,0)
        
        #Desenho boca pacman
        canto_boca = (self.centro_x,self.centro_y)
        labio_superior = (self.centro_x + self.raio, self.centro_y - self.raio)
        labio_inferior = (self.centro_x + self.raio, self.centro_y)
        pontos = [canto_boca,labio_superior,labio_inferior]
        pygame.draw.polygon(tela,PRETO,pontos,0)

        #desenha olho pacman
        olho_x = int(self.centro_x + self.raio / 3)
        olho_y = int(self.centro_y - self.raio * 0.70)
        olho_raio = int(self.raio / 10)
        pygame.draw.circle(tela,PRETO,(olho_x,olho_y), olho_raio,0)

if __name__ == "__main__":
    pacman = Pacman()
    while RUNNING:
        #Calcular regras
        pacman.calcular_regras()
        #Pintar tela
        tela.fill(PRETO)
        pacman.pintar(tela)
        pygame.display.update()
        pygame.time.delay(100)

        #Capturar os evento
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()