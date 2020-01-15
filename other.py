import pygame


# поле
# поле: 20 в ширину на 40 в высоту, видимая на акране часть: около 15-19 на 10 - 12 (в зависимости от разрешения экрана)
#
# требуется в дальнейшем реализовать камеру (я думаю, песонаж должен быть чуть ниже центра)

board_width = 40
board_height = 25
cell_size = 40

# инициализация времени
clock = pygame.time.Clock()

# создание окна
screen = pygame.display.set_mode()
# screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
# pygame.display.set_caption("")  # имя
