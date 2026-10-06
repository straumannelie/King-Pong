import pygame
from random import *

pygame.init()

win=pygame.display.set_mode((1000,750))
pygame.display.set_caption("KING PONG")
bg=pygame.image.load('download.png')
kong=pygame.image.load('kong.png').convert_alpha()
kong=pygame.transform.scale(kong,(kong.get_width()*4,kong.get_height()*4))
godzilla=pygame.image.load('godzilla.png').convert_alpha()
godzilla=pygame.transform.scale(godzilla,(godzilla.get_width()*4,godzilla.get_height()*4))
ballbounce=pygame.mixer.Sound('Ballbounce.wav')
victory=pygame.mixer.Sound('Victory.wav')
loose=pygame.mixer.Sound('Loosepoint.wav')
pygame.mixer.music.load('Music.wav')
pygame.mixer.music.play(-1)


class playerone(object):
    def __init__(self, x: int, y: int,width: int, height: int) -> None:
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.vel=3

    def draw(self,win: pygame.Surface) -> None:
        pygame.draw.rect(win,(12,162,139),(self.x,self.y,self.width,self.height))

class playertwo(object):
    def __init__(self, z: int, t: int,width: int, height: int) -> None:
        self.z=z
        self.t=t
        self.width=width
        self.height=height
        self.vel=3

    def draw(self,win: pygame.Surface) -> None:
        pygame.draw.rect(win,(153,0,0),(self.z,self.t,self.width,self.height))

class Ball(object):
    def __init__(self,a: int,b: int,radius: int,color: tuple[int, int, int],velx: int,vely: int,facingx: int,facingy: int) -> None:
        self.a=a
        self.b=b
        self.radius=radius
        self.color=(0,0,0)
        self.velx=velx
        self.vely=vely
        self.facingx=facingx
        self.facingy=facingy

    def draw(self,win: pygame.Surface) -> None:
        pygame.draw.circle(win, self.color, (self.a,self.b), self.radius)

def redrawGameWindow() -> None:
    win.blit(bg, (0,0))
    win.blit(kong, kong.get_rect(center=(two.z//2,two.t+two.height//2)))
    win.blit(godzilla, godzilla.get_rect(center=((one.x+one.width+1000)//2,one.y+one.height//2)))
    so=font.render(str(scoreone),1,(0,0,0))
    st=font.render(str(scoretwo),1,(0,0,0))
    vic=font2.render('!Victory!',1,(5,5,5))
    if Victoryimage==True:
        win.blit(vic, vic.get_rect(midtop=(500,200)))    
    win.blit(so, (550,50))
    win.blit(st, (400,50))
    one.draw(win)
    two.draw(win)
    ball.draw(win)
    pygame.display.update()


#mainloop
font=pygame.font.SysFont('krungthep',60,True)
font2=pygame.font.SysFont('krungthep',80,True,True)
Victoryimage=False
p=randint(0,1)
if p==0:
    p=-1
one = playerone(825,225, 25,200)
two=playertwo(150,225,25,200)
ball=Ball(500,375,25,(0,0,0),3,0,1,p)
scoreone=0
scoretwo=0
tap=0
Ballcenter=True
run = True
clock=pygame.time.Clock()
while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if Ballcenter==True:
        ball.velx=0
        ball.vely=0

    if scoreone==5 or scoretwo==5:
        victory.play()
        Ballcenter=True
        Victoryimage=True
        scoreone=0
        scoretwo=0
        

    if ball.b-ball.radius<one.y+one.height and ball.b+ball.radius>one.y and ball.a==800 and ball.facingx==1:
        ballbounce.play()
        ball.facingx=-1
        ball.vely=randint(0,4)
        tap+=1
        if tap==5: ball.velx+=1
        if tap==10: ball.velx+=1
        
    if ball.b-ball.radius<two.t+two.height and ball.b+ball.radius>two.t and ball.a==200 and ball.facingx==-1:
        ballbounce.play()
        ball.facingx=1
        ball.vely=randint(0,4)
        tap+=1
        if tap==5: ball.velx+=1
        if tap==10: ball.velx+=1

    if ball.a<20:
        scoreone+=1
        loose.play()
        Ballcenter=True
        ball.velx=0
        ball.vely=0
        ball.a=500
        ball.b=375
        ball.facingx=-1
        tap=0
    if ball.a>970:
        scoretwo+=1
        loose.play()
        Ballcenter=True
        ball.velx=0
        ball.vely=0
        ball.a=500
        ball.b=375
        ball.facingx=1
        tap=0
    if ball.b<20:
        ball.facingy=1
    if ball.b>720:
        ball.facingy=-1

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        if one.y-one.vel<0:
            one.y=0
        else:
            one.y-=one.vel

    if keys[pygame.K_DOWN]:
        if one.y+one.vel+one.height>750:
            one.y=750-one.height
        else:
            one.y+=one.vel

    if keys[pygame.K_z]:
        if two.t-two.vel<0:
            two.t=0
        else:
            two.t-=two.vel

    if keys[pygame.K_s]:
        if two.t+two.vel+two.height>750:
            two.t=750-two.height
        else:
            two.t+=two.vel
    if keys[pygame.K_SPACE] and Ballcenter==True:
        ball.velx=3
        Ballcenter=False
        Victoryimage=False

    ball.a+=ball.velx*ball.facingx
    ball.b+=ball.vely*ball.facingy
    redrawGameWindow()

pygame.quit()

