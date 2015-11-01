import pygame
from classes import *

pygame.init()

#global variables
display_width = 1366
display_height = 768
player1 = player()
map1 = gamemap(display_width,display_height)
objects = [] 

#color variables
black = (0,0,0)
white = (255,255,255)
blue=(0,0,255)

# main pygame variables
gameDisplay = pygame.display.set_mode((display_width,display_height))
#pygame.display.toggle_fullscreen()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None,50)
def menu():
    pass
#
def message(msg,color,mesx,mesy):
    
    screen = font.render(msg,True,color)
    gameDisplay.blit(screen,[mesx,mesy])
def gameintro():
    start = True
    while start:
         for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 gameexit()
             if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    start = False
                 
         gameDisplay.fill(black)
         message('WELCOME TO THE BEST GAME EVER',blue,300,500)
         message('PRESS s TO START THE GAME',white,400,700)
            
           
         pygame.display.update()
         clock.tick(60)
def gameinit():
    load_map('level1')           

def gameloop():
   
    quit = False
    
    while quit == False:


        is_O_pressed = False
   	    #events---------------------------------------------------------------------------------------------------
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
                if event.key == pygame.K_o:
                    is_O_pressed = True
                    
                    

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
        
        
              


        #logic------------------------------------------------------------------------------------------------------

        is_collided = False
        for obj in objects:
            #check collision with every object on the map
            if collide(player1,obj,map1.mapx,map1.mapy) == True:
                is_collided = True
                if obj.name == 'door':
                    if is_O_pressed == True:
                        obj.can_collide = False
                        is_O_pressed = False
                break
        
            
        
        if is_collided == False:
            #player is not touching anything

            if player1.speedx > 0:
                #player moving towards right

                if player1.x < map1.redx2 :
                    #player is inside red box
                    map1.mapspeedx = 0
                else:
                    #player is outside red box

                    if (-1*map1.mapx) + display_width < map1.map_edge_x:
                        #some portion of map is hidden to the right of the screen
                    
                        map1.mapspeedx = -1*player1.speedx 
                        player1.speedx = 0
                        #move map to left instead of moving player to right and stop the player

                    elif (-1*map1.mapx) + display_width == map1.map_edge_x:
                        #no portion of map left on the right of the screen

                        player1.speedx = -1*map1.mapspeedx
                        map1.mapspeedx = 0
                        #set player speed to reverse of map speed and stop map from moving

            if player1.speedx < 0:
                #player moving towards left
               
                if player1.x > map1.redx1 :
                    #player is inside red box
                    map1.mapspeedx = 0
                else:
                    #player is outside red box

                    if map1.mapx < 0:
                        #some portion of map is hidden to the left of the screen
                    
                        map1.mapspeedx = -1*player1.speedx 
                        player1.speedx = 0
                        #move map to right instead of moving player to left and stop the player

                    elif map1.mapx == 0:
                        #no portion of map left on the left of the screen
                        
                        player1.speedx = -1*map1.mapspeedx
                        map1.mapspeedx = 0
                        #set player speed to reverse of map speed and stop map from moving

            if player1.speedy > 0:
                #player moving downwards

                if player1.y < map1.redy2 :
                    #player is inside red box
                    map1.mapspeedy = 0
                else:
                    #player is outside red box

                    if (-1*map1.mapy) + display_height < map1.map_edge_y:
                        #some portion of map is hidden below the screen
                    
                        map1.mapspeedy = -1*player1.speedy 
                        player1.speedy = 0
                        #move map upwards instead of moving player downwards and stop the player

                    elif (-1*map1.mapy) + display_height == map1.map_edge_y:
                        #no portion of map left below the screen

                        player1.speedy = -1*map1.mapspeedy
                        map1.mapspeedy = 0
                        #set player speed to reverse of map speed and stop map from moving

            if player1.speedy < 0:
                #player moving upwards

                if player1.y > map1.redy1 :
                    #player is inside red box
                    map1.mapspeedy = 0
                else:
                    #player is outside red box

                    if map1.mapy < 0:
                        #some portion of map is hidden above the screen
                    
                        map1.mapspeedy = -1*player1.speedy 
                        player1.speedy = 0
                        #move map downward instead of moving player upward and stop the player

                    elif map1.mapy == 0:
                        #no portion of map left above the screen

                        player1.speedy = -1*map1.mapspeedy
                        map1.mapspeedy = 0
                        #set player speed to reverse of map speed and stop map from moving


        else:
            #player is touching something
            
            
            if player1.speedx != 0:
                #player moving in x axis

                if player1.x <= map1.redx2 or player1.x >= map1.redx1:
                    #player is inside red box
                    player1.speedx *= -0.1 
                    map1.mapspeedx = 0
                else:
                    #player is on red box

                    if ((-1*map1.mapx) + display_width < map1.map_edge_x) or (map1.mapx <0):
                        #map is not scrolled all the way
                    
                        map1.mapspeedx *= -0.1 
                        player1.speedx = 0
                        
                    elif ((-1*map1.mapx) + display_width == map1.map_edge_x) or (map1.mapx == 0):
                        #either of map edge is touching screen edge

                        player1.speedx *= -0.1
                        map1.mapspeedx = 0

            if player1.speedy != 0:
                #player moving in y axis

                if player1.y <= map1.redy2 or player1.y >= map1.redy1 :
                    #player is inside red box
                    player1.speedy *= -0.1
                    map1.mapspeedy = 0
                else:
                    #player is outside red box

                    if ((-1*map1.mapy) + display_height < map1.map_edge_y) or (map1.mapy < 0):
                        #map is not scrolled all the way
                    
                        map1.mapspeedy *= -0.1 
                        player1.speedy = 0
                        
                    elif ((-1*map1.mapy) + display_height == map1.map_edge_y) or (map1.mapy == 0):
                        #either of map edges is touching screen edge

                        player1.speedy *= -0.1
                        map1.mapspeedy = 0
                                               
            player1.inertia()
            map1.inertia()
            player1.speedx = 0
            player1.speedy = 0
            map1.mapspeedx = 0
            map1.mapspeedy = 0

        player1.inertia()
        map1.inertia()

	    #map draw-----------------------------------------------------------------------------------------------------
        gameDisplay.fill(white)
        draw_map(map1.mapx,map1.mapy)
        pygame.display.update()
        clock.tick(60)





