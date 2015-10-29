import pygame
from classes import *

pygame.init()

#global variables
display_width = 1366
display_height = 768
player1 = player()

objects = [] 

#map variables
mapx = 0.0
mapy = 0.0
mapspeedx = 4
mapspeedy = 0
redx1 = 100
redy1 = 100
redx2 = display_width - 100
redy2 = display_height - 100
map_edge_x = 2200
map_edge_y = 2200

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
    player1.x = 250.0
    player1.y = 250.0
    player1.health = 100
    player1.speed = 0.0
    #etc

    
    load_map('temp_name')           

def gameloop():
   
    quit = False
    
    #global keyword required to CHANGE the global variable's value
    #not required to READ the variable's value
    global mapspeedx
    global mapspeedy

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
            if collide(player1,obj,mapx,mapy) == True:
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

                if player1.x <= redx2 :
                    #player is inside red box
                    mapspeedx = 0
                else:
                    #player is outside red box

                    if (-1*mapx) + display_width < map_edge_x:
                        #some portion of map is hidden to the right of the screen
                    
                        mapspeedx = -1*player1.speedx 
                        player1.speedx = 0
                        #move map to left instead of moving player to right and stop the player

                    elif (-1*mapx) + display_width == map_edge_x:
                        #no portion of map left on the right of the screen

                        player1.speedx = -1*mapspeedx
                        mapspeedx = 0
                        #set player speed to reverse of map speed and stop map from moving

            if player1.speedx < 0:
                #player moving towards left

                if player1.x >= redx1 :
                    #player is inside red box
                    mapspeedx = 0
                else:
                    #player is outside red box

                    if mapx < 0:
                        #some portion of map is hidden to the left of the screen
                    
                        mapspeedx = -1*player1.speedx 
                        player1.speedx = 0
                        #move map to right instead of moving player to left and stop the player

                    elif mapx == 0:
                        #no portion of map left on the left of the screen

                        player1.speedx = -1*mapspeedx
                        mapspeedx = 0
                        #set player speed to reverse of map speed and stop map from moving

            if player1.speedy > 0:
                #player moving downwards

                if player1.y <= redy2 :
                    #player is inside red box
                    mapspeedy = 0
                else:
                    #player is outside red box

                    if (-1*mapy) + display_height < map_edge_y:
                        #some portion of map is hidden below the screen
                    
                        mapspeedy = -1*player1.speedy 
                        player1.speedy = 0
                        #move map upwards instead of moving player downwards and stop the player

                    elif (-1*mapy) + display_height == map_edge_y:
                        #no portion of map left below the screen

                        player1.speedy = -1*mapspeedy
                        mapspeedy = 0
                        #set player speed to reverse of map speed and stop map from moving

            if player1.speedy < 0:
                #player moving upwards

                if player1.y >= redy1 :
                    #player is inside red box
                    mapspeedy = 0
                else:
                    #player is outside red box

                    if mapy < 0:
                        #some portion of map is hidden above the screen
                    
                        mapspeedy = -1*player1.speedy 
                        player1.speedy = 0
                        #move map downward instead of moving player upward and stop the player

                    elif mapy == 0:
                        #no portion of map left above the screen

                        player1.speedy = -1*mapspeedy
                        mapspeedy = 0
                        #set player speed to reverse of map speed and stop map from moving


        else:
            #player is touching something
            
            
            if player1.speedx != 0:
                #player moving in x axis

                if player1.x <= redx2 or player1.x >= redx1:
                    #player is inside red box
                    player1.speedx *= -0.1 
                    mapspeedx = 0
                else:
                    #player is on red box

                    if ((-1*mapx) + display_width < map_edge_x) or (mapx <0):
                        #map is not scrolled all the way
                    
                        mapspeedx *= -0.1 
                        player1.speedx = 0
                        
                    elif ((-1*mapx) + display_width == map_edge_x) or (mapx == 0):
                        #either of map edge is touching screen edge

                        player1.speedx *= -0.1
                        mapspeedx = 0

            if player1.speedy != 0:
                #player moving in y axis

                if player1.y <= redy2 or player1.y >= redy1 :
                    #player is inside red box
                    player1.speedy *= -0.1
                    mapspeedy = 0
                else:
                    #player is outside red box

                    if ((-1*mapy) + display_height < map_edge_y) or (mapy < 0):
                        #map is not scrolled all the way
                    
                        mapspeedy *= -0.1 
                        player1.speedy = 0
                        
                    elif ((-1*mapy) + display_height == map_edge_y) or (mapy == 0):
                        #either of map edges is touching screen edge

                        player1.speedy *= -0.1
                        mapspeedy = 0
                                               
            player1.inertia()
            inertia_map()
            player1.speedx = 0
            player1.speedy = 0
            mapspeedx = 0
            mapspeedy = 0

        player1.inertia()
        inertia_map()



        '''
        if is_collided == False:
            player1.inertia()
        else:
            player1.speedx *= -0.1 
            player1.speedy *= -0.1
            player1.inertia()
            player1.speedx = 0
            player1.speedy = 0
        ''' 
    

	    #map draw-----------------------------------------------------------------------------------------------------
        gameDisplay.fill(white)
        draw_map(mapx,mapy)
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
    #temporary values
    #these values will be loaded from a text file later

    wx = 200
    wy = 200
    a = 0
    for i in range(1,61):
        wl = wall()
        wl.x = wx + a
        wl.y = wy
        a += wl.w
        objects.append(wl)

    wx = 100
    wy = 1200
    a = 0
    for i in range(1,61):
        wl = wall()
        wl.x = wx + a
        wl.y = wy
        a += wl.w
        objects.append(wl)

    wx = 150
    wy = 300
    a = 0
    for i in range(1,61):
        wl = wall()
        wl.x = wx 
        wl.y = wy + a
        a += wl.h
        objects.append(wl)

    wx = 1250
    wy = 300
    a = 0
    for i in range(1,61):
        wl = wall()
        wl.x = wx 
        wl.y = wy + a
        a += wl.h
        objects.append(wl)
    door1 = door()
    door1.x = 110
    door1.y = 240
    objects.append(door1)
    

def draw_map(x,y):
    for obj in objects:
        draw(obj,x,y)
    draw(player1,0,0)
    

def inertia_map():
    #same as player inertia
    brakespeed = 0.5
    global mapspeedx
    global mapspeedy
    global mapx
    global mapy

    if mapspeedx > 0:
        mapspeedx = (mapspeedx*1000 - brakespeed*1000)/1000
    elif mapspeedx < 0:
        mapspeedx = (mapspeedx*1000 + brakespeed*1000)/1000

    if mapspeedy > 0:
        mapspeedy = (mapspeedy*1000 - brakespeed*1000)/1000
    elif mapspeedy < 0:
        mapspeedy = (mapspeedy*1000 + brakespeed*1000)/1000

    mapx += mapspeedx
    mapy += mapspeedy

# main code
gameinit()
gameloop()
gameexit()



