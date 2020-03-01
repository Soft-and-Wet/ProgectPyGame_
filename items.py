from pygame.sprite import Sprite, collide_rect
import pygame
from defs import calculationOfSpeed

SPEEDSWORD = 8
ACCELERATIONSWORD = 0.1


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


class Sword(Sprite):
    def __init__(self, coord1, coord2):
        Sprite.__init__(self)
        print(coord1, coord2)
        if coord2[0] > coord1[0]:
            self.image = pygame.image.load('images/jedi/sword_r.png').convert()
            self.image.set_colorkey(self.image.get_at((0, 0)))
        else:
            self.image = pygame.image.load('images/jedi/sword_l.png').convert()
            self.image.set_colorkey(self.image.get_at((0, 0)))
        self.rect = self.image.get_rect()
        self.rect.x = coord1[0]
        self.rect.y = coord1[1]
        self.speed_x, self.speed_y = calculationOfSpeed(coord1, coord2, SPEEDSWORD)
        self.acc_x, self.acc_y = calculationOfSpeed(coord1, coord2, ACCELERATIONSWORD)
        self.acc_x, self.acc_y = - self.acc_x, - self.acc_y
        self.isAttack = False
        self.angle = 0
        self.isReturn = False

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

    def update(self, enemies, bloks, hero):
        self.speed_x += self.acc_x
        self.speed_y += self.acc_y
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        self.collide(enemies, bloks, hero)
        if self.speed_x + self.acc_x < 0:
            self.isReturn = True
            self.acc_y, self.acc_x = 0, 0
        if self.isReturn:
            self.speed_x, self.speed_y = calculationOfSpeed([self.rect.x, self.rect.y], [hero.rect.x, hero.rect.y],
                                                            SPEEDSWORD)

    def collide(self, enemies, bloks, hero):
        for enemy in enemies:
            if collide_rect(self, enemy):
                enemy.kill()
                self.speed_x, self.speed_y = 0, 0
        for blok in bloks:
            if collide_rect(self, blok) and not self.isReturn:
                self.speed_x, self.speed_y = 0, 0
        if collide_rect(self, hero) and self.isReturn:
            self.kill()

    # def update(self, x, y, screen, isAttack, pos):
    #     self.isAttack = isAttack
    #     self.rect.x = x
    #     self.rect.y = y
    #     if pos == 'f':
    #         self.rect.x = -1000
    #     elif pos == 'r':
    #         self.angle = 135
    #     else:
    #         self.angle = 45
    #     if self.isAttack:
    #         pass
    #     else:
    #         self.draw(screen)

    def blitRotate(self, surf, image, pos, originPos, angle):

        # calcaulate the axis aligned bounding box of the rotated image
        w, h = image.get_size()
        box = [pygame.math.Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]
        box_rotate = [p.rotate(angle) for p in box]
        min_box = (min(box_rotate, key=lambda p: p[0])[0], min(box_rotate, key=lambda p: p[1])[1])
        max_box = (max(box_rotate, key=lambda p: p[0])[0], max(box_rotate, key=lambda p: p[1])[1])

        # calculate the translation of the pivot
        pivot = pygame.math.Vector2(originPos[0], -originPos[1])
        pivot_rotate = pivot.rotate(angle)
        pivot_move = pivot_rotate - pivot

        # calculate the upper left origin of the rotated image
        origin = (
            pos[0] - originPos[0] + min_box[0] - pivot_move[0], pos[1] - originPos[1] - max_box[1] + pivot_move[1])

        # get a rotated image
        rotated_image = pygame.transform.rotate(image, angle)

        # rotate and blit the image
        surf.blit(rotated_image, origin)

        # draw rectangle around the image
        pygame.draw.rect(surf, (255, 0, 0), (*origin, *rotated_image.get_size()), 2)
