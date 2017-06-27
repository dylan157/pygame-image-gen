import pygame, sys
from random import randint
import time
pygame.init()
size = width, height = 1280, 720
screen = pygame.display.set_mode((size))
pygame.display.set_caption("random bit gen")
pygame.display.flip()
pygame.display.update()

running = True
while running:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
            pygame.quit()
    num = randint(0, width)
    x = 0
    y = 0
    ran = randint(20, 50)
    c0 = 10
    c1 = 11
    c2 = 10
    c00 = randint(10, 40)
    c10 = randint(10, 40)
    c20 = randint(10, 40)
    size = randint(15, 20)
    for p in range(1000000):
        if c0 < 255 and c1 < 255 and c2 < 255: 
            red = [randint(c0-10, c0), randint(c1-10, c1), randint(c2-10, c2)]
            c0 += c00
            c1 += c10
            c2 += c20
        elif c0 >= 255: c0 = 10
        elif c1 >= 255: c1 = 11
        elif c2 >= 255: c2 = 10


        pygame.draw.rect(screen, red, [x, y, int(size), int(size)]) 
        if x < width: x += size
        else: 
            x = 0
            if y < height: y += size
            else: break
    time.sleep(2)
    pygame.display.update()

##Quick project :)
