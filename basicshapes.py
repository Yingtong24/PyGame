import pygame
pygame.init()
screen=pygame.display.set_mode((600,600))
#Colours
beige=(245, 239, 208)
blue=(199, 247, 255)
pink=(254, 217, 255)
purple=(221, 186, 245)
green=(204, 255, 227)
screen.fill(beige)
pygame.display.update()
over=True
while over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            over=False