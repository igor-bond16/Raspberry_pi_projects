import pygame
from pygame.locals import *
import math

def sgn(a):
    if(a > 0):return 1
    return -1

RED = (255,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
BLUE = (0,0,255)
WIDTH = 640
HEIGHT = 480
pygame.init()
surface = pygame.display.set_mode((WIDTH,HEIGHT))
bx1 = 2
by1 = 3
br = 10
mx = WIDTH/2
my = HEIGHT-64
bx = mx-bx1*80
by = my-by1*80
mw = 96
mh = 16
tw = 48
th = 24
tx = []
ty = []

for i in range(40):
    tx.append((i%10)*(tw+4)+96)
    ty.append(int(i/10)*(th+4)+64)
    
pygame.joystick.init()
joystick_count = pygame.joystick.get_count()
if joystick_count == 0:
    print("Error:joystick not found")
joystick_id = 0
joystick = pygame.joystick.Joystick(joystick_id)
joystick.init()
myfont = pygame.font.Font(None,70)
message = ""
myclock = pygame.time.Clock()
endflag = 0

while endflag==0:
    for event in pygame.event.get():
        if event.type == QUIT:
            endflag=1
        
    ax = joystick.get_axis(0)
    if math.fabs(ax) < 0.2:
        ax=0
    mx += (ax*10)
    if mx<mw/2:
        mx=mw/2
    if mx>(WIDTH-(mw/2)):
        mx=(WIDTH-(mw/2))
    x = bx + bx1
    y = by + by1
    if x<br or x>(WIDTH-br):
        bx1=-bx1
    if y<br:
        by1=-by1
    if y>HEIGHT:
        bx1 = 0
        by1 = 0
        message = "Game Over"

    dx = mx-x
    dy = my-y
    if dy==0:
        dy=1
    if math.fabs(dx)<(mw/2+br) and math.fabs(dy)<(mh/2+br):
        if math.fabs(dx/dy)>(mw/mh):
            bx1 = -bx1
            bx = mx -sgn(dx)*(mw/mh)
        else:
            bx1 = -dx/10
            by1 = -by1
            by = my - sgn(dy)*(mh/2+br)
            
    for i in range(len(tx)):
        dx = tx[i]-x
        dy = ty[i]-y
        if dy==0:
            dy=1
        if math.fabs(dx)<(tw/2+br) and math.fabs(dy)<(th/2+br):
            if math.fabs(dx/dy)>(tw/th):
                bx = -bx1
                bx = tx[i]-sgn(dx)*(th/2+br)
            else:
                by1 = -by1
                by = ty[i]-sgn(dy)*(th/2+br)
            tx.pop(i)
            ty.pop(i)
            break
        
    bx += bx1
    by += by1
    surface.fill(BLUE)
    for i in range(len(tx)):
        pygame.draw.rect(surface,GREEN,(tx[i]-(tw/2),ty[i]-(th/2),tw,th))
    
    pygame.draw.rect(surface,WHITE,(mx-int(mw/2),my-int(mh/2),mw,mh))
    pygame.draw.circle(surface,RED,(int(bx),int(by)),br)
    bitmaptext = myfont.render(message,True,WHITE)
    surface.blit(bitmaptext,(200,300))
    pygame.display.update()
    myclock.tick(60)   
pygame.quit()