def gameexit():
    #runs before closing the window
    pygame.quit()
    quit()


def draw(obj,x,y):
    #used to draw any object sent to it on the screen
    gameDisplay.blit(obj.image, (obj.x + x,obj.y + y))

def collide(plyr,obj,mapx,mapy):

    if obj.can_collide == False :
        return False
    elif ( ((plyr.x + plyr.speedx) >= obj.x + mapx) and ((plyr.x + plyr.speedx) <= (obj.x + obj.w + mapx)) ) and \
         ( ((plyr.y + plyr.speedy) >= obj.y + mapy) and ((plyr.y + plyr.speedy) <= (obj.y + obj.h + mapy)) ):
        return True
    elif ( ((plyr.x + plyr.w + plyr.speedx) >= obj.x + mapx) and ((plyr.x + plyr.w + plyr.speedx) <= (obj.x + obj.w + mapx)) ) and \
         ( ((plyr.y + plyr.speedy) >= obj.y + mapy) and ((plyr.y + plyr.speedy) <= (obj.y + obj.h + mapy)) ):
        return True
    elif ( ((plyr.x + plyr.speedx) >= obj.x + mapx) and ((plyr.x + plyr.speedx) <= (obj.x + obj.w + mapx)) ) and \
         ( ((plyr.y + plyr.h + plyr.speedy) >= obj.y + mapy) and ((plyr.y + plyr.h + plyr.speedy) <= (obj.y + obj.h + mapy)) ):
        return True
    elif ( ((plyr.x + plyr.w + plyr.speedx) >= obj.x + mapx) and ((plyr.x + plyr.w + plyr.speedx) <= (obj.x + obj.w + mapx)) ) and \
         ( ((plyr.y + plyr.h + plyr.speedy) >= obj.y + mapy) and ((plyr.y + plyr.h + plyr.speedy) <= (obj.y + obj.h + mapy)) ):
        return True
    else:
        return False

def load_map(name):
    path = 'maps/' + name + '.txt'
    filein = open(path,'r')

    line = filein.readline()
    a = line.split()
    player1.x = float(a[0])
    player1.y = float(a[1])
    map1.map_edge_x = int(a[2])
    map1.map_edge_y = int(a[3])
    l = int(a[4])

    w = 0.0
    h = 0.0

    for i in range(1,l+1):

        line = filein.readline()
        #print line
        for o in line:

            if o == 'W':
                wl = wall(w,h)
                objects.append(wl)
            elif o == 'D':
                dr = door(w,h)
                objects.append(dr)
            
            w += 30

        h += 30
        w = 0.0

    filein.close()
  
def draw_map(x,y):
    for obj in objects:
        draw(obj,x,y)
    draw(player1,0,0)
    
# main code
gameintro()#intro loop run firstly
gameinit()
gameloop()
gameexit()
