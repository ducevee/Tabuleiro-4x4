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