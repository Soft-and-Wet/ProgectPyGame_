from pygame.sprite import Sprite
from pygame import Surface, image


class Blok(Sprite):
    def __init__(self, x, y, number):
        Sprite.__init__(self)
        adress = 'images/decor/platform_' + number + '.png'
        self.image = image.load(adress).convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
