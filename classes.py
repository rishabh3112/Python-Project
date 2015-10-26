import pygame
pygame.init()

#temporary values, to be changed later
brakespeed = 0.5
maxspeed = 5

class player():

    def __init__(self):
        #initialize all variables

        self.x = 0.0
        self.y = 0.0
        self.h = 25
        self.w = 25
        self.speedx = 0.0
        self.speedy = 0.0
        self.health = 100.0
        self.armour = 0.0

        self.powerup1 = False
        self.powerup2 = False
        self.powerup3 = False

        self.image = pygame.image.load('images/player.png')
        self.image = pygame.transform.scale(self.image, (self.w, self.h))

    def move(self,direction):
        #set initial speed according to direction

        if direction == 'up':
            self.speedy = -maxspeed
        elif direction == 'down':
            self.speedy = maxspeed
        elif direction == 'left':
            self.speedx = -maxspeed
        elif direction == 'right':
            self.speedx = maxspeed     

    def inertia(self):
        #constantly reduce speed till it is zero for smooth motion
        #brakespeed is low to see the slowing effect

        if self.speedx > 0:
            self.speedx = (self.speedx*1000 - brakespeed*1000)/1000
        elif self.speedx < 0:
            self.speedx = (self.speedx*1000 + brakespeed*1000)/1000

        if self.speedy > 0:
            self.speedy = (self.speedy*1000 - brakespeed*1000)/1000
        elif self.speedy < 0:
            self.speedy = (self.speedy*1000 + brakespeed*1000)/1000

        #always adds speed to x and y coords
        self.x += self.speedx
        self.y += self.speedy

    def shoot():
        pass

    def interact():
        pass
    

class wall():

    def __init__(self):
        #initialize all variables

        self.x = 0.0
        self.y = 0.0
        self.h = 30
        self.w = 30

        self.can_collide = True

        self.image = pygame.image.load('images/wall.png')
        self.image = pygame.transform.scale(self.image, (self.w, self.h))
        