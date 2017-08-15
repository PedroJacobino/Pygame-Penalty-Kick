import pygame
import os
import random

from Objets import *

fps = 30
direction = False
Tir_précision = False
n = 0
t1 = True # Les flèches sont disparues
t2 = True # La direction est déterminée
t3 = True
t4 = True
sy = 0
sx = 0
intro = Intro()
# Initialize pygame and create window

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tirs de Pénalty")
clock = pygame.time.Clock()
#icn = pygame.image.load(os.path.join(img_folder, "icon.jpg")).convert()
#pygame.display.set_icon(icn)
keystate = pygame.key.get_pressed()

from Addsprites import *

# Game loop
running = True
while running:
    clock.tick(fps)


    #Image d'introduction
    if t4 == True:
        all_sprites.add(intro)
        all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.flip()
        pygame.time.wait(2000)
        all_sprites.remove(intro)
        all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.flip()
        t4 = False

    #if t4:
        #intro()

    #Faire les paramètres disparaître une fois déterminés
    if flechedeforce.a == False and t1 == True:
        pygame.time.wait(2000)
        BarredePrécision.kill(barredeprécision)
        BarredeForce.kill(barredeforce)
        FlèchedeForce.kill(flechedeforce)
        FlèchedePrécision.kill(flechedeprécision)
        t1 = False

    for event in pygame.event.get():
        #Pour pouvoir sortir du jeu, et montrer l'image de sortie
        if event.type == pygame.QUIT:
            gExit()
            pygame.time.wait(2000)
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                gExit()
                pygame.time.wait(2000)
                running = False

        #determiner la direction du tir
        if event.type == pygame.KEYDOWN and flechedeforce.a == False and direction == False and t2 == True:

            if event.key == pygame.K_q:
                direction = 1
                t2 = False

            elif event.key == pygame.K_w:
                direction = 2
                t2 = False

            elif event.key == pygame.K_e:
                direction = 3
                t2 = False

            elif event.key == pygame.K_a:
                direction = 4
                t2 = False

            elif event.key == pygame.K_s:
                direction = 5
                t2 = False

            elif event.key == pygame.K_d:
                direction = 6
                t2 = False

        #Logique pour déterminer la précision du tir d'aorès les paramètres
        if t2 == False and t3 == True:
            Bonne_direction = 1 * flechedeprécision.précision
            Moyenne_direction = (3 - flechedeprécision.précision) * flechedeprécision.précision
            Mauvaise_direction = (3 - flechedeprécision.précision) * 0.5
            Tir_pr = (random.choices([3, 2, 1], [Bonne_direction, Moyenne_direction, Mauvaise_direction]))

            if n == 0:
                Tir_précision = Tir_pr
                n = 1

            if Tir_précision == [3]:
                if 1 <= direction <= 3:
                    sy = -10
                if 4 <= direction <= 6:
                    sy = -5
                if direction == 1 or direction == 4:
                    sx = -10
                if direction == 3 or direction == 6:
                    sx = 10
                if direction == 2 or direction == 5:
                    sx = 0

            if Tir_précision == [2]:
                if 1 <= direction <= 3:
                    sy = -10
                if 4 <= direction <= 6:
                    sy = -5
                if direction == 1 or direction == 4:
                    sx = -10
                if direction == 3 or direction == 6:
                    sx = 10
                if direction == 2 or direction == 5:
                    sx = 0

            if Tir_précision == [1]:
                sy = random.choice([-10, 10, -5, 5])
                sx = random.choice([-10, 10, -5, 5])
            ballon.speedy = sy * flechedeforce.force
            ballon.speedx = sx * flechedeforce.force
            # Tir(flechedeforce.force, flechedeprécision.précision, direction)
            t3 = False


            # Update
    all_sprites.update()
    # Draw/render
    screen.fill(black)
    all_sprites.draw(screen)
    draw_text(screen, str(100), 40, width / 1.07, 30)
    # draw_text(screen, str(5), 40, width / 1.17, 30)
    # draw_text(screen, "-", 40, width / 1.12, 30)

    # After drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
