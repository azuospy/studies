#!/usr/bin/env python3

import os
import random
import time
import sys
import termios
import tty

# Dimensões do tabuleiro
board_width = 20
board_height = 10

# Representação dos elementos
snake_char = '#'
food_char = '*'
empty_char = ' '

# Direções possíveis
UP = 'w'
DOWN = 's'
LEFT = 'a'
RIGHT = 'd'

def create_board(width, height):
    return [[empty_char for _ in range(width)] for _ in range(height)]

def place_food(board):
    while True:
        x = random.randint(0, board_width - 1)
        y = random.randint(0, board_height - 1)
        if board[y][x] == empty_char:
            board[y][x] = food_char
            return x, y

def print_board(board):
    os.system('clear')  # Limpa a tela no Linux
    for row in board:
        print(''.join(row))
    print("Use 'WASD' para mover. Pressione 'q' para sair.")

def move_snake(snake, direction):
    head_x, head_y = snake[0]
    if direction == UP:
        new_head = (head_x, head_y - 1)
    elif direction == DOWN:
        new_head = (head_x, head_y + 1)
    elif direction == LEFT:
        new_head = (head_x - 1, head_y)
    elif direction == RIGHT:
        new_head = (head_x + 1, head_y)
    else:
        new_head = (head_x, head_y)

    # Verifica se a nova cabeça está fora dos limites
    if new_head[0] < 0 or new_head[0] >= board_width or new_head[1] < 0 or new_head[1] >= board_height:
        return None  # Retorna None para indicar colisão com a borda
    
    snake.insert(0, new_head)
    return snake

def check_collision(snake):
    head = snake[0]
    if head in snake[1:]:
        return True
    return False

def update_board(board, snake):
    # Limpa o tabuleiro
    for y in range(board_height):
        for x in range(board_width):
            if board[y][x] != food_char:
                board[y][x] = empty_char
    # Desenha a cobra
    for segment in snake:
        if 0 <= segment[1] < board_height and 0 <= segment[0] < board_width:  # Verifica os limites
            board[segment[1]][segment[0]] = snake_char

def get_keypress():
    """Captura uma tecla pressionada pelo usuário sem esperar por Enter"""
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1).lower()
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def main():
    board = create_board(board_width, board_height)
    snake = [(board_width // 2, board_height // 2)]
    food_x, food_y = place_food(board)
    direction = RIGHT
    game_over = False

    while not game_over:
        update_board(board, snake)
        print_board(board)

        if snake[0] == (food_x, food_y):
            food_x, food_y = place_food(board)
        else:
            snake.pop()  # Remove a cauda, exceto se tiver comido

        # Move a cobra e verifica se o movimento é válido
        moved_snake = move_snake(snake, direction)
        if moved_snake is None or check_collision(snake):
            game_over = True
        else:
            snake = moved_snake

        time.sleep(0.2)

        # Captura o input do usuário para Linux
        key = get_keypress()
        if key in [UP, DOWN, LEFT, RIGHT, 'q']:
            if key == 'q':
                break
            direction = key

    print("Fim de jogo! Pontuação: ", len(snake) - 1)

if __name__ == "__main__":
    main()

