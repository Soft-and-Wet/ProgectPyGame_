from pygame.sprite import Sprite, collide_rect
from pygame import Surface, time, image
from defs import *
from bullet import Bullet

SPEED = 4
GRAVITY = 0.4


class Enemy(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.speed_x = 0
        self.speed_y = 0
        self.image = image.load('images/clone/clone_all_colored_f.png').convert()
        self.image.set_colorkey(self.image.get_at((0, 0)))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.onFlour = False
        self.agroRadius = 200
        self.cooldown = 0
        self.Agro = False
        self.clock = time.Clock()
        self.positionOfGun = (0, 0)

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

    def attack(self, hero):
        coord1 = [self.rect.x + self.positionOfGun[0], self.rect.y + self.positionOfGun[1]]
        coord2 = [hero.rect.x, hero.rect.y]
        self.Agro = isAgro(coord1, coord2, self.agroRadius)
        if self.Agro and self.cooldown <= 0:
            self.cooldown = 1000
            return Bullet(coord1, coord2)

    def update(self, platforms, hero):
        if self.Agro:
            if hero.rect.x > self.rect.x:
                self.image = image.load('images/clone/clone_all_colored_r.png').convert()
                self.image.set_colorkey(self.image.get_at((0, 0)))
                self.positionOfGun = (39, 24)
            else:
                self.image = image.load('images/clone/clone_all_colored_l.png').convert()
                self.image.set_colorkey(self.image.get_at((0, 0)))
                self.positionOfGun = (0, 24)
        if self.cooldown > 0:
            self.cooldown -= self.clock.tick()
        if self.cooldown < 0:
            self.cooldown = 0

        if not self.onFlour:
            self.speed_y += GRAVITY

        self.onFlour = False
        self.rect.x += self.speed_x
        self.collide(self.speed_x, 0, platforms)
        self.rect.y += self.speed_y
        self.collide(0, self.speed_y, platforms)

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
