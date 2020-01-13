import pygame
import pygame.mixer


# инициализия музыки
pygame.mixer.init()

# фоновая музыка
m_main = pygame.mixer.music.load("")  # в кавычках: папка/нахвание

# другие звуки
m_other = pygame.mixer.Sound("")
# ...
