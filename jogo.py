import random
import time

def mostra_tabuleiro(tabuleiro):
    # Itera sobre cada linha do tabuleiro
    for linha in tabuleiro:
        # Divide visualmente cada casa do tabuleiro
        print(" | ".join(linha))
        print("-" * 14)
    print()

def coordenadas():
    linha = int(input("Digite o número da linha (1 a 4): ")) - 1
    coluna = int(input("Digite o número da coluna (1 a 4): ")) - 1
    return linha, coluna

def realiza_jogada(tabuleiro, jogador, linha, coluna):
    if tabuleiro[linha][coluna] == "-":
        tabuleiro[linha][coluna] = jogador
        return True
    else:
        return False

def verifica_ganhador(tabuleiro):
    
    # Verificar linhas
    for linha in tabuleiro:
        if linha[0] == linha[1] == linha[2] == linha[3] != "-":
            return linha[0]

    # Verificar colunas
    for coluna in range(4):
        if tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna] == tabuleiro[3][coluna] != "-":
            return tabuleiro[0][coluna]

    # Verificar diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == tabuleiro[3][3] != "-":
        return tabuleiro[0][0]
    if tabuleiro[0][3] == tabuleiro[1][2] == tabuleiro[2][1] == tabuleiro[3][0] != "-":
        return tabuleiro[0][3]

    return None

def jogada_aleatoria(tabuleiro):
    jogadas_disponiveis = [] # cria uma lista para as possiveis jogadas
    for i in range(4): 
        for j in range(4):
            if tabuleiro[i][j] == "-":
                jogadas_disponiveis.append((i, j)) # adiciona as jogadas disponiveis na lista
    return random.choice(jogadas_disponiveis) # retorna uma jogada aleatoria disponivel da lista

def minimax(tabuleiro, jogador, profundidade, max_jogador): # ALGORITMO MINIMAX
    ganhador = verifica_ganhador(tabuleiro)
    # avaliação heruística para determinar qual a melhor jogada
    if ganhador:
        if ganhador == max_jogador:
            return 1
        else:
            return -1
    elif profundidade == 0:
        return 0
    
    if jogador == max_jogador:
        melhor_valor = float("-inf")
        for i in range(4):
            for j in range(4):
                if tabuleiro[i][j] == "-":
                    tabuleiro[i][j] = jogador
                    valor = minimax(tabuleiro, jogador, profundidade - 1, max_jogador)
                    tabuleiro[i][j] = "-"
                    melhor_valor = max(melhor_valor, valor)
        return melhor_valor
    else:
        melhor_valor = float("inf")
        for i in range(4):
            for j in range(4):
                if tabuleiro[i][j] == "-":
                    tabuleiro[i][j] = jogador
                    valor = minimax(tabuleiro, jogador, profundidade - 1, max_jogador)
                    tabuleiro[i][j] = "-"
                    melhor_valor = min(melhor_valor, valor)
        return melhor_valor

def jogada_minimax(tabuleiro, jogador):
    melhor_valor = float("-inf")
    melhor_jogada = None
    for i in range(4):
        for j in range(4):
            if tabuleiro[i][j] == "-":
                tabuleiro[i][j] = jogador
                valor = minimax(tabuleiro, jogador, 4, jogador)
                tabuleiro[i][j] = "-"
                if valor > melhor_valor:
                    melhor_valor = valor
                    melhor_jogada = (i, j)
    return melhor_jogada

