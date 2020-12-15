#Fractal Spirograph
#Rohan Deswal
import pygame
from math import cos,sin,pi,radians
pygame.init()

angularOffset = -pi/2

class Circle:
    def __init__(self,x,y,r,k,i = 0,parent = None):
        self.x = x
        self.y = y
        self.r = r
        self.parent = parent
        self.time = 0
        self.speed = 0.01*radians((k)**(i-1))
    def show(self):
        if not self.r < 1:
            pygame.draw.circle(gameDisplay,(255,255,255),(self.x,self.y),int(self.r),1)
    def update(self):
        if self.parent != None:
            self.time += self.speed
            self.x = int(self.parent.x + (self.parent.r + self.r) * cos(self.time+angularOffset))
            self.y = int(self.parent.y + (self.parent.r + self.r) * sin(self.time+angularOffset))

display_width = 800
display_height = 700

gameDisplay = pygame.display.set_mode((display_width,display_height))
clock = pygame.time.Clock()

def game_loop():

    # Values to play with
    k = -4  # integer only
    ratio = 0.5 # can be anything
    n_circles = 11 # more than 20 just makes it ugly and chaotic

    circles = []

    circles.append(Circle(int(display_width/2),int(display_height/2),100,k))

    for i in range(1,n_circles):
        circles.append(Circle(0,0,circles[i-1].r * ratio,k,i,circles[i-1]))

    points = []

    iters_per_frame = 100

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()

        gameDisplay.fill((0,0,0))
        for i in range(0,iters_per_frame):
            for c in circles:
                c.update()
                c.show()
            points.append((circles[-1].x,circles[-1].y))

        pygame.draw.lines(gameDisplay,(171, 218, 244),False,points,1)

        pygame.display.update()
        clock.tick(60)

game_loop()            
