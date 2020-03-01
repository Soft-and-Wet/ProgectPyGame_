from pygame.sprite import Sprite, collide_rect
import pygame


class BallOfHealth(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = pygame.image.load('images/health.png').convert()
        self.image.set_colorkey(self.image.get_at((0, 0)))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def update(self, hero):
        if collide_rect(self, hero):
            self.kill()
            hero.health += 30


class BallOfForce(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = pygame.image.load('images/force.png').convert()
        self.image.set_colorkey(self.image.get_at((0, 0)))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def update(self, hero):
        if collide_rect(self, hero):
            self.kill()
            hero.force += 30


class Storage(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = pygame.image.load('images/decor/box.png').convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def update(self, shots, buffs):
        for shot in shots:
            if collide_rect(self, shot):
                buff = BallOfForce(self.rect.x, self.rect.y)
                buff.add(buffs)
                self.kill()
                shot.kill()
