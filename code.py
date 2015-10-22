import pygame
from classes import *

pygame.init()

#global variables
display_width = 1366
display_height = 768
player1 = player()
wall1 = wall()

#color variables
black = (0,0,0)
white = (255,255,255)

# main pygame variables
gameDisplay = pygame.display.set_mode((display_width,display_height))
#pygame.display.toggle_fullscreen()
clock = pygame.time.Clock()


def menu():
    pass

def gameinit():
    #initialise player
    player1.x = 0.0
    player1.y = 0.0
    player1.health = 100
    player1.speed = 0.0
    #etc
    wall1.x = 200
    wall1.y = 300
            

def gameloop():
   
    quit = False
    while quit == False:

   	    #events
        for event in pygame.event.get():
        
            # event - quit
            if event.type == pygame.QUIT:
                quit = True
            if event.type == pygame.KEYDOWN:

                #close game if backspace is pressed
                #(made this shortcut as game cannot be closed in full screen)
                if event.key == pygame.K_BACKSPACE:
                    quit = True
                #toggles fulscreen mode when pressing esc
                if event.key == pygame.K_ESCAPE:
                    pygame.display.toggle_fullscreen()

            #used for debugging
            #print event

        #this event runs when any key is pressed
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_LEFT] == True:
            player1.move('left')
        if pressed_keys[pygame.K_RIGHT] == True:
            player1.move('right')
        if pressed_keys[pygame.K_UP] == True:
            player1.move('up')
        if pressed_keys[pygame.K_DOWN] == True:
            player1.move('down')
              


        #logic
        if collide(player1,wall1) == False:
            player1.inertia()
        else:
            player1.speedx *= -0.1 
            player1.speedy *= -0.1
            player1.inertia()
            player1.speedx = 0
            player1.speedy = 0
            
        print collide(player1,wall1)

	    #map draw
        gameDisplay.fill(white)
        draw(player1)
        draw(wall1)
        pygame.display.update()
        clock.tick(60)





def gameexit():
    #runs before closing the window
    pygame.quit()
    quit()


def draw(obj):
    #used to draw any object sent to it on the screen
    gameDisplay.blit(obj.image, (obj.x,obj.y))

def collide(plyr,obj):

    if obj.can_collide == False :
        return False
    elif ( ((plyr.x + plyr.speedx) >= obj.x) and ((plyr.x + plyr.speedx) <= (obj.x + obj.w)) ) and \
         ( ((plyr.y + plyr.speedy) >= obj.y) and ((plyr.y + plyr.speedy) <= (obj.y + obj.h)) ):
        return True
    elif ( ((plyr.x + plyr.w + plyr.speedx) >= obj.x) and ((plyr.x + plyr.w + plyr.speedx) <= (obj.x + obj.w)) ) and \
         ( ((plyr.y + plyr.speedy) >= obj.y) and ((plyr.y + plyr.speedy) <= (obj.y + obj.h)) ):
        return True
    elif ( ((plyr.x + plyr.speedx) >= obj.x) and ((plyr.x + plyr.speedx) <= (obj.x + obj.w)) ) and \
         ( ((plyr.y + plyr.h + plyr.speedy) >= obj.y) and ((plyr.y + plyr.h + plyr.speedy) <= (obj.y + obj.h)) ):
        return True
    elif ( ((plyr.x + plyr.w + plyr.speedx) >= obj.x) and ((plyr.x + plyr.w + plyr.speedx) <= (obj.x + obj.w)) ) and \
         ( ((plyr.y + plyr.h + plyr.speedy) >= obj.y) and ((plyr.y + plyr.h + plyr.speedy) <= (obj.y + obj.h)) ):
        return True
    else:
        return False


# main code
gameinit()
gameloop()
gameexit()



