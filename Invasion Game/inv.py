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
    pygame.display.update()
