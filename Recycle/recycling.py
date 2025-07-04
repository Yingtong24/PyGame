import pygame
import random
import time
from pygame.locals import *
pygame.init()
WIDTH=1000
HEIGHT=1000
st=time.time()
score=0
screen=pygame.display.set_mode((WIDTH, HEIGHT))
bg=pygame.image.load("bg.jpg")
fnt=pygame.font.SysFont("Lobster", 35)
fnt2=pygame.font.SysFont("Caveat", 50)
text=fnt2.render("Score ="+str(0), True, "black")


#Bin Class
class bin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("bin.png")
        self.rect=self.image.get_rect()
bin2=bin()
asprite=pygame.sprite.Group()
asprite.add(bin2)


#Class for Recyclable items
class recyclable(pygame.sprite.Sprite):
    def __init__(self, img):
        super().__init__()
        self.image=pygame.image.load(img)
        self.rect=self.image.get_rect()

ry=["pabag.png","cc.png","pencil.png"]
rcyble=pygame.sprite.Group()


#Class for Non-Recyclable Items
class nrecyclable(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("plbag.png")
        self.rect=self.image.get_rect()
nrcyble=pygame.sprite.Group()

#Creating recyclable and non-recyclable objects
for i in range(30):
    obj=recyclable(random.choice(ry))
    obj.rect.x=random.randint(0,1000)
    obj.rect.y=random.randint(0,1000)
    rcyble.add(obj)
    asprite.add(obj)

for i in range(15):
    obj=nrecyclable()
    obj.rect.x=random.randint(0,1000)
    obj.rect.y=random.randint(0,1000)
    nrcyble.add(obj)
    asprite.add(obj)

run=True
while run:
    for event in pygame.event.get():
        if event.type == QUIT:
            run=False
    tt=time.time()-st
    if tt>=30:
        if score>=15:
            text=fnt.render("Congrats, you win",1, "dark green")
        else:
            text=fnt2.render("You lost :( try again", 1, "red")
        screen.blit(text, (500,500))
    else:
        screen.blit(bg, (0, 0))
        ttxt=fnt2.render("Time Left: "+str(30-int(tt)), 1, "green")
        screen.blit(ttxt, (100,100))
        keys=pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            if bin2.rect.y>0:
                bin2.rect.y-=5
        if keys[pygame.K_LEFT]:
            if bin2.rect.x>0:
                bin2.rect.x-=5
        if keys[pygame.K_RIGHT]:
            if bin2.rect.x<1000:
                bin2.rect.x+=5
        if keys[pygame.K_DOWN]:
            if bin2.rect.y<1000:
                bin2.rect.y+=5


#Checking Collision
        #Recyclable Group
        recyclehit=pygame.sprite.spritecollide(bin2, rcyble, True)
        #Non Recyclable Group
        nrecyclehit=pygame.sprite.spritecollide(bin2, nrcyble, True)
#Scoring
        for item in recyclehit:
            score+=1
            text=fnt2.render("Score ="+str(score), True, "black")
        for item in nrecyclehit:
            score-=2
            text=fnt2.render("Score ="+str(score), True, "black")
        screen.blit(text,(0,0))

        asprite.draw(screen)
    pygame.display.update()
pygame.quit()
