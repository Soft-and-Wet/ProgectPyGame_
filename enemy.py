from pygame.sprite import Sprite, collide_rect
from pygame import Surface, time
from defs import *
from bullet import Bullet

SPEED = 4
GRAVITY = 0.4


class Enemy(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.speed_x = 0
        self.speed_y = 0
        self.image = Surface((20, 30))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.onFlour = False
        self.agroRadius = 200
        self.cooldown = 0
        self.Agro = False
        self.clock = time.Clock()

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

    def attack(self, hero):
        coord1 = [self.rect.x, self.rect.y]
        coord2 = [hero.rect.x, hero.rect.y]
        self.Agro = isAgro(coord1, coord2, self.agroRadius)
        if self.Agro and self.cooldown <= 0:
            self.cooldown = 1000
            return Bullet(coord1, coord2)

    def update(self):
        if self.cooldown > 0:
            self.cooldown -= self.clock.tick()
        if self.cooldown < 0:
            self.cooldown = 0

    # if flags[0]:
    #     self.speed_x = -SPEED
    # if flags[1]:
    #     self.speed_x = SPEED
    # if flags[2] and self.onFlour:
    #     self.speed_y = - JUMP
    #     self.onFlour = False
    # if not(flags[0] or flags[1]):
    #     self.speed_x = 0
    # if not self.onFlour:
    #     self.speed_y += GRAVITY

    # self.onFlour = False
    # self.rect.x += self.speed_x
    # self.collide(self.speed_x, 0, platforms)
    # self.rect.y += self.speed_y
    # self.collide(0, self.speed_y, platforms)

    def collide(self, speed_x, speed_y, platforms):
        for pl in platforms:
            if collide_rect(self, pl):
                if speed_x > 0:
                    self.rect.right = pl.rect.left
                if speed_x < 0:
                    self.rect.left = pl.rect.right
                if speed_y > 0:
                    self.rect.bottom = pl.rect.top
                    self.onFlour = True
                    self.speed_y = 0
                if speed_y < 0:
                    self.rect.top = pl.rect.bottom
                    self.speed_y = 0
