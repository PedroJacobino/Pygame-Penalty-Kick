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

# set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")


#Les Figures

class Terrain(pygame.sprite.Sprite):
   #sprite for the player
   def __init__(self):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.image.load(os.path.join(img_folder, "Terrain.jpg")).convert()
       self.rect = self.image.get_rect()
       self.rect.center = (width / 2, height / 2)

class Intro(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, "Intro.jpg"))
        self.rect = self.image.get_rect()
        self.rect.center = (width / 2, height / 2)

class ExitImage(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, "Team1.jpg"))
        self.rect = self.image.get_rect()
        self.rect.center = (width / 2, height / 2)

class Gardien(pygame.sprite.Sprite):
   def __init__(self):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.image.load(os.path.join(img_folder, "Gardien.png")).convert_alpha()
       #self.image.set_colorkey(white)
       self.rect = self.image.get_rect()
       self.rect.center = (width / 2, height / 3.5)

   def update(self):
       keystate = pygame.key.get_pressed()
       #if keystate[pygame.K_DOWN]:
        #   self.image = pygame.image.load(os.path.join(img_folder, "Gardien_2.png")).convert_alpha

class Ballon(pygame.sprite.Sprite):
    def __init__(self):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.image.load(os.path.join(img_folder, "Ballon.png")).convert()
       self.image.set_colorkey(white)
       self.rect = self.image.get_rect()
       self.rect.center = (500, 580)
       self.speedy = 0
       self.speedx = 0

    def update(self):
       self.rect.y += self.speedy
       self.rect.x += self.speedx
       if self.rect.y <= 0 or self.rect.y >= 800 or self.rect.x <= 0 or self.rect.x >= 1000:
           self.kill()

       #if direction != "pqp":
        #   if goal == True:
         #      if self.rect.center >= (500, 533):
          #         self.rect.center = (500, 533)
           #if goal == False
            #   if self.rect.center >= smthing:
             #      self.rect.center = Gardien.rect.center

class Player(pygame.sprite.Sprite):
   def __init__(self):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.image.load(os.path.join(img_folder, "player.png")).convert_alpha()
       self.rect = self.image.get_rect()
       self.rect.center = (width / 3.5, height / 1.2)

   def update(self):
       self.speedx = 0
       keystate = pygame.key.get_pressed()
       if keystate[pygame.K_DOWN]:
           self.speedx = 10
       self.rect.x += self.speedx
       self.speedy = 0
       if keystate[pygame.K_DOWN]:
           self.speedy = -10
       self.rect.y += self.speedy
       if self.rect.center >= (500, 533):
           self.rect.center = (500, 533)

# Pour mesurer La Force et déterminer la direction
class BarredeForce(pygame.sprite.Sprite):
   def __init__(self):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.image.load(os.path.join(img_folder, "Barre_de_force.png")).convert()
       self.rect = self.image.get_rect()
       self.rect.center = (width/1.6, height/2)

class BarredePrécision(pygame.sprite.Sprite):
   def __init__(self):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.image.load(os.path.join(img_folder, "Rectangle_de_précision_Pénalti.jpg")).convert()
       self.rect = self.image.get_rect()
       self.rect.center = (width/2, height/1.2)

class FlèchedeForce(pygame.sprite.Sprite):
   def __init__(self):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.image.load(os.path.join(img_folder, "Flèche_de_force.png")).convert()
       self.rect = self.image.get_rect()
       self.image.set_colorkey(white)
       self.rect.center = (width/1.5, 515)
       self.a = True  # Pendant que le button est appuyé
       self.b = False # Pour que le button ne soit plus appuyé à nouveau
       self.force = 0

   def update(self):

       self.speedy = 0
       keystate = pygame.key.get_pressed()

       if keystate[pygame.K_UP] and self.a == True:
           self.speedy = -10 + self.acceleration_y
           self.b = True

       self.rect.y += self.speedy

       if self.rect.top < 215:
           self.rect.center = (width / 1.5, 515)
       if self.rect.top >400:
           self.acceleration_y = 0
           self.force = 1
       if 400>self.rect.top >350:
           self.acceleration_y = -5
           self.force = 2
       if 350>self.rect.top >220:
           self.acceleration_y = -10
           self.force = 3

       if  not keystate[pygame.K_UP] and self.b == True:
           self.a = False

class FlèchedePrécision(pygame.sprite.Sprite):
   def __init__(self):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.image.load(os.path.join(img_folder, "Flèche_de_précision.png")).convert()
       self.rect = self.image.get_rect()
       self.rect.center = (width/2, height/1.2)
       self.acceleration_x = 0
       self.vitesse = 15
       self.précision = 0


   def update(self):
       self.speedx = 0
       keystate = pygame.key.get_pressed()

       if keystate[pygame.K_UP]:
           self.acceleration_x = self.vitesse

       self.speedx = -self.vitesse + self.acceleration_x

       self.rect.x += self.speedx

       if  (490, height/1.2) <= self.rect.center <= (510, height/1.2):
           self.précision = 3

       if  (460, height/1.2) <= self.rect.center < (490, height/1.2) or (510, height/1.2) < self.rect.center <= (540, height/1.2):
           self.précision = 2

       if (420, height / 1.2) <= self.rect.center < (460, height / 1.2) or (540, height / 1.2) < self.rect.center <= (580, height / 1.2):

           self.précision = 1

       if  (390, height/1.2) <= self.rect.center < (420, height/1.2) or (580, height/1.2) < self.rect.center <= (610, height/1.2):

           self.précision = 0

       if self.rect.left < 400:
           self.acceleration_x = 2 * self.vitesse

       if self.rect.right > 600:
           self.acceleration_x = 0