import pygame
import pygame.mixer


# инициализия музыки
pygame.mixer.init()

# фоновая музыка
pygame.mixer.music.load("music/John Williams - Star Wars Main Theme.mp3")  # в кавычках: папка/название
m_game = pygame.mixer.Sound("music/Order-66.wav")
