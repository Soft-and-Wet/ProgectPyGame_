import sys

import pygame

from board import *
from units import *

pygame.init()

board = Board(board_width, board_height)
board.set_view(0, 0, cell_size)

# size = width, height = pygame.display.Info().current_w, pygame.display.Info().current_h  # получить размеры экрана
# screen = pygame.display.set_mode(size)
# print(width, height)

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

running = True
while running:
    screen.fill((0, 0, 255))
    for event in pygame.event.get():
        # закрытие на shift + esc
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE and pygame.key.get_mods() & pygame.KMOD_LSHIFT:
                running = False
                pygame.quit()
                sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.get_click(event.pos)
    screen.fill((0, 0, 0))
    board.render()
    pygame.display.flip()
