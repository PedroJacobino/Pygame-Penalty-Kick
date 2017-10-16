import pygame
import os
import random

from Objets import *

intro = Intro()
score = 0
gardien_pris = 0
isolé = 0
tentatives = 0
fps = 30
Tutorial = True
reiniciar = True
Introduction = True # Pour faire l'intro
InterfaceTutoriel = 0
running = True
son = False
infini = False
# Initialize pygame and create window

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tirs de Pénalty")
clock = pygame.time.Clock()
icn = pygame.image.load(os.path.join(img_folder, "icon.jpg"))
pygame.display.set_icon(icn)
keystate = pygame.key.get_pressed()
bg = pygame.image.load(os.path.join(img_folder, "bgblanc.jpg")).convert()
flèchedroite = pygame.image.load(os.path.join(img_folder, "flèchedroite.png")).convert()
flèchegauche = pygame.transform.flip(flèchedroite, 1, 0)
jouer = pygame.image.load(os.path.join(img_folder, "Jouer.png")).convert_alpha()
rejouer = pygame.image.load(os.path.join(img_folder, "Rejouer.png")).convert_alpha()
but = pygame.image.load(os.path.join(img_folder, "BUT.png")).convert()
image_son = pygame.image.load(os.path.join(img_folder, "Hautparleur.jpg")).convert()
image_pas_son = pygame.image.load(os.path.join(img_folder, "PasHautparleur.jpg")).convert()
image_infinie = pygame.image.load(os.path.join(img_folder, "infinie.jpg")).convert()
image_pasinfinie = pygame.image.load(os.path.join(img_folder, "pasinfinie.jpg")).convert()


