import sys

import pygame


pygame.init()

# size = width, height = pygame.display.Info().current_w, pygame.display.Info().current_h  # получить размеры экрана
# screen = pygame.display.set_mode(size)
# print(width, height)
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# python -m pygame.examples.eventlist  #штука
# #C:\Users\User\PycharmProjects\ProgectPyGame\venv\lib\site-packages\pygame\examples\__init__.py

running = True
while running:
    screen.fill((0, 0, 255))
    for event in pygame.event.get():
        """if event.type == pygame.QUIT:
            running = False
            # pygame.quit()
            # sys.exit()"""
        # закрытие на shift + esc
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE and pygame.key.get_mods() & pygame.KMOD_LSHIFT:
                running = False
                pygame.quit()
                sys.exit()