def jogada_alphabeta(tabuleiro, jogador):
    def alphabeta(tabuleiro, jogador, profundidade, alpha, beta, max_jogador):
        ganhador = verifica_ganhador(tabuleiro)
        if ganhador:
            if ganhador == max_jogador:
                return 1
            else:
                return -1
        elif profundidade == 0:
            return 0

        if jogador == max_jogador:
            valor = float("-inf")
            for i in range(4):
                for j in range(4):
                    if tabuleiro[i][j] == "-":
                        tabuleiro[i][j] = jogador
                        valor = max(valor, alphabeta(tabuleiro, jogador, profundidade - 1, alpha, beta, max_jogador))
                        tabuleiro[i][j] = "-"
                        alpha = max(alpha, valor)
                        if alpha >= beta:
                            break
            return valor
        else:
            valor = float("inf")
            for i in range(4):
                for j in range(4):
                    if tabuleiro[i][j] == "-":
                        tabuleiro[i][j] = jogador
                        valor = min(valor, alphabeta(tabuleiro, jogador, profundidade - 1, alpha, beta, max_jogador))
                        tabuleiro[i][j] = "-"
                        beta = min(beta, valor)
                        if alpha >= beta:
                            break
            return valor

    melhor_valor = float("-inf")
    melhor_jogada = None
    alpha = float("-inf")
    beta = float("inf")
    for i in range(4):
        for j in range(4):
            if tabuleiro[i][j] == "-":
                tabuleiro[i][j] = jogador
                valor = alphabeta(tabuleiro, jogador, 4, alpha, beta, jogador)
                tabuleiro[i][j] = "-"
                if valor > melhor_valor:
                    melhor_valor = valor
                    melhor_jogada = (i, j)
    return melhor_jogada


def jogar():
    tabuleiro = [["-" for _ in range(4)] for _ in range(4)]
    jogadores = ["X", "O"]
    print('-' * 30)
    print("Bem-vindo ao jogo da velha 4x4!")
    print('-' * 30)
    print()
    time.sleep(1)
    print('Modos de jogo:')
    print()
    modo = input("1- Jogador vs Jogador\n2 - Jogador vs Computador\nEscolha o modo de jogo:")
    if modo == "1":
        jogador_atual = jogadores[0]
    elif modo == "2":
        print()
        print('Boa escolha...')
        print()
        estrategia = input("Estratégias Disponíveis para o racíocinio do Computador:\n1 - Aleatória\n2 - Minimax\n3 - Minimax com Alfa-beta\nEscolha a estratégia do Computador: ")
        jogador_atual = random.choice(jogadores)
    else:
        print("Modo inválido. Encerrando o jogo.")
        return
    print()
    jogada = 1  # Número da jogada

    while True:
        print('Estado atual do tabuleiro:')
        print()
        mostra_tabuleiro(tabuleiro)
        print('-' * 14)
        print(jogada, "ª rodada")  # Número da jogada
        print("Vez do jogador: ", jogador_atual)
        print()
        time.sleep(1)
        print()
        start_time = time.time()  # Tempo inicial da jogada

        if jogador_atual == "X" or (jogador_atual == "O" and modo == "1"):
            linha, coluna = coordenadas()
            jogada_valida = realiza_jogada(tabuleiro, jogador_atual, linha, coluna)
        else:
            if estrategia == "1":
                linha, coluna = jogada_aleatoria(tabuleiro)
            elif estrategia == "2":
                linha, coluna = jogada_minimax(tabuleiro, jogador_atual)
            elif estrategia == "3":
                linha, coluna = jogada_alphabeta(tabuleiro, jogador_atual)
            else:
                print("Estratégia inválida. Encerrando o jogo.")
                return

            jogada_valida = realiza_jogada(tabuleiro, jogador_atual, linha, coluna)

        end_time = time.time()  # Tempo final da jogada

        print()
        tempo_rodada = end_time - start_time
        print("Tempo da rodada: ", tempo_rodada)
        print()
        print('-' * 14)
        if not jogada_valida:
            print('!' * 14)
            print()
            print("Jogada inválida. Tente novamente.")
            print()
            print('!' * 14)
            continue

        ganhador = verifica_ganhador(tabuleiro)
        if ganhador:
            mostra_tabuleiro(tabuleiro)
            print("O jogador", ganhador, "venceu!")
            break

        if jogador_atual == "X":
            jogador_atual = "O"
        else:
            jogador_atual = "X"

        jogada += 1  # Incrementa o número da jogada

jogar()
