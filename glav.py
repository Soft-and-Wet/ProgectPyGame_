import pygame
from pygame import *
from character import Character
from blok import Blok
from enemy import Enemy
from shot import Shot
from bar import StatusBar
from items import *
from defs import *
from music import *


SIZE = (2000, 800)
SIZE_WINDOW = (760, 800)

level = []

f = open("data/lvl_1.txt", encoding="utf8")
lines = f.readlines()
f.close()
for line in lines:
    if line[-1] == '\n':
        level.append(line[:-1])
    else:
        level.append(line)

window = pygame.display.set_mode(SIZE_WINDOW, pygame.FULLSCREEN)
screen = pygame.Surface(SIZE)
bloks = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()
swords = pygame.sprite.Group()
bar = StatusBar()
buffs = pygame.sprite.Group()
storages = pygame.sprite.Group()
brokens = pygame.sprite.Group()
running = True
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
        elif col == 'v':
            enemy = Enemy(x, y)
            enemy.add(enemies)
        elif col == 'h':
            hero = Character(x, y)
        elif col == 'e':
            exit_level = Exit(x, y)
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

    m_game.play(-1)

    if hero.health < 0:
        running = False
    if pygame.sprite.collide_rect(hero, exit_level):
        running = False
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
        if hero.force > 30:
            sword = Sword([hero.rect.x, hero.rect.y], coord2, hero.pos)
            sword.add(swords)
            hero.force -= 30
    for sword in swords.sprites():
        sword.update(enemies, bloks)
    health, force = hero.status()
    bar.update(health, force)
    buffs.update(hero)
    storages.update(swords, buffs, brokens)
    brokens.update()
    bloks.draw(screen)
    hero.draw(screen)
    enemies.draw(screen)
    bullets.draw(screen)
    swords.draw(screen)
    buffs.draw(screen)
    storages.draw(screen)
    brokens.draw(screen)
    exit_level.draw(screen)
    window.blit(screen, camera(hero, SIZE))
    pygame.draw.rect(window, (0, 0, 0), (0, 600, 760, 200))
    bar.draw(window)
    pygame.display.flip()
    pygame.display.toggle_fullscreen()
    timer.tick(60)
