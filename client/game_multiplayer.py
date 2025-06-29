import pygame
import asyncio
import websockets
import threading
import json
import uuid
import os
from jogo_base import Cenario, Pacman, ALTURA_TELA, LARGURA_TELA, PRETO


def gerar_id():
    return uuid.uuid4().hex


player_id = gerar_id()
pacman = Pacman(ALTURA_TELA // 30)
cenario = Cenario(ALTURA_TELA // 30, pacman)
jogadores_remotos = {}
VERMELHO = (255, 0, 0)


async def comunicar():
    uri = "ws://localhost:8000/ws"
    while True:
        try:
            async with websockets.connect(uri, ping_interval=10, ping_timeout=30) as ws:
                print(f"[CLIENTE] Conectado ao servidor com ID {player_id}")

                dados_iniciais = {
                    "tipo": "movimento",
                    "id": player_id,
                    "linha": pacman.linha,
                    "coluna": pacman.coluna,
                }
                await ws.send(json.dumps(dados_iniciais))

                async def envia_loop():
                    while True:
                        dados = {
                            "tipo": "movimento",
                            "id": player_id,
                            "linha": pacman.linha,
                            "coluna": pacman.coluna,
                        }
                        await ws.send(json.dumps(dados))
                        await asyncio.sleep(0.05)

                asyncio.create_task(envia_loop())

                while True:
                    msg = await ws.recv()
                    dados = json.loads(msg)

                    if dados.get("tipo") == "erro":
                        print(f"[ERRO DO SERVIDOR] {dados.get('mensagem')}")
                        pygame.quit()
                        os._exit(0)

                    if dados["tipo"] == "estado_matriz":
                        cenario.matriz = dados["matriz"]

                    elif dados["tipo"] == "estado_jogo":
                        cenario.matriz = dados["matriz"]
                        jogador_id = dados["jogador_id"]
                        if jogador_id == player_id:
                            cenario.pontos = dados["pontos"]
                        else:
                            jogadores_remotos[jogador_id] = (
                                dados["coluna"],
                                dados["linha"],
                            )
                    elif dados["tipo"] == "jogador_saiu":
                        jogador_id = dados["jogador_id"]
                        if jogador_id in jogadores_remotos:
                            jogadores_remotos.pop(jogador_id)
                            print(f"[INFO] Jogador {jogador_id} saiu do jogo.")

        except Exception as e:
            print(f"[CLIENTE] Erro: {e}, tentando reconectar...")
            await asyncio.sleep(1)


def iniciar_rede():
    threading.Thread(target=lambda: asyncio.run(comunicar()), daemon=True).start()


pygame.init()
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA), 0)
pygame.display.set_caption("Pacman Multiplayer Online")

clock = pygame.time.Clock()
iniciar_rede()

while not cenario.matriz:
    print("[INFO] Aguardando matriz do servidor...")
    pygame.time.delay(100)

while True:
    pacman.calcular_regras()
    linha = pacman.linha_intensao
    coluna = pacman.coluna_intensao
    linhas_mapa = len(cenario.matriz)
    colunas_mapa = len(cenario.matriz[0])

    if 0 <= linha < linhas_mapa and 0 <= coluna < colunas_mapa:
        if cenario.matriz[linha][coluna] != 2:
            pacman.aceitar_movimento()

    tela.fill(PRETO)
    cenario.pintar(tela)
    pacman.pintar(tela)

    # Desenhar jogadores remotos
    for _, (col, lin) in jogadores_remotos.items():
        centro_x = int(col * pacman.tamanho + pacman.raio)
        centro_y = int(lin * pacman.tamanho + pacman.raio)
        raio = pacman.raio

        # Corpo do jogador remoto
        pygame.draw.circle(tela, VERMELHO, (centro_x, centro_y), raio)
        pygame.draw.circle(tela, (0, 0, 0), (centro_x, centro_y), raio, 1)

        # Boca do jogador remoto
        canto_boca = (centro_x, centro_y)
        labio_superior = (centro_x + raio, centro_y - raio)
        labio_inferior = (centro_x + raio, centro_y)
        pontos = [canto_boca, labio_superior, labio_inferior]
        pygame.draw.polygon(tela, PRETO, pontos)

        # Olho do jogador remoto
        olho_x = int(centro_x + raio / 3)
        olho_y = int(centro_y - raio * 0.7)
        olho_raio = int(raio / 10)
        pygame.draw.circle(tela, PRETO, (olho_x, olho_y), olho_raio)

    pygame.display.update()
    pygame.time.delay(50)

    eventos = pygame.event.get()
    for e in eventos:
        if e.type == pygame.QUIT:
            pygame.quit()
            os._exit(0)
    pacman.processar_eventos(eventos)
