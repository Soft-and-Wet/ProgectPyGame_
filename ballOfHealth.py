from pygame.sprite import Sprite
from pygame import Surface
import pygame


class Blok(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = pygame.image.load('images/health')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))