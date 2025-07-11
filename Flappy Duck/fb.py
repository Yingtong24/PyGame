import pygame
import random
import time
from pygame.locals import*
pygame.init()
WIDTH=864
HEIGHT=700
screen=pygame.display.set_mode((WIDTH, HEIGHT))
clock=pygame.time.Clock()
pygame.display.set_caption("FLAPPY BIRD")
#Font
fnt=pygame.font.SysFont("Cavier", 50)
#Gaming Variables
fps=60
gs=0
ss=2
fly=False
gover=False
score=0
pfreq=1500
last_pipe=pygame.time.get_ticks()-pfreq
pass_pipe=False
pgap=150
#Loading Images
scr=pygame.image.load("bg.png")
gr=pygame.image.load("ground.png")
lb=pygame.image.load("restart.png")
#Fuctiong to draw text
def drawtxt(txt, ft, tc, x, y):
    text=ft.render(txt, True, tc)
    screen.blit(text, (x, y))
#Class for Bird
class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images=[]
        self.index=0
        self.counter=0
        #Loading Bird Images
        for i in range(1,4):
            img=pygame.image.load(f"bird{i}.png")
            self.images.append(img)
        self.im=self.images[self.index]
        self.rect=self.im.get_rect()
        self.rect.center=[x, y]
        self.vel=0
        self.clicked=False
#Sprite groups
birdg=pygame.sprite.Group()
pipe=pygame.sprite.Group()
#Bird Group Object
bird=Bird(200, 350)
birdg.add(bird)
#Main Whileloop
run=True
while run:
    clock.tick(fps)
    screen.blit(scr, (0,0))
    birdg.draw(screen)
    birdg.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    pygame.display.update()
pygame.quit()
