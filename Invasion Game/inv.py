import pygame
from pygame.locals import*
import os
pygame.font.init()
pygame.mixer.init()
screen=pygame.display.set_mode((1000,800))
healfnt=pygame.font.SysFont("Times New Roman", 50)
winfnt=pygame.font.SysFont("Times New Roman", 80)
speeduck=5
speedbullet=8
pond=pygame.transform.scale(pygame.image.load("pond.jpg"), (1000,800))
lftduckh=100
rghtduckh=100
lduck=pygame.transform.scale(pygame.image.load("left_duck.png"), (200,200))
rduck=pygame.transform.scale(pygame.image.load("right_duck.png"), (150,150))

border=pygame.Rect(500,0,5,800)

#Class for the Ducks
class ducks(pygame.sprite.Sprite):
    def __init__(self, image, xpos, ypos, speed):
        super().__init__()
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.x=xpos
        self.rect.y=ypos
        self.speed = speed
    def hmove(self, speed, player):
        self.rect.x+=speed
        if player==1:
            if self.rect.left<=0 or self.rect.right>=border.left:
                self.rect.move_ip(-speed, 0)
        if player==2:
            if self.rect.left<=border.right or self.rect.right>=1000:
                self.rect.move_ip(-speed, 0)
    def vmove(self, speed):
        self.rect.move_ip(0, speed)
        if self.rect.top<=0 or self.rect.bottom>=800:
            self.rect.move_ip(0,-speed)
#Function for Bullets
ldbullet=[]
rdbullet=[]
def bullet():
    for bullets in ldbullet:
        pygame.draw.rect(screen, "brown", bullets)
        bullets.x+=5
    for bullets in rdbullet:
        pygame.draw.rect(screen,"brown", bullets)
        bullets.x-=5
#Function for Damage
lefthit=pygame.USEREVENT+1
righthit=pygame.USEREVENT+2
def collide():
    global lftduckh, rghtduckh
    for bullets in ldbullet:
        if rghtduck.rect.colliderect(bullets):
            rghtduckh-=2
            ldbullet.remove(bullets)
        elif bullets.x>1000:
            ldbullet.remove(bullets)

    for bullets in rdbullet:
        if lftduck.rect.colliderect(bullets):
            lftduckh-=2
            rdbullet.remove(bullets)
        elif bullets.x>1000:
            rdbullet.remove(bullets)
    
    #Bullets collide together
    for bullet1 in ldbullet:
        for bullet2 in rdbullet:
            if bullet1.colliderect(bullet2):
                ldbullet.remove(bullet1)
            if bullet2.colliderect(bullet1):
                rdbullet.remove(bullet2)

lftduck = ducks(lduck, 100, 400, speed=2)
rghtduck = ducks(rduck, 750, 400, speed=-3)
sgroup=pygame.sprite.Group()
sgroup.add(lftduck)
sgroup.add(rghtduck)
run=True
while run:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
        #Bullet creation
        if event.type==KEYDOWN:
            if event.key==K_LCTRL:
                bullets=pygame.Rect(lftduck.rect.x+lftduck.rect.width, lftduck.rect.y+lftduck.rect.height//2,10,5)
                ldbullet.append(bullets)
            if event.key==K_RCTRL:
                bullets=pygame.Rect(rghtduck.rect.x, rghtduck.rect.y+rghtduck.rect.height//2,10,5)
                rdbullet.append(bullets)
        #if event.type==lefthit:

    press=pygame.key.get_pressed()
    
    #Player 1
    if press[K_a]:
        lftduck.hmove(-5, 1)
    if press[K_d]:
        lftduck.hmove(5, 1)
    if press[K_w]:
        lftduck.vmove(-5)
    if press[K_s]:
        lftduck.vmove(5)
    
    #Player 2
    if press[K_UP]:
        rghtduck.vmove(-5)
    if press[K_DOWN]:
        rghtduck.vmove(5)
    if press[K_LEFT]:
        rghtduck.hmove(-5, 2)
    if press[K_RIGHT]:
        rghtduck.hmove(5, 2)

    screen.blit(pond, (0,0))
    lifelduck=healfnt.render("Health: " + str(lftduckh), 1, "black")
    screen.blit(lifelduck, (10,10))
    liferduck=healfnt.render("Health: " + str(rghtduckh), 1, "black")
    screen.blit(liferduck, (750,10))

    pygame.draw.rect(screen, "yellow", border)
    sgroup.draw(screen)
    bullet()
    collide()
    if lftduckh<=0:
        txt=winfnt.render("Game over, right duck wins!!!", 1, "Black")
        screen.blit(txt, (600,10))
        pygame.display.update()
        pygame.time.delay(10000)
        run=False
    if rghtduckh<=0:
        txt=winfnt.render("Game over, left duck wins!!!", 1, "Black")
        screen.blit(txt, (200,10))
        pygame.display.update()
        pygame.time.delay(10000)
        run=False
    pygame.display.update()
