import sys

import pygame

from board import *
from sprites import *

pygame.init()

board = Board(board_width, board_height)
board.set_view(0, 0, cell_size)

# size = width, height = pygame.display.Info().current_w, pygame.display.Info().current_h  # получить размеры экрана
# screen = pygame.display.set_mode(size)
# print(width, height)

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

running = True
move_r, move_l, move_u = False, False, False
move_d = True
hero = True

left_right_pose = True
hero_x = 100
hero_y = 100

while running:
    # all_sprites.draw(screen)

    screen.fill((0, 0, 0))
    board.render()
    all_sprites.draw(screen)

    for event in pygame.event.get():
        # закрытие на shift + esc
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE and pygame.key.get_mods() & pygame.KMOD_LSHIFT:
                running = False
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_a:
                move_l = True
                left_right_pose = False
            if event.key == pygame.K_d:
                move_r = True
                left_right_pose = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            board.get_click(event.pos)

        if event.type == pygame.KEYUP:
            move_r, move_l = False, False

    if move_r:
        hero_x += 5
    if move_l:
        hero_x -= 5

    if move_d:
        pass

    if hero:
        if left_right_pose:
            screen.blit(p_hero_1_look_right, (hero_x, hero_y))
        else:
            screen.blit(p_hero_1_look_left, (hero_x, hero_y))
        print((hero_x, hero_y))

    pygame.display.flip()
    clock.tick(fps)
    pygame.event.pump()
