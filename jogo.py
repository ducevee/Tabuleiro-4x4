import random
import time

def mostra_tabuleiro(tabuleiro):
    # Itera sobre cada linha do tabuleiro
    for linha in tabuleiro:
        # Divide visualmente cada casa do tabuleiro
        print(" | ".join(linha))
        print("-" * 14)
    print()

def coordenadas(): # Função para receber as coordenadas da jogada
    linha = int(input("Digite o número da linha (1 a 4): ")) - 1
    coluna = int(input("Digite o número da coluna (1 a 4): ")) - 1
    return linha, coluna

def realiza_jogada(tabuleiro, jogador, linha, coluna): # Função para realizar a jogada
    if tabuleiro[linha][coluna] == "-": # Verifica se a casa está vazia
        tabuleiro[linha][coluna] = jogador # Realiza a jogada
        return True # True para jogada válida
    else:
        return False # False para jogada inválida

def verifica_ganhador(tabuleiro):
    # Verificar linhas
    for linha in tabuleiro: # Itera sobre cada linha do tabuleiro
        if linha[0] == linha[1] == linha[2] == linha[3] != "-": # Verifica se há 4 casas iguais e não vazias
            return linha[0] # Retorna o jogador vencedor

    # Verificar colunas
    for coluna in range(4): # Itera sobre cada coluna do tabuleiro
        if tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna] == tabuleiro[3][coluna] != "-": # Verifica se há 4 casas iguais e não vazias
            return tabuleiro[0][coluna] # Retorna o jogador vencedor

    # Verificar diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == tabuleiro[3][3] != "-": # Verifica se há 4 casas iguais e não vazias na diagonal principal
        return tabuleiro[0][0] # Retorna o jogador vencedor
    if tabuleiro[0][3] == tabuleiro[1][2] == tabuleiro[2][1] == tabuleiro[3][0] != "-": # Verifica se há 4 casas iguais e não vazias na diagonal secundária
        return tabuleiro[0][3] # Retorna o jogador vencedor

    return None

def jogada_aleatoria(tabuleiro):
    jogadas_disponiveis = [] # cria uma lista para as possiveis jogadas
    for i in range(4): 
        for j in range(4):
            if tabuleiro[i][j] == "-":
                jogadas_disponiveis.append((i, j)) # adiciona as jogadas disponiveis na lista
    return random.choice(jogadas_disponiveis) # retorna uma jogada aleatoria disponivel da lista

def min(a, b):
    if a < b:
        return a
    return b

def max(a, b):
    if a > b:
        return a
    return b

def algoritmo_minimax(tabuleiro, jogador_atual, profundidade, jogador_max):
    """
    PARÂMETROS:
    tabuleiro:  [[][][][]...] Lita de listas que representa o estado atual do jogo;
    jogador_atual: {string} Que indica qual jogador deve jogar na jogada atual;
    profundidade: {int} que representa a profundidade máxima que o algoritmo deve explorar na árvore de jogadas.
    jogador_max: {string} que indica qual jogador é o jogador "max", isto é, o jogador que o algoritmo deve maximizar as chances de vitória.  
    """
    ganhador = verifica_ganhador(tabuleiro)
    # Avaliação Heurística
    if ganhador:
        return 1 if ganhador == jogador_max else -1 # se o jogador max vencer, retorna 1, se o jogador min vencer, retorna -1
    elif profundidade == 0:
        return 0 # se a profundidade for empate, retorna 0
    
    if jogador_atual == jogador_max: # se o jogador atual for o max
        melhor_valor = float("-inf") #  inicializa com um valor negativo infinito
        for i in range(4):
            for j in range(4):
                if tabuleiro[i][j] == "-":
                    tabuleiro[i][j] = jogador_atual # realiza a jogada
                    valor = algoritmo_minimax(tabuleiro, jogador_atual, profundidade - 1, jogador_max)  # para cada campo vazio, realiza uma jogada simulada, chamando o algoritmo minimax recursivamente
                    tabuleiro[i][j] = "-" # desfaz a jogada  para atualizar o tabuleiro entre o melhor valor e o valor
                    melhor_valor = max(melhor_valor, valor) # Faz a comparação e atualiza entre o melhor valor e o valor recebido
        return melhor_valor # retorna o melhor valor
    
    else:
        melhor_valor = float("inf") # caso contrário, inicializa com um valor positivo infinito
        for i in range(4):
            for j in range(4):
                if tabuleiro[i][j] == "-":
                    tabuleiro[i][j] = jogador_atual
                    valor = algoritmo_minimax(tabuleiro, jogador_atual, profundidade - 1, jogador_max) # chama o mesmo algoritmo, mas para o jogador min
                    tabuleiro[i][j] = "-"
                    melhor_valor = min(melhor_valor, valor) # Faz a comparação e atualiza entre o melhor valor e o valor recebido
        return melhor_valor # retorna o melhor valor
    
