import pygame as pg
import random

pg.init()
clock = pg.time.Clock()
screen =pg.display.set_mode((800, 800))

dx=400
dy=400

cx =random.randint(0,800)
cy =random.randint(0,800)

tokens =0

font =pg.font.SysFont('Comic Sans MS', 30)

background =pg.image.load("pictures/background.png")

doomguy =pg.image.load("pictures/doom.png")
doomguy =pg.transform.smoothscale(doomguy,(32,32))

coin =pg.image.load("pictures/coin.png")
coin =pg.transform.smoothscale(coin,(32,32))
        
screen.blit(coin,(cx,cy))
alive =True

run = True
while run:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            run = False
            
    screen.blit(background,(0,0))
            
    k =pg.key.get_pressed()
    if k[pg.K_w]:
        dy-=1
    if k[pg.K_s]:
        dy+=1
    if k[pg.K_a]:
        dx-=1
    if k[pg.K_d]:
        dx+=1
        
    coin_hitbox =screen.blit(coin,(cx,cy))
    doomguy_hitbox =screen.blit(doomguy,(dx,dy))
    
    text = font.render(f"tokens: {tokens}", False, (0, 0, 0))
    screen.blit(text,(0,0))
    
    if doomguy_hitbox.colliderect(coin_hitbox):
        tokens+=1
        alive=False
    
    if not alive:
        cx =random.randint(0,800)
        cy =random.randint(0,800)
        alive=True

    pg.display.flip()
    clock.tick(144)