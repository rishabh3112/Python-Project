import pygame
import time
from classes import * #for player2
breakspeed = 0.5
objects = []
display_width = 1366
display_height = 768
white = (255,255,255)
black=(0,0,0)
blue = (0,0,255)
red = (255,0,0)
gameDisplay = pygame.display.set_mode((display_width,display_height))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None,50)

def message(msg,color,mesx,mesy):
    
    screen = font.render(msg,True,color)
    gameDisplay.blit(screen,[mesx,mesy])

class gamemap2:
    def __init__(self):
        self.map2_x = 0
        self.map2_y = 0
        self.map2_edgex = 2400
        self.map2_edgey = 2400
        self.map2speedx = 0
        self.map2speedy = 0
        self.mapp = False
        
        self.maxspeed = 7   #defaul speed
        self.imgx = display_width-200


map2 = gamemap2()
player2 = player()
def game2intro():
    start = True
    load=0
    while start:
         for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 gameexit()
             if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    load = 1
                    start = False
                 
         gameDisplay.fill(black)
         if load ==1:
              message("LOADING...",red,300,500)
              pygame.display.update()
         i=pygame.image.load('images/background.png')
         i=pygame.transform.scale(i, (1000, 700))
         gameDisplay.blit(i, (100,0))     
         message('welcome to "SPAIN BULL RACE"',blue,300,300)
         message('PRESS c TO continue THE GAME',black,400,400)
            
           
         pygame.display.update()
         clock.tick(60)
def gameloop2():
    gameexit = False
    while gameexit == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                map2_exit()
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_LEFT] == True:
            player2.move('left')
        if pressed_keys[pygame.K_RIGHT] == True:
            player2.move('right')
        if pressed_keys[pygame.K_UP] == True:
            player2.move('up')
        if pressed_keys[pygame.K_DOWN] == True:
            player2.move('down')
            

        is_collided = False
        for obj in objects:
           
            if collide(player2,obj,map2.map2_x,map2.map2_y) == True:
                is_collided = True
    


        if is_collided == False: #doesnt collide any thing
            if -1*(map2.map2_x) + display_width <= map2.map2_edgex:
                map2.map2speedx = -map2.maxspeed
                #print(map2.maxwid)
                print(map2.map2_x)
                if (map2.map2_x <= -2300 and map2.map2_x >= -2400) or (map2.mapp == True):
                    map2.map2speedx = 0
                    map2.maxspeed = 0
                    
                    if player2.speedx >0:#moving right
                        if player2.x < map2.imgx:
                            map2.map2speedx = 0
                        else:
                            map2.map2speedx = -1*(player2.speedx)
                            player2.speedx = 0
                    map2.mapp = True     

                          

                        



            
            
        else:
            if obj.name=="bull":
                print('bull')
            a = True
            while a == True:
                map2.map2speedx = 0
                gameDisplay.fill(black)
                
                message("DEAD",red,300,300)
                message("PRESS r TO REPLAY , q TO QUIT",white,400,400)
                
                pygame.display.update()
                clock.tick(60)
                
                
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_r:
                            map2.map2_x = 0
                            map2.map2_y = 0
                            a = False
                            load_map2("map2")
                            gameloop2()
                        else:
                            if event.key == pygame.K_q:
                                a = False
                                map2_exit()
                
                    
        player2.inertia()
        inertiamap2()


        gameDisplay.fill(white)
        draw_map(map2.map2_x,map2.map2_y)
        pygame.display.update()
        clock.tick(60)

        
    

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
def draw(obj,x,y):
    gameDisplay.blit(obj.image, (obj.x + x,obj.y + y))
def draw_map(x,y):
    for obj in objects:
        draw(obj,x,y)
    draw(player2,0,0)

def inertiamap2():
    #same as map1
    if map2.map2speedx > 0:
        map2.map2speedx = (map2.map2speedx*1000 - brakespeed*1000)/1000
    elif map2.map2speedx < 0:
        map2.map2speedx = (map2.map2speedx*1000 + brakespeed*1000)/1000

    if map2.map2speedy > 0:
        map2.map2speedy = (map2.map2speedy*1000 - brakespeed*1000)/1000
    elif map2.map2speedy < 0:
        map2.map2peedy = (map2.map2speedy*1000 + brakespeed*1000)/1000

    map2.map2_x += map2.map2speedx
    map2.map2_y += map2.map2speedy

def load_map2(name):
    path = 'maps/' + name + '.txt'
    filein = open(path,'r')

    line = filein.readline()
    a = line.split()
    player2.x = float(a[0])
    player2.y = float(a[1])
    map2.map2_edgex = int(a[2])
    map2.map2_edgey = int(a[3])
    l = int(a[4])

    w = 0.0
    h = 0.0

    for i in range(1,l+1):

        line = filein.readline()
        

        for o in line:

            if o == 'b':
                bl = bull(w,h)
                objects.append(bl)
            elif o == 'c':
                ca = car(w,h)
                objects.append(ca)
            elif o == 's':
                sh = shop(w,h)
                objects.append(sh)
            elif o == 'r':
                rd = road(w,h)
                objects.append(rd)
            
            w += 30
            
        h += 30
        w = 0.0


    
    filein.close()
def map2_exit():
    pygame.quit()
    quit()
game2intro()
load_map2("map2")
gameloop2()  