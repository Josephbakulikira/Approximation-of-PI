import pygame 
import random 
import math
import os

os.environ["SDL_VIDEO_CENTERED"]='1'
width, height = 1920, 1080
pygame.init()
pygame.display.set_caption("APPROXIMATION OF PI")
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
fps = 60


number_of_point = 10000
counter = 0
screen.fill((0, 0, 0))
my_radius = 500
point_list = []
inside_list = []
pygame.draw.circle(screen, (100, 100, 100), (int(width/2), int(height/2)), my_radius)

class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.distance = math.sqrt(((self.x - (width/2)) **2) + ((self.y - (height/2)) ** 2))
    def display(self):
        if self.distance > my_radius:
            pygame.draw.circle(screen, (255, 255, 255), (self.x, self.y), 1)
        elif self.distance < my_radius:
            pygame.draw.circle(screen, (0, 255, 0), (self.x, self.y), 1)

for i in range(number_of_point):
    x = random.randint(int(width/2), int(width/2)+my_radius)
    y = random.randint(int(height/2)-my_radius, int(height/2))
    point = Point(x, y)
    point_list.append(point)


for point in point_list:
    if point.distance < my_radius:
        inside_list.append(point)
    point.display()

print(len(inside_list))

pi = 0.00
pi = 4 * len(inside_list)/len(point_list)
print(pi)

font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render(str(pi), False, (255, 255, 255))
textRect = text.get_rect() 
textRect.center = (250, 50)
screen.blit(text, textRect)
#area circle pi * (radius **2)

run = True
while run:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()