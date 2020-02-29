import pygame
from pygame import *
from character import Character
from blok import Blok
from enemy import Enemy
from shot import Shot
from bar import StatusBar
from items import *

SIZE = (760, 600)
SIZE_WINDOW = (760, 800)

level = [
    '-------------------',
    '-                 -',
    '-                 -',
    '-                 -',
    '-   -------       -',
    '-                 -',
    '-                 -',
    '-        -----    -',
    '-                 -',
    '-   *+            -',
    '-   ---           -',
    '-                 -',
    '-                 -',
    '-                 -',
    '-------------------',
]

window = pygame.display.set_mode(SIZE_WINDOW)
screen = pygame.Surface(SIZE)
bloks = pygame.sprite.Group()
enemies = pygame.sprite.Group()
enemies.add(Enemy(300, 200))
bullets = pygame.sprite.Group()
shots = pygame.sprite.Group()
bar = StatusBar()
buffs = pygame.sprite.Group()
running = True
hero = Character(50, 50)
flags = [False, False, False]
timer = pygame.time.Clock()

x = 0
y = 0
for row in level:
    for col in row:
        if col == '-':
            blok = Blok(x, y)
            blok.add(bloks)
        if col == '+':
            buff = BallOfHealth(x, y)
            buff.add(buffs)
        if col == '*':
            buff = BallOfForce(x, y)
            buff.add(buffs)
        x += 40
    y += 40
    x = 0
pygame.display.flip()
pygame.display.toggle_fullscreen()

while running:
    isShot = False
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
            isShot = True

    screen.fill((47, 79, 79))
    hero.update(flags, bloks)
    for elem in enemies.sprites():
        elem.update(bloks, hero)
        bul = elem.attack(hero)
        if bul is not None:
            bullets.add(bul)
    for elem in bullets.sprites():
        elem.update(hero, bloks)
    if isShot:
        shot = hero.Shot(coord2)
        if shot is not None:
            shots.add(shot)
    for shot in shots.sprites():
        shot.update(enemies, bloks)
    health, force = hero.status()
    bar.update(health, force)
    buffs.update(hero)
    bloks.draw(screen)
    hero.draw(screen)
    enemies.draw(screen)
    bullets.draw(screen)
    shots.draw(screen)
    buffs.draw(screen)
    bar.draw(window)
    window.blit(screen, (0, 0))

    pygame.display.flip()
    pygame.display.toggle_fullscreen()
    timer.tick(60)
