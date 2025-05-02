import pygame
import time
pygame.init()
WIDTH=1000
HEIGHT=800
over=True
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("MERRY CHRISTMAS")
c1=(212,68,68)
c2=(68,212,130)
c3=(247,250,80)
c4=(64,233,255)
f1=pygame.font.SysFont("lexend", 60)
#Image 1
bgi1=pygame.image.load("tree2.jpg")
bgi1=pygame.transform.scale(bgi1, (WIDTH, HEIGHT))

while over==True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    text1=f1.render("MERRY", 1,c1)
    text2=f1.render("CHRISTMAS", 1,c2)
    screen.blit(bgi1, (0,0))
    screen.blit(text1, (450,350))
    screen.blit(text2, (400,400))
    pygame.display.update()
    time.sleep(5)

#Image 2
    bgi2=pygame.image.load("cover.jpg")
    bgi2=pygame.transform.scale(bgi2, (WIDTH, HEIGHT))
    f2=pygame.font.SysFont("garamond", 60)
    text3=f2.render("Ho Ho Ho", 1,c3)
    screen.blit(bgi2, (0,0))
    screen.blit(text3, (350,300))
    pygame.display.update()
    time.sleep(5)

#Image 3
    bgi3=pygame.image.load("duck.webp")
    bgi3=pygame.transform.scale(bgi3, (WIDTH, HEIGHT))
    f3=pygame.font.SysFont("garamond", 60)
    text4=f3.render("QUACKKKKKK", 1,c1)
    screen.blit(bgi3, (0,0))
    screen.blit(text4, (350,300))
    pygame.display.update()
    time.sleep(5)

#Image 4
    bgi4=pygame.image.load("tree.jpg")
    bgi4=pygame.transform.scale(bgi4, (WIDTH, HEIGHT))
    f4=pygame.font.SysFont("garamond", 60)
    text5=f4.render("Have a jolly good day", 1,c1)
    screen.blit(bgi4, (0,0))
    screen.blit(text5, (350,300))
    pygame.display.update()
    time.sleep(5)

pygame.quit()
