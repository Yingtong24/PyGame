import pygame
import random
import time
from pygame.locals import*
pygame.init()
WIDTH=1000
HEIGHT=1000
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