                                                                      Aqui tem várias idéias que eu posso adicionar depois





import pygame

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Penalites')

gameExit = False

lead_x = 300
lead_y = 300
lead_x_change = 0

clock = pygame.time.Clock()

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x_change = -2
            if event.key == pygame.K_RIGHT:
                lead_x_change = 2

    lead_x += lead_x_change
    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay, black, [lead_x, lead_y, 10, 10])
    pygame.display.update()

    clock.tick(100)

pygame.quit()
quit()












------> Definiçao da Flecha de Força <-------------


class FlèchedeForce(pygame.sprite.Sprite):
   #sprite for the player
   def __init__(self):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.image.load(os.path.join(img_folder, "Flèche_de_force.png")).convert()
       self.rect = self.image.get_rect()
       self.image.set_colorkey(white)
       self.rect.center = (width/1.5, 515)


   def update(self):
       self.y_speed = 0
       self.rect.y += self.y_speed
       keystate = pygame.key.get_pressed()
       if keystate[pygame.K_p]:
           self.y_speed = -10 + self.accelerationy
       if self.rect.top < 215:
           self.accelerationy = 20
       if self.rect.bottom > 800:
           self.accelerationy = -20

   x = 0
   if keystate[pygame.K_p]:
       x = 1
   if not keystate[pygame.K_p]:
       if x == 1:
           self.y_speed = 0




    #deu certo sem deixar pressionado

           def update(self):
               self.rect.y += self.y_speed

               if self.rect.top < 215:
                   self.y_speed = 10
               if self.rect.bottom > 600:
                   self.y_speed = -10

               keystate = pygame.key.get_pressed()
               if keystate[pygame.K_p]:
                   a = 1
               if not keystate[pygame.K_p]:
                   if x == 1:
                       self.y_speed = 0
                       x = self.rect.y


#Melhor de TODOS :(faza seta voltar direto embaixo)
#Sem ter feito cagada
       class FlèchedeForce(pygame.sprite.Sprite):
           # sprite for the player
           def __init__(self):
               pygame.sprite.Sprite.__init__(self)
               self.image = pygame.image.load(os.path.join(img_folder, "Flèche_de_force.png")).convert()
               self.rect = self.image.get_rect()
               self.image.set_colorkey(white)
               self.rect.center = (width / 1.5, 515)
               self.a = True
               self.b = False
               self.x = 0

           def update(self):

               self.speedy = 0
               keystate = pygame.key.get_pressed()

               if keystate[pygame.K_UP] and self.a == True:
                   self.speedy = -10 + self.acceleration_y
                   self.b = True

               self.rect.y += self.speedy

               if self.rect.top < 215:
                   self.rect.center = (width / 1.5, 515)
               if self.rect.top > 400:
                   self.acceleration_y = 0
                   self.x = 1
               if 400 > self.rect.top > 350:
                   self.acceleration_y = -5
                   self.x = 2
               if 350 > self.rect.top > 220:
                   self.acceleration_y = -10
                   self.x = 3
               if not keystate[pygame.K_UP] and self.b == True:
                   self.a = False

------> Definiçao da Flecha de Força <-------------