from Fonctions import *
while Introduction:
    if InterfaceTutoriel == 0:
        all_sprites = pygame.sprite.Group()
        all_sprites.add(intro)
        all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.flip()
        pygame.time.wait(2000)
        all_sprites.remove(intro)
        Intro.kill(intro)
        all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.flip()
        InterfaceTutoriel = 1

    if 3 > InterfaceTutoriel > 1: # Pour retourner une page
        screen.blit(flèchegauche, (15, 600))

    if InterfaceTutoriel < 2:  # pour avancer une page
        screen.blit(flèchedroite, (935, 600))

    if InterfaceTutoriel >= 1:
        Intro.kill(intro)
        all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.flip()
        screen.blit(bg, (0, 0))
        if InterfaceTutoriel == 1:
            screen.blit(jouer, (392.5, 364))
            if infini:
                screen.blit(image_infinie, (50, 40))
            if not infini:
                screen.blit(image_pasinfinie, (50, 40))
            if son :
                screen.blit(image_son, (850,40))
            if not son:
                screen.blit(image_pas_son, (850, 40))

        if InterfaceTutoriel == 2:
            draw_text(screen, "Tutoriel", 35, 500, 50, green)
            draw_text(screen, "Pour jouer à ce jeux, vous devez cliquer que deux fois sur le clavier:", 25, 500, 100, black)
            draw_text(screen, "Une première fois sur l'espace pour déterminer la précision de votre tir", 25, 500, 150, black)
            draw_text(screen, "évidemment que c'est sur le vert que vous voulez appuyer pour la meilleur précision", 25, 500, 200, black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            Introduction = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                Introduction = False
            if event.key == pygame.K_RIGHT:
                InterfaceTutoriel += 1
            if event.key == pygame.K_LEFT:
                if InterfaceTutoriel > 1:
                    InterfaceTutoriel -= 1
        if event.type == pygame.MOUSEBUTTONDOWN: # event.pos[o] = x et event.pos[1] = y
            if event.pos[0] >= 935 and event.pos[0] <= 985 and event.pos[1] >= 600 and event.pos[1] <= 640 and InterfaceTutoriel < 2:
                InterfaceTutoriel += 1
            if event.pos[0] >= 15 and event.pos[0] <= 65 and event.pos[1] >= 600 and event.pos[1] <= 640 and InterfaceTutoriel > 1:
                InterfaceTutoriel -= 1
            if event.pos[0] >= 393.5 and event.pos[0] <= 606.5 and event.pos[1] >= 364 and event.pos[1] <= 436 and InterfaceTutoriel == 1:
                Introduction = False
            if event.pos[0] >= 850 and event.pos[0] <= 947 and event.pos[1] >= 40 and event.pos[1] <= 116 and InterfaceTutoriel == 1:
                son = not son
            if event.pos[0] >= 50 and event.pos[0] <= 153 and event.pos[1] >= 40 and event.pos[1] <= 88 and InterfaceTutoriel == 1:
                infini = not infini


# Game loop

while running:

    clock.tick(fps)

    if reiniciar:
        reiniciar = False # pour retourner cette boucle ert rejouer le jeu
        direction = False # le joueur a donné la direction
        Tir_précision = False
        changeforprecision = 0
        flèches_sur_lécran = True  # Les flèches sont ou pas sur l'écran
        direction_pas_détérminée = True  # La direction est déterminée ou pas
        t3 = True
        t5 = True
        t6 = True
        sy = 0
        sx = 0
        st = 0
        saut = 0
        all_sprites = pygame.sprite.Group()
        player = Player()
        terrain = Terrain()
        ballon = Ballon()
        gardien = Gardien()
        barredeforce = BarredeForce()
        flechedeforce = FlèchedeForce()
        barredeprécision = BarredePrécision()
        flechedeprécision = FlèchedePrécision()
        all_sprites.add(terrain, gardien, ballon, player, barredeforce, flechedeforce, barredeprécision,
                        flechedeprécision)
        sound = True



    def gExit():   # Teve de definit aqui para ser depois da definiçao de all_sprites
        all_sprites.remove(all_sprites)
        exit = ExitImage()
        all_sprites.update()
        all_sprites.add(exit)
        all_sprites.update()
        team = pygame.image.load(os.path.join(img_folder, "Team1.jpg"))
        pygame.display.set_mode((width, height)).blit(team, (0, 0))
        pygame.display.update()


    '''Si l'on veut limiter le nombre de chances'''
    if tentatives == 5 and not infini:
        reiniciar = False
        all_sprites.remove(all_sprites)
        all_sprites.update(all_sprites)
        all_sprites.draw(screen)
        screen.blit(bg, (0, 0))
        screen.blit(rejouer, (360.5, 355))
        draw_text(screen, "Vous avez fait " + str(score) + " buts", 30, 500, 30)
        draw_text(screen, "Le gardien a pris " + str(gardien_pris) + " tirs", 30, 500, 60)
        draw_text(screen, "Vous avez isolé " + str(isolé) + " tirs", 30, 500, 90)
        pygame.display.flip()
        if event.type == pygame.MOUSEBUTTONDOWN: # event.pos[o] = x et event.pos[1] = y
            if event.pos[0] >= 360.5 and event.pos[0] <= 639.5 and event.pos[1] >= 355 and event.pos[1] <= 445:
                tentatives = 0
                score = 0
                gardien_pris = 0
                isolé = 0
                reiniciar = True

    # Faire les flèches disparaître une fois les paramètres déterminés
    if not flechedeforce.a and flèches_sur_lécran:
        pygame.time.wait(2000)
        BarredePrécision.kill(barredeprécision)
        BarredeForce.kill(barredeforce)
        FlèchedeForce.kill(flechedeforce)
        FlèchedePrécision.kill(flechedeprécision)
        flèches_sur_lécran = False

    for event in pygame.event.get():

        if event.type == pygame.QUIT: #Pour pouvoir sortir du jeu, et montrer l'image de sortie
            gExit()
            pygame.time.wait(2000)
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                gExit()
                pygame.time.wait(2000)
                running = False
            if event.key == pygame.K_r:
                reiniciar = True
        #determiner la direction du tir
        if event.type == pygame.KEYDOWN and not flechedeforce.a and not direction and direction_pas_détérminée:

            if event.key == pygame.K_q:
                direction = 1
                direction_pas_détérminée = False

            elif event.key == pygame.K_w:
                direction = 2
                direction_pas_détérminée = False

            elif event.key == pygame.K_e:
                direction = 3
                direction_pas_détérminée = False

            elif event.key == pygame.K_a:
                direction = 4
                direction_pas_détérminée = False

            elif event.key == pygame.K_s:
                direction = 5
                direction_pas_détérminée = False

            elif event.key == pygame.K_d:
                direction = 6
                direction_pas_détérminée = False



        #Logique pour déterminer la précision du tir d'aorès les paramètres et où le gardien va sauter
        if not direction_pas_détérminée and t3:
            Bonne_direction = 1 * flechedeprécision.précision
            Moyenne_direction = (3 - flechedeprécision.précision) * flechedeprécision.précision
            Mauvaise_direction = (3 - flechedeprécision.précision) * 0.5
            Tir_pr = (random.choices([3, 2, 1], [Bonne_direction, Moyenne_direction, Mauvaise_direction]))

            if changeforprecision == 0:
                Tir_précision = Tir_pr
                changeforprecision = 1

            if Tir_précision == [3]:
                if 1 <= direction <= 3:
                    sy = -21
                if 4 <= direction <= 6:
                    sy = -16
                if direction == 1 or direction == 4:
                    sx = -10
                if direction == 3 or direction == 6:
                    sx = 10
                if direction == 2 or direction == 5:
                    sx = 0

            if Tir_précision == [2]:
                if 1 <= direction <= 3:
                    sy = -21
                if 4 <= direction <= 6:
                    sy = -16
                if direction == 1 or direction == 4:
                    sx = -10
                if direction == 3 or direction == 6:
                    sx = 10
                if direction == 2 or direction == 5:
                    sx = 0

            if Tir_précision == [1]:
                sy = random.choice([-10, 10, -5, 5])
                sx = random.choice([-10, 10, -5, 5])

            # ----------------------------------------------------------- SAUT DU GARDIEN ---------------------------------------
            if Tir_précision == [1]:
                if flechedeforce.force == 1 or flechedeforce.force == 2:
                    st = ["Immobile"]
                if flechedeforce.force == 3:
                    st = (random.choices(["PeuImporte", "Immobile"], [0.5, 0.5])) #( ON PEUT REMPLACER "BON" PAR "MAUVAIS" ÇA NE CHANGERA RIEN )

            if Tir_précision == [2]:
                if flechedeforce.force == 1:
                    st = ["Bon"]
                if flechedeforce.force == 2:
                    st = (random.choices(["Mauvais", "Bon"], [0.25, 0.75]))
                if flechedeforce.force == 3:
                    st = (random.choices(["Mauvais", "Bon"], [0.65, 0.35]))

            if Tir_précision == [3]:
                if flechedeforce.force == 1:
                    st = (random.choices(["Mauvais", "Bon"], [0.60, 0.40]))
                if flechedeforce.force == 2:
                    st = (random.choices(["Mauvais", "Bon"], [0.8, 0.2]))
                if flechedeforce.force == 3:
                    st = ["Mauvais"]



            if st != 0:
                if st == ['Immobile']:
                    saut = 0
                    gardien.stop = True


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

                player.run = True

                t3 = False


                #""""Application des valeurs calculées sur les classes"""
    if t5 == True and t3 == False and player.chutant == True:
         # """Pour que le ballon ne sorte que lorsque le joueur chute le ballon"""
        ballon.sx = sx
        ballon.sy = sy
        gardien.saut = [saut]


        ballon.speedy = ballon.sy * flechedeforce.force
        ballon.speedx = ballon.sx * flechedeforce.force
        print(Tir_précision)
        print(flechedeforce.force)
        print(st)
        print(gardien.saut)
        print(player.chutant)
        t5 = False

    if son:
        if not t5 and ballon.stop and gardien.stop:
            if st == ["Bon"]:
                pygame.mixer.music.load(os.path.join(sound_folder, "tafarel.mp3"))
                pygame.mixer.music.play(0)
                pygame.time.delay(8000)
                gardien_pris += 1
            # pygame.time.delay(1000)
            if st == ["Mauvais"]:
                score += 1
                screen.blit(but, (200, 200))
                pygame.mixer.music.play(0)
                pygame.time.delay(3500)
                pygame.display.flip()
                pygame.time.delay(2000)

            if st == ["Immobile"] or st == ["PeuImporte"]:
                pygame.mixer.music.load(os.path.join(sound_folder, "errou.mp3"))
                pygame.mixer.music.play(0)
                isolé += 1

            tentatives += 1
            pygame.time.delay(2000)
            reiniciar = True
        if st == ["Mauvais"] and player.chutant and sound:
            pygame.mixer.music.load(os.path.join(sound_folder, "gol_cut.mp3"))
            pygame.mixer.music.play(0)
            sound = False

    if not son:
        if not t5 and ballon.stop and gardien.stop:
            # pygame.time.delay(1000)
            if st == ["Bon"]:
                gardien_pris += 1
            if st == ["Mauvais"]:
                score += 1
                screen.blit(but, (200, 200))
                pygame.display.flip()
                pygame.time.delay(2000)
            if st == ["Immobile"] or st == ["PeuImporte"]:
                isolé += 1
            tentatives += 1
            pygame.time.delay(2000)
            reiniciar = True



        #pygame.mixer.music.load(os.path.join(sound_folder, "tafarel.mp3"))
    #pygame.mixer.music.play(0)
            # Update
    gardien.animate()
    all_sprites.update()
    # Draw/render
    #screen.fill(black)
    all_sprites.draw(screen)
    '''Si l'on veut laisser 5 tentatives'''
    if running and tentatives < 5 and not infini:
        draw_text(screen, "Score : " + str(score), 40, 900, 30)
        draw_text(screen, "Tentatives : " +str(tentatives), 40, 100, 30)
    if running and infini:
        draw_text(screen, "Score : " + str(score), 40, 900, 30)
        raté = gardien_pris + isolé
        draw_text(screen, "Ratées : " + str(raté), 40, 100, 30)


    # After drawing everything, flip the display
    pygame.display.flip()

pygame.quit()