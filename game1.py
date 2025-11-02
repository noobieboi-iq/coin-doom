import pygame as pg
import random

pg.init()
clock = pg.time.Clock()
screen =pg.display.set_mode((800, 800))

fps =144

dx=400
dy=400

points =0

cx =random.randint(0,800)
cy =random.randint(0,800)


font =pg.font.SysFont('Comic Sans MS', 30)

def say(pos, txt):
    text = font.render(txt, False, (0, 0, 0))
    screen.blit(text,pos)

class Button:
    def __init__(self,size,pos,color):
        self.rect =pg.Rect(pos,size)
        self.color=color
    
    def is_hovering(self,mouse_pos):
        return self.rect.collidepoint(mouse_pos)
    
    def show(self, surface):
        pg.draw.rect(surface, self.color, self.rect)
        if self.is_hovering(pg.mouse.get_pos()):
            pg.draw.rect(surface,(255,255,0),self.rect,2)
        

background =pg.image.load("pictures/background.png")

doomguy =pg.image.load("pictures/char.png")
doomguy =pg.transform.smoothscale(doomguy,(32,32))

token =pg.image.load("pictures/token.png")
token =pg.transform.smoothscale(token,(32,32))
        
screen.blit(token,(cx,cy))
alive =True

restart_button =Button((40,50),(700,650),(255,0,0))

timer =2
    
run = True
while run:
    pressed=False
    for event in pg.event.get():     
        if event.type==pg.QUIT:
            run = False
            
        if event.type == pg.MOUSEBUTTONUP:
            pressed = True
            
            
    timer-=1/fps
    screen.blit(background,(0,0))
    
    if timer<=0:
        say((300,400),"Game Over")
        say((300,350),f"Score: {points}")
        say((550,650),"restart! ->")
        restart_button.show(screen)
        if restart_button.is_hovering(pg.mouse.get_pos()) and pressed:
            points =0
            timer =10
            alive =False
        
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
