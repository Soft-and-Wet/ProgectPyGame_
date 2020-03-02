from pygame.sprite import Sprite, collide_rect
from pygame import Surface
import pygame


class StatusBar():
    def __init__(self):
        self.bars = pygame.Surface((680, 120))
        self.health = 100
        self.force = 100
        self.coord = (40, 640)

    def draw(self, surface):
        self.bars.fill((0, 0, 0))
        pygame.draw.rect(self.bars, (255, 0, 0), (0, 0, 680 * self.health / 100, 40))
        pygame.draw.rect(self.bars, (0, 0, 255), (0, 80, 680 * self.force / 100, 40))
        surface.blit(self.bars, self.coord)

    def update(self, health, force):
        self.health = health
        self.force = force