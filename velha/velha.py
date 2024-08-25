#!/usr/bin/env python3

def print_board(board):
    
    """Imprime o tabuleiro do jogo da velha com arte ASCII."""
    
    print("   A   B   C")
    
    print("  ┌───┬───┬───┐")  # Linha horizontal superior

    for i, row in enumerate(board):
        
        row_display = f"{i + 1} │ " + " │ ".join(row) + " │"
        print(row_display)
        
        if i < 2:  # Adiciona a linha horizontal após cada linha do tabuleiro, exceto a última
            print("  ├───┼───┼───┤")
    print("  └───┴───┴───┘")  # Linha horizontal inferior

def check_winner(board):
    
    """Verifica se há um vencedor."""
    
    # Verifica linhas
    
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return True
    
    # Verifica colunas
    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return True
    
    # Verifica diagonais
    
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return True
    return False

def check_draw(board):
    
    """Verifica se o jogo terminou em empate."""
    
    for row in board:
        if ' ' in row:
            return False
    return True

def main():
    
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        
        print_board(board)
        print(f"\nJogador {current_player}, escolha sua jogada (letra da coluna e número da linha, por exemplo A1): ")
        
        try:
            entrada = input().replace(" ", "")
            col_letter = entrada[0].upper()  # Primeira letra é a coluna
            row = int(entrada[1:]) - 1  # O restante é a linha, ajusta para índice base 0
            col = ord(col_letter) - ord('A')
        except (ValueError, IndexError):
            print("Entrada inválida! Use uma letra de A a C para a coluna e um número de 1 a 3 para a linha.")
            continue

        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Entrada inválida! Escolha uma letra de A a C para a coluna e um número de 1 a 3 para a linha.")
            continue

        if board[row][col] != ' ':
            print("Essa posição já está ocupada! Tente novamente.")
            continue

        board[row][col] = current_player

        if check_winner(board):
            print_board(board)
            print(f"Parabéns, Jogador {current_player}! Você venceu!")
            break

        if check_draw(board):
            print_board(board)
            print("O jogo terminou em empate!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    main()

