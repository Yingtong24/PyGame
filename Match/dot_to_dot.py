import pygame
pygame.init()
WIDTH=1000
HEIGHT=1000
screen=pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill("white")
ss=pygame.image.load("subway_surfers.png")
bb=pygame.image.load("block_blast.png")
gi=pygame.image.load("genshin_impact.webp")
m=pygame.image.load("minecraft.png")
r=pygame.image.load("roblox.png")
screen.blit("subway_surfers.png" ,(400,150))





pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()