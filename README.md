# 🕹️ Pacman Multiplayer com Python + Pygame + FastAPI

Este projeto é um jogo multiplayer inspirado no clássico **Pacman**, desenvolvido em Python. Ele utiliza **Pygame** no cliente para a interface gráfica e **FastAPI** com **WebSocket** no backend para comunicação em tempo real entre os jogadores.

> ✅ Ideal para aprendizado de multiplayer em tempo real com WebSocket, comunicação cliente-servidor e uso de Python moderno.

---

## 🧱 Estrutura do Projeto

```
pacman-python-pygame/
│
├── .devcontainer/           # Definição do ambiente DevContainer
│   └── devcontainer.json
│
├── client/                  # Código do cliente (Pygame)
│   ├── game_multiplayer.py
│   └── jogo_base.py
│
├── backend/                  # Código do servidor (FastAPI + WebSocket)
│   └── main.py
│
├── requirements.txt         # Dependências do projeto
├── README.md                # Este arquivo
└── .vscode/settings.json    # Configurações do VS Code (opcional)
```

---

## 🚀 Como Rodar Localmente com DevContainer

### ✅ Pré-requisitos

- [Docker](https://www.docker.com/)
- [Visual Studio Code](https://code.visualstudio.com/)
- Extensão [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) (ou Dev Containers)

---

### 📦 Primeira Execução

1. **Clone o projeto:**

```bash
git clone https://github.com/jacksonrodrigodev/pacman-python-pygame.git
cd pacman-python-pygame
```

2. **Abra no VS Code e clique em:**

```
><> Reopen in Container
```

3. O container será construído automaticamente, instalando:
   - Python 3.12
   - Pygame
   - FastAPI
   - Websockets
   - Uvicorn

---

## ▶️ Como Executar

### 🖥️ 1. Iniciar o Servidor FastAPI (WebSocket)

No terminal integrado (dentro do DevContainer):

```bash
cd server
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

> O servidor WebSocket estará disponível em `ws://localhost:8000/ws`

---

### 🧑‍🎮 2. Executar o Cliente (Jogo Pygame)

No terminal do DevContainer (ou qualquer outro bash com interface gráfica configurada):

```bash
cd client
python3 game_multiplayer.py
```

Para testar multiplayer, você pode abrir **vários terminais** e executar o cliente em cada um deles.

---

## 🎯 Como Jogar

- Use as **setas do teclado** para mover o Pacman.
- Cada jogador tem uma cor diferente.
- Os pontos são coletados ao passar por cima deles.
- A pontuação é **gerenciada e validada pelo servidor**.
- Todos os jogadores compartilham a mesma matriz (mapa).

---

## ⚙️ Arquivos DevContainer

### `.devcontainer/devcontainer.json` (exemplo)
```json
{
  "name": "Pacman Multiplayer",
  "dockerComposeFile": "../docker-compose.yml",
  "service": "backend",
  "workspaceFolder": "/workspace",
  "customizations": {
    "vscode": {
      "extensions": ["ms-python.python"]
    }
  },
  "forwardPorts": [8000]
}

```

### `.devcontainer/Dockerfile`
```dockerfile
FROM python:3.12

WORKDIR /workspace

COPY ../requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

CMD [ "bash" ]
```

---

## 📄 Requisitos (requirements.txt)

```text
pygame
fastapi
websockets
uvicorn
```

---

## ❓ Dúvidas Comuns

### 💻 O cliente precisa de interface gráfica?
Sim. O `pygame` exige que o terminal seja executado em ambiente com display X (Linux) ou com suporte gráfico. Se estiver no WSL, use `xming` ou `VcXsrv`.

### 🧩 Posso rodar o cliente fora do container?
Sim, desde que o Python e as dependências estejam instaladas. Basta rodar `python3 game_multiplayer.py` dentro da pasta `client`.

---

## 🛠️ Próximos Passos

- [ ] Criar sistema de salas (para multiplayer isolado)
- [ ] Mostrar nick dos jogadores
- [ ] Persistir scores em banco de dados
- [ ] Interface de início com login/nome
- [ ] Ranking de jogadores
- [ ] Sistema de Game Over
---

## 👨‍💻 Autor

Feito por [jacksonrodrigodev](https://github.com/jacksonrodrigodev)

---

## 🧾 Licença

MIT — use como quiser!