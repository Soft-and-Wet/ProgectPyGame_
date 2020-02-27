import pygame
import os
from music import *
from pygame import *
from character import Character
from blok import Blok
from enemy import Enemy
from shot import Shot
from bar import StatusBar


SIZE = (760, 600)
SIZE_WINDOW = (760, 800)

pygame.init()
pygame.mixer.init()


def load_image(name, colorkey=None):
    fullname = os.path.join('', name)
    image = pygame.image.load(fullname).convert_alpha()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


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
    '-                 -',
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

menu = True
running = False

hero = Character(50, 50)
flags = [False, False, False]
timer = pygame.time.Clock()
platforms = []

x = 0
y = 0
for row in level:
    for col in row:
        if col == '-':
            blok = Blok(x, y)
            blok.add(bloks)
            platforms.append(blok)
        x += 40
    y += 40
    x = 0
pygame.display.flip()

pygame.display.set_caption("SW game")

size_menu = width, height = 760, 432
screen_menu = pygame.display.set_mode(size_menu)

size = width, height = SIZE_WINDOW
screen = pygame.display.set_mode(size)

pygame.mixer.music.play()

while menu:
    # screen_menu.fill((0, 0, 255))
    image_menu = load_image("sw_pic/menu/menu.png")
    screen_menu.blit(image_menu, (-4, 0))
    # играет музон_1
    # pygame.mixer.music.play()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.mixer.music.stop()
            menu = False
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP_ENTER:
                # музон_1 не играет, играет музон_2
                pygame.mixer.music.stop()
                m_game.play(-1)
                menu = False
                running = True

    pygame.display.flip()
    timer.tick(60)


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

    screen.fill((125, 125, 125))
    hero.update(flags, platforms)
    for elem in enemies.sprites():
        elem.update()
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
    bloks.draw(screen)
    hero.draw(screen)
    enemies.draw(screen)
    bullets.draw(screen)
    shots.draw(screen)
    bar.draw(window)
    window.blit(screen, (0, 0))

    pygame.display.flip()
    timer.tick(60)
