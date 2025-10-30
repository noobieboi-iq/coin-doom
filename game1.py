import pygame as pg
import random

pg.init()
clock = pg.time.Clock()
screen =pg.display.set_mode((800, 800))

dx=400
dy=400

cx =random.randint(0,800)
cy =random.randint(0,800)

points =0

font =pg.font.SysFont('Comic Sans MS', 30)

def say(position, txt):
    text = font.render(txt, False, (0, 0, 0))
    screen.blit(text,position)

background =pg.image.load("pictures/background.png")

doomguy =pg.image.load("pictures/char.png")
doomguy =pg.transform.smoothscale(doomguy,(32,32))

token =pg.image.load("pictures/token.png")
token =pg.transform.smoothscale(token,(32,32))
        
screen.blit(token,(cx,cy))
alive =True

fps =144

timer =10
    
run = True
while run:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            run = False
    
    timer-=1/fps
    screen.blit(background,(0,0))
    
    if timer<=0:
        say((300,400),"Game Over")
        say((300,350),f"Score: {points}")
        
    else:
            
        k =pg.key.get_pressed()
        if k[pg.K_w]:
            dy-=1
        if k[pg.K_s]:
            dy+=1
        if k[pg.K_a]:
            dx-=1
        if k[pg.K_d]:
            dx+=1
        
        token_hitbox =screen.blit(token,(cx,cy))
        doomguy_hitbox =screen.blit(doomguy,(dx,dy))
    
        say((0,0),f"points: {points}")
    
        say((0,40),f"time left: {timer:.1f}")
        if doomguy_hitbox.colliderect(token_hitbox):
            points+=1
            alive=False
            timer=5
    
        if not alive:
            cx =random.randint(0,800)
            cy =random.randint(0,800)
            alive=True

    pg.display.flip()
    clock.tick(fps)