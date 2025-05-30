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
lftduck=100
rghtduck=100
lduck=pygame.transform.scale(pygame.image.load("left_duck.png"), (200,200))
rduck=pygame.transform.scale(pygame.image.load("right_duck.png"), (150,150))
#Class for the Ducks
class ducks(pygame.sprite.Sprite):
    def __init__(self, image, xpos, ypos):
        super().__init__()
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.x=xpos
        self.rect.y=ypos
lftduck=ducks(lduck, 100,400)
rghtduck=ducks(rduck, 750,400)
sgroup=pygame.sprite.Group()
sgroup.add(lftduck)
sgroup.add(rghtduck)
run=True
while run:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()

    screen.blit(pond, (0,0))
    sgroup.draw(screen)
    pygame.display.update()
