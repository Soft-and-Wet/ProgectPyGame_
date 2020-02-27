from pygame.sprite import Sprite
from pygame import Surface
import pygame
from pygame import *


class BallOfHealth(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = pygame.image.load('images/items/health.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))


screen = pygame.Surface((100, 100))
running = True
s = BallOfHealth(0, 0)
s.draw(screen)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        pygame.display.flip()
