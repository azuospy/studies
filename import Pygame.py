import Pygame
import sys
import numpy as np
 
# Inicializando Pygame
Pygame.init()
 
# Definindo cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
 
# Definindo o tamanho da tela
WIDTH = 300
HEIGHT = 300
LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE // 4
 
# Definindo a tela
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Jogo da Velha')
screen.fill(WHITE)
 
# Tabuleiro
board = np.zeros((BOARD_ROWS, BOARD_COLS))
 
# Função para desenhar as linhas do tabuleiro
def draw_lines():
  # Linhas horizontais
  pygame.draw.line(screen, BLACK, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
  pygame.draw.line(screen, BLACK, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)
 
  # Linhas verticais
  pygame.draw.line(screen, BLACK, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
  pygame.draw.line(screen, BLACK, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)
 
# Função para desenhar o X
def draw_x(row, col):
  start_desc = (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE)
  end_desc = (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE)
  pygame.draw.line(screen, RED, start_desc, end_desc, CROSS_WIDTH)
 
  start_asc = (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE)
  end_asc = (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE)
  pygame.draw.line(screen, RED, start_asc, end_asc, CROSS_WIDTH)
 
# Função para desenhar o O
def draw_o(row, col):
  center = (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2)
  pygame.draw.circle(screen, BLUE, center, CIRCLE_RADIUS, CIRCLE_WIDTH)
 
# Função para desenhar as figuras no tabuleiro
def draw_figures():
  for row in range(BOARD_ROWS):
    for col in range(BOARD_COLS):
      if board[row][col] == 1:
        draw_x(row, col)
      elif board[row][col] == 2:
        draw_o(row, col)
 
# Função para marcar uma célula no tabuleiro
def mark_square(row, col, player):
  board[row][col] = player
 
# Função para verificar se uma célula está vazia
def available_square(row, col):
  return board[row][col] == 0
 
# Função para verificar se o tabuleiro está cheio
def is_board_full():
  for row in range(BOARD_ROWS):
    for col in range(BOARD_COLS):
      if board[row][col] == 0:
        return False
  return True
 
# Função para verificar vitória
def check_win(player):
  # Checando as linhas
  for row in range(BOARD_ROWS):
    if board[row][0] == player and board[row][1] == player and board[row][2] == player:
      draw_win_line(row, 0, row, 2)
      return True
 
  # Checando as colunas
  for col in range(BOARD_COLS):
    if board[0][col] == player and board[1][col] == player and board[2][col] == player:
      draw_win_line(0, col, 2, col)
      return True
 
  # Checando as diagonais
  if board[0][0] == player and board[1][1] == player and board[2][2] == player:
    draw_win_line(0, 0, 2, 2)
    return True
 
  if board[2][0] == player and board[1][1] == player and board[0][2] == player:
    draw_win_line(2, 0, 0, 2)
    return True
 
  return False
 
# Função para desenhar a linha de vitória
def draw_win_line(row1, col1, row2, col2):
  start_pos = (col1 * SQUARE_SIZE + SQUARE_SIZE // 2, row1 * SQUARE_SIZE + SQUARE_SIZE // 2)
  end_pos = (col2 * SQUARE_SIZE + SQUARE_SIZE // 2, row2 * SQUARE_SIZE + SQUARE_SIZE // 2)
  pygame.draw.line(screen, BLACK, start_pos, end_pos, LINE_WIDTH)
 
# Função para reiniciar o jogo
def restart():
  screen.fill(WHITE)
  draw_lines()
  for row in range(BOARD_ROWS):
    for col in range(BOARD_COLS):
      board[row][col] = 0
 
# Desenhando as linhas do tabuleiro ao iniciar o jogo
draw_lines()
 
# Loop principal do jogo
player = 1
game_over = False
 
while True:
  for event in Pygame.event.get():
    if event.type == Pygame.QUIT:
      Pygame.quit()
      sys.exit()
 
    if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
      mouseX = event.pos[0]  # X
      mouseY = event.pos[1]  # Y
 
      clicked_row = mouseY // SQUARE_SIZE
      clicked_col = mouseX // SQUARE_SIZE
 
      if available_square(clicked_row, clicked_col):
        mark_square(clicked_row, clicked_col, player)
        if check_win(player):
          game_over = True
        player = 2 if player == 1 else 1
        draw_figures()
 
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_r:
        restart()
        player = 1
        game_over = False
 
  pygame.display.update()