import pygame
import random
import time
from pygame.locals import *
pygame.init()
WIDTH=1000
HEIGHT=1000
screen=pygame.display.set_mode((WIDTH, HEIGHT))
bg=pygame.image.load("bg.jpg")

#Bin Class
class bin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("bin.png")
        self.rect=self.image.get_rect()
bin2=bin()
asprite=pygame.sprite.Group()
asprite.add(bin2)

run=True
while run:
    for event in pygame.event.get():
        if event.type == QUIT:
            run=False
    screen.blit(bg, (0, 0))
    asprite.draw(screen)
    pygame.display.update()
pygame.quit()