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
#Creating Class
class shapes:
    def __init__(self, colour, sides):
        self.screen=screen
        self.colour=colour
        self.sides=sides
    def draw(self):
        self.draw_rect=pygame.draw.rect(self.screen, self.colour, self.sides)

obj1=shapes(blue, (65, 65, 200,200))
obj2=shapes(pink, (165, 165, 200, 200))
        

over=True
while over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            over=False
    obj1.draw()
    obj2.draw()
    pygame.display.update()
