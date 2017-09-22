import pygame, sys
from random import randint
from datetime import datetime
import time
pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode((size))
pygame.display.set_caption("random bit gen")
pygame.display.flip()
pygame.display.update()

running = True

def image(res, c01, c02, c03, size, curve):
    res = width, height = 900, 900
    screen = pygame.display.set_mode((res))
    pygame.display.set_caption("random bit gen")
    pygame.display.flip()
    pygame.display.update()
    num = randint(0, width)
    x = 0
    y = 0
    ran = randint(20, 50)
    c0 = 10
    c1 = 11
    c2 = 10
    if c01 == '':
        c00 = randint(randint(5, 20), randint(21, 255))
        c10 = randint(randint(5, 20), randint(21, 255))
        c20 = randint(randint(5, 20), randint(21, 255))
        size = randint(3, 30)
    else:
        c00 = int(c01)
        c10 = int(c02)
        c20 = int(c03)
        size = int(size)


    
    finalnum = str(size) + " " + str(res[0]) + " " + str(res[1]) + " "
    for p in range(int(width*height/size)):
        if int(curve) > 0:
            red = [c0, c1, c2]
        else:
            red = [c0%255, c1%255, c2%255]
        c0 += c00
        c1 += c10
        c2 += c20
        if int(curve) > 0:
            if c0 >255:
                c0 = randint(1, int(curve))
            if c1 >255:
                c1 = randint(1, int(curve))
            if c2 >255:
                c2 = randint(1, int(curve))

        pygame.draw.rect(screen, red, [x, y, int(size), int(size)]) 
        finalnum += str(red[0]) +" "+ str(red[1]) +" "+ str(red[2])+" "
        if x < width: x += size
        else: 
            x = 0
            if y < height: y += size
            else: break

    pygame.display.update()
    if input("save?" +(str(size)+"A"+str(c00)+str(c10)+str(c20))+" y/n") == "y":
        filename = str(size)+"A"+str(c00)+str(c10)+str(c20)+"B"+str(randint(0,55))
        file1 = str(filename)+".txt"
        file2 =  open(file1, "w")
        file2.write(finalnum)
        file2.close()
        print("Saved image as :"+filename+".txt")
        pygame.image.save(screen, str(filename)+".jpeg")



def modify():
    file = input("enter text file name: ")+".txt"
    if len(file) < 6:
        return 0
    x = 0
    y = 0
    a = open(file, "r")
    b = (a.read())
    b = b.split()
    size = int(b[0])
    pygame.display.quit()
    res = width, height = int(b[1]), int(b[2])
    screen = pygame.display.set_mode((res))
    pygame.display.set_caption("random bit gen")
    pygame.display.flip()
    pygame.display.update()


    counter = 3
    for p in range(10000000):
        a0 = int(b[counter])
        b0 = int(b[counter+1])
        c0 = int(b[counter+2])
        if a0 + 20 < 0:
            a0 -= randint(0, 20)
        if b0 + 200 < 0:
            b0 -= randint(0, 20)
        if c0 + 20 < 0:
            c0 -= randint(0, 20)
        red = [a0, b0, c0]
        pygame.draw.rect(screen, red, [x, y, int(size), int(size)]) 
        counter += 3
        if x < width: x += size
        else: 
            x = 0
            if y < height: y += size
            else: break

    print("finished....")
    pygame.display.update()





def draw():
    file = input("enter text file name: ")+".txt"
    if len(file) < 6:
        return 0
    x = 0
    y = 0
    a = open(file, "r")
    b = (a.read())
    b = b.split()
    size = int(b[0])
    pygame.display.quit()
    res = width, height = int(b[1]), int(b[2])
    screen = pygame.display.set_mode((res))
    pygame.display.set_caption("random bit gen")
    pygame.display.flip()
    pygame.display.update()


    counter = 3
    for p in range(10000000):

        red = [int(b[counter]), int(b[counter+1]), int(b[counter+2])]
        pygame.draw.rect(screen, red, [x, y, int(size), int(size)]) 
        counter += 3
        if x < width: x += size
        else: 
            x = 0
            if y < height: y += size
            else: break

    print("finished....")
    pygame.display.update()

while True:
    pygame.display.update()
    choice = input("new image, load image, modify or custom? n/l/m/c: ")
    if choice == "c":
        image(size, input("Seed A: "), input("Seed B: "), input("Seed C: "), input("Size?: "), input("Curve ratio: "))
    elif choice == "n":
        image(size, "","","","","")
    elif choice == "l":
        draw()
    elif choice == "m":
        modify()




##Quick project :)