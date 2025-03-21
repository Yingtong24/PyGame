import pygame
pygame.init()
screen=pygame.display.set_mode((600,600))
#Colours
beige=(245, 239, 208)
blue=(199, 247, 255)
pink=(254, 217, 255)
purple=(221, 186, 245)
green=(204, 255, 227)
grey=(166, 171, 179)
yellow=(255, 252, 92)
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
obj3=shapes(green, (265, 265, 200, 200))
obj4=shapes(purple, (365, 365, 200, 200))
obj5=shapes(yellow, (465, 465, 200, 200))
obj6=shapes(grey, (565, 565, 200, 200))

over=True
while over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            over=False
    obj1.draw()
    obj2.draw()
    obj3.draw()
    obj4.draw()
    obj5.draw()
    obj6.draw()
    pygame.display.update()
