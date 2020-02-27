from pygame.sprite import Sprite, collide_rect
from pygame import Surface
import pygame


class StatusBar():
    def __init__(self):
        self.maxHealth = 100
        self.maxForce = 100
        self.health = self.maxHealth
        self.force = self.maxForce
        self.bars = pygame.Surface((680, 120))
        self.imageOfHealth = Surface((680, 40))
        self.imageOfHealth.fill((255, 0, 0))
        self.imageOfForce = Surface((680, 40))
        self.imageOfForce.fill((0, 0, 255))
        self.coord = (40, 640)

    def draw(self, surface):
        surface.blit(self.imageOfHealth, self.coord)
