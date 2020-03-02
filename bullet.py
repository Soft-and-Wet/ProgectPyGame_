from pygame.sprite import Sprite, collide_rect
from pygame import Surface
from defs import calculationOfSpeed

SPEEDBULLET = 5

class Bullet(Sprite):
    def __init__(self, coord1, coord2):
        Sprite.__init__(self)
        self.speed_x = 0
        self.speed_y = 0
        self.speed_x, self.speed_y = calculationOfSpeed(coord1, coord2, SPEEDBULLET)
        self.image = Surface((10, 5))
        self.image.fill((200, 10, 10))
        self.rect = self.image.get_rect()
        self.rect.x = coord1[0]
        self.rect.y = coord1[1]

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

    def update(self, hero, bloks):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        self.collide(hero, bloks)

    def collide(self, hero, bloks):
        if collide_rect(self, hero):
            hero.hurt(30)
            self.kill()
        for blok in bloks:
            if collide_rect(self, blok):
                self.kill()


