import pygame
import os
import random

from Objets import *

frnt_1 = pygame.image.load(os.path.join(img_folder, "front-1.jpg"))

all_sprites = pygame.sprite.Group()
player = Player()
terrain = Terrain()
ballon = Ballon()
gardien = Gardien()
barredeforce = BarredeForce()
flechedeforce = FlèchedeForce()
barredeprécision = BarredePrécision()
flechedeprécision = FlèchedePrécision()
all_sprites.add(terrain, ballon, gardien, player, barredeforce, flechedeforce, barredeprécision, flechedeprécision)

font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, black)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

#Fonts
smallfont=pygame.font.SysFont("comicsansms",25)
medfont=pygame.font.SysFont("comicsansms",50)
largefont=pygame.font.SysFont("comicsansms",80)

#Font Formating Function
def text_objects(text, color, size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    if size == "medium":
        textSurface = medfont.render(text, True, color)
    if size == "large":
        textSurface = largefont.render(text, True, color)
    return textSurface, textSurface.get_rect()

def gExit():
    all_sprites.remove(all_sprites)
    exit = ExitImage()
    all_sprites.update()
    all_sprites.add(exit)
    all_sprites.update()
    team = pygame.image.load(os.path.join(img_folder, "Team.jpg"))
    pygame.display.set_mode((width, height)).blit(team, (0, 0))
    pygame.display.update()

#Intro Function

def Tir(force, précision, direction):
    sx = 0
    sy = 0
    Bonne_direction = 1 * précision
    Moyenne_direction = (3 - précision) * précision
    Mauvaise_direction = (3 - précision) * 0.5
    Tir_précision = (random.choices([3, 2, 1], [Bonne_direction, Moyenne_direction, Mauvaise_direction]))
    if Tir_précision == 3:
        if 1 <= direction <= 3:
            sy = -10
        if 4 <= direction <= 6:
            sy = -5
        if direction == 1 or 3 or 4 or 6:
            sx = -10
        if direction == 2 or 5:
            sx = 0

    if Tir_précision == 2:
        if 1 <= direction <= 3:
            sy = -10
        if 4 <= direction <= 6:
            sy = -5
        if direction == 1 or 3 or 4 or 6:
            sx = -10
        if direction == 2 or 5:
            sx = 0

    if Tir_précision == 1:
        sy = random.randrange(-10, 10, 10, 5, -5, 5)
        sx = random.randrange(-10, 10, 10, 5, -5, 5)

    ballon.speedy = sy * force
    ballon.speedx = sx * force

    return ballon.speedy
    return ballon.speedx
    print("rola")