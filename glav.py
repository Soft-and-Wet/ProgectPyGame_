import pygame
from pygame import *
from character import Character
from blok import Blok
from enemy import Enemy
from shot import Shot
from bar import StatusBar
from items import *
from defs import *

SIZE = (920, 600)
SIZE_WINDOW = (760, 800)

level = [
    '52222222222222222222226',
    '1                     3',
    '1                     3',
    '1                     3',
    '1   5222226           3',
    '1                     3',
    '1         s           3',
    '1        52226        3',
    '1                     3',
    '1   *+                3',
    '1   526               3',
    '1                     3',
    '1                     3',
    '1                     3',
    '84444444444444444444447',
]

window = pygame.display.set_mode(SIZE_WINDOW, pygame.FULLSCREEN)
screen = pygame.Surface(SIZE)
bloks = pygame.sprite.Group()
enemies = pygame.sprite.Group()
# enemies.add(Enemy(300, 200))
bullets = pygame.sprite.Group()
swords = pygame.sprite.Group()
bar = StatusBar()
buffs = pygame.sprite.Group()
storages = pygame.sprite.Group()
running = True
hero = Character(50, 50)
flags = [False, False, False]
timer = pygame.time.Clock()

x = 0
y = 0
for row in level:
    for col in row:
        if col == '+':
            buff = BallOfHealth(x, y)
            buff.add(buffs)
        elif col == '*':
            buff = BallOfForce(x, y)
            buff.add(buffs)
        elif col == 's':
            storage = Storage(x, y)
            storage.add(storages)
        elif col != ' ':
            blok = Blok(x, y, col)
            blok.add(bloks)
        x += 40
    y += 40
    if x > SIZE[0] or y > SIZE[1]:
        SIZE = (x, y)
    x = 0
pygame.display.flip()
pygame.display.toggle_fullscreen()

while running:
    isAttack = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                flags[0] = True
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                flags[1] = True
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                flags[2] = True
            if event.key == pygame.K_ESCAPE:
                running = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                flags[0] = False
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                flags[1] = False
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                flags[2] = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            coord2 = list(event.pos)
            isAttack = True

    screen.fill((47, 79, 79))
    hero.update(flags, bloks)
    for elem in enemies.sprites():
        elem.update(bloks, hero)
        bul = elem.attack(hero)
        if bul is not None:
            bullets.add(bul)
    for elem in bullets.sprites():
        elem.update(hero, bloks)
    if isAttack:
        sword = Sword([hero.rect.x, hero.rect.y], coord2)
        sword.add(swords)
    for sword in swords.sprites():
        sword.update(enemies, bloks, hero)
    health, force = hero.status()
    bar.update(health, force)
    buffs.update(hero)
    storages.update(swords, buffs)
    bloks.draw(screen)
    hero.draw(screen)
    enemies.draw(screen)
    bullets.draw(screen)
    swords.draw(screen)
    buffs.draw(screen)
    storages.draw(screen)
    bar.draw(window)
    window.blit(screen, camera(hero, SIZE))
    pygame.display.flip()
    pygame.display.toggle_fullscreen()
    timer.tick(60)