def jogada_minimax(tabuleiro, jogador): # jogada do minimax
    melhor_valor = float("-inf") # para garantir que o primeiro valor avaliado seja sempre maior que o valor inicial.
    melhor_jogada = None # melhor jogada recebe None, pois ainda não foi definida
    for i in range(4): 
        for j in range(4):
            if tabuleiro[i][j] == "-": 
                tabuleiro[i][j] = jogador
                valor = algoritmo_minimax(tabuleiro, jogador, 4, jogador) # chama a função minimax
                tabuleiro[i][j] = "-" # desfaz a jogada
                if valor > melhor_valor: # se o valor for maior que o melhor valor
                    melhor_valor = valor # melhor valor recebe o valor
                    melhor_jogada = (i, j) # melhor jogada recebe a jogada
    return melhor_jogada # retorna a melhor jogada

def algoritmo_alphabeta(tabuleiro, jogador, profundidade, alpha, beta, max_jogador): # ALGORITMO MINIMAX COM ALFA-BETA

    valor = float("-inf") if jogador == max_jogador else float("inf") # inicializa o valor com um valor negativo infinito se o jogador for o max, caso contrário, inicializa com um valor positivo infinito
    for i in range(4):
        for j in range(4):
            if tabuleiro[i][j] == "-":
                tabuleiro[i][j] = jogador
                if jogador == max_jogador:
                    valor = max(valor, algoritmo_alphabeta(tabuleiro, jogador, profundidade - 1, alpha, beta, max_jogador)) # diminui a profundidade em 1 e atualiza os valores de alpha e beta
                    alpha = max(alpha, valor) # valor é atualizado com o máximo entre o valor atual e o resultado da chamada recursiva
                    if alpha >= beta: 
                        tabuleiro[i][j] = "-"
                        return valor # Se alpha for maior ou igual a beta, ocorre a poda alfa-beta, e a função retorna o valor.
                else:
                    valor = min(valor, algoritmo_alphabeta(tabuleiro, jogador, profundidade - 1, alpha, beta, max_jogador)) # valor é atualizado com o mínimo entre o valor atual e o resultado da chamada recursiva
                    beta = min(beta, valor) # valor é atualizado com o mínimo entre o valor atual e o resultado da chamada recursiva
                    if alpha >= beta:
                        tabuleiro[i][j] = "-"
                        return valor # Se alpha for maior ou igual a beta, ocorre a poda alfa-beta, e a função retorna o valor.
                tabuleiro[i][j] = "-"
    return valor

def jogada_alphabeta(tabuleiro, jogador):
    melhor_valor = float("-inf") # para garantir que o primeiro valor avaliado seja sempre maior que o valor inicial.
    melhor_jogada = None # melhor jogada ainda não definida
    alpha = float("-inf") # 
    beta = float("inf") 
    for i in range(4):
        for j in range(4):
            if tabuleiro[i][j] == "-":
                tabuleiro[i][j] = jogador
                valor = algoritmo_alphabeta(tabuleiro, jogador, 4, alpha, beta, jogador) # passa o tabuleiro atualizado, o jogador atual com uma profundidade 4, os valores de alpha e beta e o jogador max
                tabuleiro[i][j] = "-"
                if valor > melhor_valor:
                    melhor_valor = valor # se for maior,atualiza o melhor valor com o valor atualizado 
                    melhor_jogada = (i, j) # atualiza a melhor jogada com a jogada atual

    return melhor_jogada # retorna a melhor jogada


def jogada_computadorVScomputador(tabuleiro, jogador, estrategia):
    if estrategia == "1":
        linha, coluna = random.choice([(i, j) for i in range(4) for j in range(4) if tabuleiro[i][j] == "-"])
    elif estrategia == "2":
        linha, coluna = jogada_minimax(tabuleiro, jogador)
    elif estrategia == "3":
        linha, coluna = jogada_alphabeta(tabuleiro, jogador)
    else:
        print("Estratégia inválida.")
        return

    jogada_valida = realiza_jogada(tabuleiro, jogador, linha, coluna)

    if not jogada_valida:
        print("Jogada inválida. Encerrando o jogo.")
        return

    ganhador = verifica_ganhador(tabuleiro)
    if ganhador:
        mostra_tabuleiro(tabuleiro)
        print("O jogador", ganhador, "venceu!")
        return

    return linha, coluna

import time
import random

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
    modo = input("1- Jogador X Jogador\n2 - Jogador X Computador\n3 - Computador X Computador\nEscolha o modo de jogo: ")
    if modo == "1":
        print()
        print('Modo Jogador X Jogador selecionado...')
        print()
        jogador_atual = jogadores[0]
    elif modo == "2":
        print()
        print('Modo Jogador X Computador selecionado...')
        print()
        estrategia = input("Estratégias Disponíveis para o raciocínio do Computador:\n1 - Aleatória\n2 - Minimax\n3 - Minimax com Alfa-beta\nESCOLHA A ESTRATÉGIA: ")
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
        print("Vez do jogador:", jogador_atual)
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
        print("Tempo da rodada:", tempo_rodada)
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
