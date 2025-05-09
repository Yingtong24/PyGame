import pygame
from pygame.locals import*
import time
pygame.init()
WIDTH=1000
HEIGHT=800
screen=pygame.display.set_mode((WIDTH,HEIGHT))
xpos=500
ypos=400
im=pygame.image.load("bedroom.jpg")
im2=pygame.image.load("duck.png")
while ypos<800:
    screen.blit(im,(0,0))
    screen.blit(im2,(xpos, ypos))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    
    ypos+=2
























    pygame.display.update()
