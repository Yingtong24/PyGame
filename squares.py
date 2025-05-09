import pygame
pygame.init()
screen = pygame.display.set_mode((800, 800))
over = True

# Colors
beige = (245, 239, 208)
pink = (247, 188, 241)
blue = (189, 230, 255)
green = (185, 250, 196)
purple = (229, 188, 247)
turquoise = (154, 237, 212)

screen.fill(beige)
pygame.display.update()

# Classes
class shapes:
    def __init__(self, colour, position, radius, thickness=0):
        self.screen = screen
        self.colour = colour
        self.position = position
        self.radius = radius  # now interpreted as half-side-length
        self.thickness = thickness

    def draw(self):
        top_left = (self.position[0] - self.radius, self.position[1] - self.radius)
        side_length = self.radius * 2
        pygame.draw.rect(self.screen, self.colour, (*top_left, side_length, side_length), self.thickness)

    def grow(self, size):
        self.radius += size
        self.draw()

# Object Creation
pos = (400, 400)
rad = 100
thicks = 5

# Multiple Squares
c1 = shapes(blue, pos, rad + 50)
c2 = shapes(green, pos, rad + 25)
c3 = shapes(purple, pos, rad + 13, 10)
c4 = shapes(turquoise, pos, rad + 7, 10)

# Draw center pink square
pygame.draw.rect(screen, pink, (pos[0] - rad, pos[1] - rad, rad * 2, rad * 2), thicks)
pygame.display.update()

# Main loop
while over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            over = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            c1.draw()
            c2.draw()
            c3.draw()
            c4.draw()
            pygame.display.update()
        elif event.type == pygame.MOUSEBUTTONUP:
            c1.grow(5)
            c2.grow(10)
            c3.grow(15)
            c4.grow(20)
            pygame.display.update()
        elif event.type == pygame.MOUSEMOTION:
            position = pygame.mouse.get_pos()
            cir = shapes("light blue", position, 7)
            cir.draw()
            pygame.display.update()
