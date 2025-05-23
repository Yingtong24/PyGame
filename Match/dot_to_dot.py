import pygame
pygame.init()
WIDTH=1000
HEIGHT=1000
screen=pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill("white")
ss=pygame.image.load("subway_surfers.png")
bb=pygame.image.load("block_blast.png")
gi=pygame.image.load("genshin_impact.jpg")
m=pygame.image.load("minecraft.png")
r=pygame.image.load("roblox.png")
screen.blit(ss ,(25,20))
screen.blit(bb ,(-50,220))
screen.blit(gi ,(25,420))
screen.blit(m ,(12,620))
screen.blit(r ,(25,820))
#Font for text
f=pygame.font.SysFont("Times New Roman", 50)
txt1=f.render("Minecraft", True, "Blue")
txt2=f.render("Subway Surfers", True, "Pink")
txt3=f.render("Roblox", True, "Red")
txt4=f.render("Block Blast", True, "Yellow")
txt5=f.render("Genshin Impact", True, "Green")

screen.blit( txt1,(600,75))
screen.blit( txt2,(600,275))
screen.blit( txt3,(600,475))
screen.blit( txt4,(600,675))
screen.blit( txt5,(600,875))


pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    event=pygame.event.poll()
    if event.type==pygame.MOUSEBUTTONDOWN:
            pos=pygame.mouse.get_pos()
            pygame.draw.circle(screen, "blue", (pos), 12.5, 0)
            pygame.display.update()
    if event.type==pygame.MOUSEBUTTONUP:
            pos2=pygame.mouse.get_pos()
            pygame.draw.line(screen, "blue", (pos), (pos2), 5)
            pygame.draw.circle(screen, "blue", (pos2), 12.5, 0)
            pygame.display.update()

        
