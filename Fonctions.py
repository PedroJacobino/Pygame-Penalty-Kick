import pygame
import os
import random

width = 1000
height = 800
centre_x = width/2
centre_y = height/2
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)


# pour ecrire sur l ecran
font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y, color = black):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
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
    print("bola")


def sauter(direction, force, Tir_précision):
    saut = 0
    if Tir_précision == [1]:
        if force == 1 or force == 2:
            st = "Immobile"
        if force == 3:
            st = (random.choices(["Mauvais", "Immobile"], [0.5, 0.5]))

    if Tir_précision == [2]:
        if force == 1:
            st = "Bon"
        if force == 2:
            st = (random.choices(["Mauvais", "Bon"], [0.25, 0.75]))
        if force == 3:
            st = (random.choices(["Mauvais", "Bon"], [0.75, 0.25]))

    if Tir_précision == [3]:
        if force == 1:
            st = (random.choices(["Mauvais", "Bon"], [0.75, 0.25]))
        if force == 2:
            st = (random.choices(["Mauvais", "Bon"], [0.8, 0.2]))
        if force == 3:
            st = "Mauvais"

    if st != 0:
        if st == "Immobile":
            saut = 0

        if st == "Mauvais":
            if direction == 1:
                saut = random.choice([2, 3, 4, 5, 6])
            if direction == 2:
                saut = random.choice([1, 3, 4, 5, 6])
            if direction == 3:
                saut = random.choice([1, 2, 4, 5, 6])
            if direction == 4:
                saut = random.choice([1, 2, 3, 5, 6])
            if direction == 5:
                saut = random.choice([1, 2, 3, 4, 6])
            if direction == 6:
                saut = random.choice([1, 2, 3, 4, 5])

        if st == "Bon":
            saut = direction

        return saut

def Saut(Tir_précision, force, st, gardienstop, direction, playerrun, t3):
    if Tir_précision == [1]:
        if force == 1 or force == 2:
            st = ["Immobile"]
        if force == 3:
            st = (random.choices(["PeuImporte", "Immobile"],
                                 [0.5, 0.5]))  # ( ON PEUT REMPLACER "BON" PAR "MAUVAIS" ÇA NE CHANGERA RIEN )

    if Tir_précision == [2]:
        if force == 1:
            st = ["Bon"]
        if force == 2:
            st = (random.choices(["Mauvais", "Bon"], [0.25, 0.75]))
        if force == 3:
            st = (random.choices(["Mauvais", "Bon"], [0.65, 0.35]))

    if Tir_précision == [3]:
        if force == 1:
            st = (random.choices(["Mauvais", "Bon"], [0.60, 0.40]))
        if force == 2:
            st = (random.choices(["Mauvais", "Bon"], [0.8, 0.2]))
        if force == 3:
            st = ["Mauvais"]

    if st != 0:
        if st == ['Immobile']:
            saut = 0
            gardienstop = True


        elif st == ['Mauvais'] or st == ["PeuImporte"]:
            if direction == 1:
                saut = random.choice([2, 3, 4, 5, 6])
            elif direction == 2:
                saut = random.choice([1, 3, 4, 5, 6])
            elif direction == 3:
                saut = random.choice([1, 2, 4, 5, 6])
            elif direction == 4:
                saut = random.choice([1, 2, 3, 5, 6])
            elif direction == 5:
                saut = random.choice([1, 2, 3, 4, 6])
            elif direction == 6:
                saut = random.choice([1, 2, 3, 4, 5])

        elif st == ['Bon']:
            saut = direction

        playerrun = True

        t3 = False