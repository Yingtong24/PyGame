import pygame
pygame.init()
screen=pygame.display.set_mode((800,800))
over=True
beige=(245, 239, 208)
pink=(247, 188, 241)
blue=(189, 230, 255)
green=(185, 250, 196)
purple=(229, 188, 247)
turquoise=(154, 237, 212)
screen.fill(beige)
pygame.display.update()
#Classes
class shapes:
    def __init__(self, colour, position, radius, thickness=0):
        self.screen=screen
        self.colour=colour
        self.position=position
        self.radius=radius
        self.thickness=thickness

    def draw(self):
        pygame.draw.circle(self.screen, self.colour, self.position, self.radius, self.thickness)
    def grow(self, size):
        self.radius+=size
        pygame.draw.circle(self.screen, self.colour, self.position, self.radius, self.thickness)
#Object Creation
pos=(400,400)
rad=100
thicks=5

#Multiple Circles
c1=shapes(blue, pos, rad+50)
c2=shapes(green, pos, rad+25)
c3=shapes(purple, pos, rad+13, 10)
c4=shapes(turquoise, pos, rad+7, 10)

pygame.draw.circle(screen, pink, pos, rad, thicks)
pygame.display.update()

while over==True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            over=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            c1.draw()
            c2.draw()
            c3.draw()
            c4.draw()
            pygame.display.update()
        elif event.type==pygame.MOUSEBUTTONUP:
            c1.grow(5)
            c2.grow(10)
            c3.grow(15)
            c4.grow(20)
            pygame.display.update()