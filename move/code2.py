import pygame
from pygame.locals import*
import time
pygame.init()
WIDTH=1000
HEIGHT=800
screen=pygame.display.set_mode((WIDTH,HEIGHT))
listok=[False, False, False, False]
xpos=500
ypos=400
im=pygame.image.load("bedroom.jpg")
im2=pygame.image.load("duck.png")
while ypos<800:
    screen.blit(im,(0,0))
    screen.blit(im2,(xpos, ypos))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
        if event.type==pygame.KEYDOWN:
            if event.key==K_UP:
                listok[0]=True
            elif event.key==K_DOWN:
                listok[1]=True
            elif event.key==K_LEFT:
                listok[2]=True
            elif event.key==K_RIGHT:
                listok[3]=True
        if event.type==pygame.KEYUP:
            if event.key==K_UP:
                listok[0]=False
            elif event.key==K_DOWN:
                listok[1]=False
            elif event.key==K_LEFT:
                listok[2]=False
            elif event.key==K_RIGHT:
                listok[3]=False
    if listok[0]:
        ypos-=5
    elif listok[1]:
        ypos+=5
    elif listok[2]:
        xpos-=5
    elif listok[3]:
        xpos+=5
            
    ypos+=1
    time.sleep(0.01)
print("GAME OVER")
