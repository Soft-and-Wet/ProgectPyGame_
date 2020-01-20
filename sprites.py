# коммент чтобы был
import os

import pygame

from other import *


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert_alpha()
    return image


all_sprites = pygame.sprite.Group()
"""
# создадим спрайт
sprite = pygame.sprite.Sprite()
# определим его вид
sprite.image = load_image("bomb.png")
# и размеры
sprite.rect = sprite.image.get_rect()
# добавим спрайт в группу
all_sprites.add(sprite)"""
""""""
p_wall_image = pygame.transform.scale(load_image("p_wall.png"), (cell_size, cell_size))
p_not_wall_image = pygame.transform.scale(load_image("p_not_wall.png"), (cell_size, cell_size))

p_hero_1_look_right = pygame.transform.scale(load_image("p_hero_1_look_right.png"), (cell_size, cell_size))
p_hero_1_look_right.set_colorkey(p_hero_1_look_right.get_at((0, 0)))
p_hero_1_look_left = pygame.transform.scale(load_image("p_hero_1_look_left.png"), (cell_size, cell_size))
p_hero_1_look_left.set_colorkey(p_hero_1_look_left.get_at((0, 0)))


for i in range(board_height):
    for j in range(board_width):
        if i == 0 or i == board_height - 1 or j == 0 or j == board_width - 1:
            wall = pygame.sprite.Sprite(all_sprites)
            wall.image = p_wall_image
            wall.rect = wall.image.get_rect()

            wall.rect.x = j * cell_size
            wall.rect.y = i * cell_size
        else:
            not_wall = pygame.sprite.Sprite(all_sprites)
            not_wall.image = p_not_wall_image
            not_wall.rect = not_wall.image.get_rect()

            not_wall.rect.x = j * cell_size
            not_wall.rect.y = i * cell_size
