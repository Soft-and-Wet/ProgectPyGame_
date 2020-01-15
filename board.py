import pygame

pygame.init()

from other import *
from sprites import *


# all_sprites = pygame.sprite.Group()


class Board:
    def __init__(self, board_width, board_height):
        # self.screen = screen
        self.k_n = True
        self.board_width = board_width
        self.board_height = board_height
        self.board = [[0] * board_width for _ in range(board_height)]
        print(self.board)
        self.left = 0
        self.top = 0

    def get_cell(self, mouse_pos):
        x, y = mouse_pos
        if self.top <= y <= self.top + self.cell_size * self.board_height and \
                self.left <= x <= self.left + self.cell_size * self.board_width:
            for i in range(self.board_height):
                if self.left + self.cell_size * i <= y <= self.left + self.cell_size * (i + 1):
                    y = i
                    break
            for j in range(self.board_width):
                if self.top + self.cell_size * j <= x <= self.top + self.cell_size * (j + 1):
                    x = j
                    break
            print("(", x, ", ", y, ")", sep="")
            return y, x
        else:
            print("None")
            return None

    def on_click(self, cell_coord):
        # x, y = cell_coord
        """if cell_coord is not None:
            # ...
            self.render()"""
        pass

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self):
        for i in range(self.board_height):
            for j in range(self.board_width):
                if self.board[i][j] == 0:
                    pygame.draw.rect(screen, pygame.Color("black"),
                                     (self.left + self.cell_size * j, self.top + self.cell_size * i,
                                      self.cell_size, self.cell_size))
                pygame.draw.rect(screen, pygame.Color("white"),
                                 (self.left + self.cell_size * j, self.top + self.cell_size * i,
                                  self.cell_size, self.cell_size), 1)
