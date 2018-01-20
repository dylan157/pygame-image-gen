import pygame, sys
from random import randint
from datetime import datetime
import time, math, imageio
global screen
global size
size = width, height = 500, 500
pygame.init()
screen = pygame.display.set_mode((size))
pygame.display.set_caption("random bit gen")
pygame.display.flip()
pygame.display.update()
running = True

# image, the main function for generating and saving images. 
def image(c01, c02, c03, size, curve, auto, tick, autosave):
    #screen = pygame.display.set_mode(res, pygame.FULLSCREEN)   
    res = width, height = 2000, 2000
    screen = pygame.display.set_mode((res))
    if not curve: curve = 0
    screen = screen
    pygame.display.update()
    num = randint(0, width)
    x = 0
    y = 0
    ran = randint(20, 50)

    rannum = randint(2, 244)

    #pixel colors:
    c0 = 10
    c1 = 11
    c2 = 10
    d0 = 10
    d1 = 11
    d2 = 10
    d11 = randint(1, rannum)
    d12 = randint(1, rannum)
    d13 = randint(1, rannum)
    if c01 == '':
        c00 = randint(1, rannum)
        c10 = randint(1, rannum)
        c20 = randint(1, rannum)
        size = randint(6, 40)
    else:
        c00 = int(c01)
        c10 = int(c02)
        c20 = int(c03)
        size = int(size)


    #finalnum is a string that will be saved with an image as a txt file. this allows you to re open the image with the load option or animate.
    finalnum = str(size) + " " + str(res[0]) + " " + str(res[1]) + " "
    switch = 0
    for p in range(int(width*height/size)):
        if switch % 2:
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
            switch += 1
        else:
            if int(curve) > 0:
                red = [d0, d1, d2]
            else:
                red = [d0%255, d1%255, d2%255]
            d0 += d11
            d1 += d12
            d2 += d13
            if int(curve) > 0:
                if d0 >255:
                    d0 = randint(1, int(curve))
                if d1 >255:
                    d1 = randint(1, int(curve))
                if d2 >255:
                    d2 = randint(1, int(curve))
            switch += 1


        finalnum += str(red[0]) +" "+ str(red[1]) +" "+ str(red[2])+" "
        if x < width: x += size
        else: 
            x = 0
            if y < height: y += size
            else: break
    draw(finalnum, screen)
    pygame.display.update()
    if not auto:
        if input("save?" +(str(size)+"A"+str(c00)+str(c10)+str(c20))+" y/n") == "y":
            filename = str(size)+"A"+str(c00)+str(c10)+str(c20)+"B"+str(randint(0,55))
            file1 = str(filename)+".txt"
            file2 =  open(file1, "w")
            file2.write(finalnum)
            file2.close()
            print("Saved image as :"+filename+".txt")
            pygame.image.save(screen, str(filename)+".jpeg")
        if input("animate?") == 'y': animate(finalnum)
    else: 
        if autosave:
            filename = str(size)+"A"+str(c00)+str(c10)+str(c20)+"B"+str(randint(0,55))
            file1 = str(filename)+".txt"
            file2 =  open(file1, "w")
            file2.write(finalnum)
            file2.close()
            print("Saved image as :"+filename+".txt")
            pygame.image.save(screen, str(filename)+".jpeg")
        print(str(size)+"A"+str(c00)+'.'+str(c10)+'.'+str(c20))
        time.sleep(2.5)
        image("","","","",5, True, 1)


# animate still needs lots of work. It works as intended but dosn't look that interesting. 
def animate(txt_file):
    if not txt_file: 
        file = (input("enter text file name: ")+".txt")
        if len(file) < 6:
            return 0
        try:
            a = open(file, "r")
            txt_file = (a.read())
        except:
            print ("file not found ")
            return 0
    x = 0
    y = 0
    txt_file = txt_file.split()
    size = int(txt_file[0])
    pygame.display.quit()
    res = width, height = int(txt_file[1]), int(txt_file[2])
    blocks = math.floor(width / size)
    screen = pygame.display.set_mode(res, pygame.FULLSCREEN)
    pygame.display.set_caption("random bit gen")
    pygame.display.flip()
    pygame.display.update()
    counter = 3
    steps = int(txt_file[6]) - int(txt_file[3])
    steps2 = int(txt_file[7]) - int(txt_file[4]) 
    steps3 = int(txt_file[8]) - int(txt_file[5])
    print (steps, steps2, steps3)


    for a in range(blocks*1):
        for p in range(10000000):

            red = [int(txt_file[counter]), int(txt_file[counter+1]), int(txt_file[counter+2])]
            pygame.draw.rect(screen, red, [x, y, int(size), int(size)]) 
            counter += 3
            if x < width: x += size
            else: 
                x = 0
                if y < height: y += size
                else: break
        pygame.display.update()
        if gif == y:
            name = str(size+"A"+red[1]+red[2]+red[3])+".jpeg"
            pygame.image.save(screen, name)
            images.append(imageio.imread(name))
        time.sleep(0.1)
        counter = 3
        x = 0
        y = 0
        for blx in range(blocks):
            txt_file.pop(3)
            txt_file.pop(4)
            txt_file.pop(5)
            txt_file.append((int(txt_file[-3]) + steps)%255)
            txt_file.append((int(txt_file[-3]) + steps2)%255)
            txt_file.append((int(txt_file[-3]) + steps3)%255)

    if gif == "y": imageio.mimsave(str(steps+steps2+steps3+".gif"), images)

# draw opens image partner text files. ##A###B##.txt
def draw(file, screen):
    if file == "":
        file = input("  enter text file name: ")+".txt"
        try:
            a = open(file, "r")
            b = (a.read())
            b = b.split()
        except:
            print("file not found")
            return 0
    else: b = file.split()

    size = int(b[0])
    res = width, height = int(b[1]), int(b[2])
    if screen == "":
        pygame.display.quit()
        screen = pygame.display.set_mode((res))
        pygame.display.set_caption("random bit gen")
        pygame.display.flip()
        pygame.display.update()

    if len(file) < 6:
        return 0

    x = 0
    y = 0
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

    pygame.display.update()

while True:
    choice = input("random image(1) load image(2), animate image(3), auto-play(4) or custom(5)")
    if choice == "1":
        image("","","","",0, False, 0)
    elif choice == "2":
        draw("")
    elif choice == "3":
        animate('')
    elif choice == "4":
        res = width, height = 900, 900
        image("","","","",0, True, 0, input("auto save? y/n"))
    elif choice == "5":
        image(input("Seed A: "), input("Seed B: "), input("Seed C: "), input("Size?: "), input("Curve ratio: "), False, 0)





##Quick project :)