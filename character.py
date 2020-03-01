from pygame.sprite import Sprite, collide_rect
from pygame import Surface, time, image
from shot import Shot

SPEED = 4
GRAVITY = 0.4
JUMP = 12
SPEEDOFREGENERATION = 1000
FORCEOFREGENERATION = 1


class Character(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.speed_x = 0
        self.speed_y = 0
        self.image = image.load('images/jedi/jedi_f.png').convert()
        self.image.set_colorkey(self.image.get_at((0, 0)))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.onFlour = False
        self.health = 100
        self.force = 100
        self.clock = time.Clock()
        self.regeneration = SPEEDOFREGENERATION
        self.pos = 'f'

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

    def update(self, flags, platforms):
        if flags[0]:
            self.speed_x = -SPEED
            self.image = image.load('images/jedi/jedi_run_l_1.png').convert()
            self.image.set_colorkey(self.image.get_at((0, 0)))
            self.pos = 'l'
        if flags[1]:
            self.speed_x = SPEED
            self.image = image.load('images/jedi/jedi_run_r_1.png').convert()
            self.image.set_colorkey(self.image.get_at((0, 0)))
            self.pos = 'r'
        if flags[2] and self.onFlour:
            self.speed_y = - JUMP
            self.onFlour = False
        if not (flags[0] or flags[1]):
            self.speed_x = 0
            self.image = image.load('images/jedi/jedi_f.png').convert()
            self.image.set_colorkey(self.image.get_at((0, 0)))
            self.pos = 'f'
        if not self.onFlour:
            self.speed_y += GRAVITY

        self.onFlour = False
        self.rect.x += self.speed_x
        self.collide(self.speed_x, 0, platforms)
        self.rect.y += self.speed_y
        self.collide(0, self.speed_y, platforms)

        if self.regeneration > 0:
            self.regeneration -= self.clock.tick()
        if self.regeneration < 0:
            self.cooldown = 0

        if self.regeneration <= 0:
            self.regeneration = SPEEDOFREGENERATION
            self.health += FORCEOFREGENERATION
            self.force += FORCEOFREGENERATION

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

    def Shot(self, coord2):
        if self.force >= 30:
            self.force -= 30
            coord1 = [self.rect.x, self.rect.y]
            return Shot(coord1, coord2)

    def status(self):
        return self.health, self.force

    def hurt(self, damage):
        self.health -= damage
