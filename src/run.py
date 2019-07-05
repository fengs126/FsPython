'''
Created on 2019/05/21

@author: Fengs
'''

import sys
import pygame
import random
import time

white = 255, 255, 255
black = 0, 0, 0
blue = 0, 0, 255

FPS = 60
clock = pygame.time.Clock()
key = None
m = 50
w = 250
h = 500
x = w / 2 - m / 2
y = h - m
oRect = [0, 0, m, m / 2], [50, 0, m, m / 2], [100, 0, m, m / 2], [150, 0, m, m / 2], [200, 0, m, m / 2]
aRect = {}
mode = 0
speed = 1
time0 = 1
time1 = 0
time2 = 0
good = 0
miss = 0
add = 0
sub = 0

pygame.init()
pygame.display.set_caption("Run")
screen = pygame.display.set_mode((w, h))
screen.fill(white)
textImage = pygame.font.SysFont(pygame.font.get_fonts()[10], 20).render("Press [1] to start.", True, black)
screen.blit(textImage, (20, 100))
textImage = pygame.font.SysFont(pygame.font.get_fonts()[10], 20).render("Press [2] to easy mode.", True, black)
screen.blit(textImage, (20, 130))
textSpeed = pygame.font.SysFont(pygame.font.get_fonts()[10], 15).render("Speed:" + str(speed), True, black)
screen.blit(textSpeed, (20, 5))
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if key is not None:
                    key = "L"
            elif event.key == pygame.K_RIGHT:
                if key is not None:
                    key = "R"
            elif event.key == pygame.K_1:
                key = "S"
                mode = 1
                aRect.clear()
            elif event.key == pygame.K_2:
                key = "E"
                mode = 2
                aRect.clear()
            elif event.key == pygame.K_UP:
                key = "U"
                if speed < 5:
                    speed += 1
                    time0 -= 0.2
            elif event.key == pygame.K_DOWN:
                key = "D"
                if speed > 1 and speed <= 5 :
                    speed -= 1
                    time0 += 0.2
                elif speed > 5:
                    speed -= 1
            else:
                key = None

    if key is None:
        continue
    elif key == "L":
        if x - m < 0:
            x = 200
        else:
            x -= m

        key = "S"
    elif key == "R":
        if x + m > 200:
            x = 0
        else:
            x += m

        key = "S"
    elif key == "U" or key == "D":
        if mode == 0:
            screen.fill(white)
            textImage1 = pygame.font.SysFont(pygame.font.get_fonts()[10], 20).render("Press [1] to start.", True, black)
            screen.blit(textImage1, (20, 100))
            textImage2 = pygame.font.SysFont(pygame.font.get_fonts()[10], 20).render("Press [2] to easy mode.", True, black)
            screen.blit(textImage2, (20, 130))
            textSpeed = pygame.font.SysFont(pygame.font.get_fonts()[10], 15).render("Speed:" + str(speed), True, black)
            screen.blit(textSpeed, (20, 5))
            pygame.display.update()
            continue

    screen.fill(white)
    for rect in oRect:
        pygame.draw.rect(screen, black, rect)

    if good != 0 and good % 100 == 0 and add != good:
        add = good
        if speed < 99:
            speed += 1

    if miss != 0 and miss % 100 == 0 and sub != miss:
        sub = miss
        if speed > 1 and speed <= 5 :
            speed -= 1
            time0 += 0.2
        elif speed > 5:
            speed -= 1

    textSpeed = pygame.font.SysFont(pygame.font.get_fonts()[10], 15).render("Speed:" + str(speed), True, white)
    screen.blit(textSpeed, (20, 5))
    textSpeed = pygame.font.SysFont(pygame.font.get_fonts()[10], 15).render("Good:" + str(good), True, white)
    screen.blit(textSpeed, (100, 5))
    textSpeed = pygame.font.SysFont(pygame.font.get_fonts()[10], 15).render("Miss:" + str(miss), True, white)
    screen.blit(textSpeed, (180, 5))

    # Me
    mRect = [x, y, m, m / 2]
    pygame.draw.rect(screen, blue, mRect)

    # Active
    time1 = time.time()
    if time1 - time2 >= time0:
        kTime = time1
        vRect = list(oRect[random.randint(0, 4)])
        if mode == 1:
            vRect = list(oRect[random.randint(0, 4)])
        elif mode == 2:
            vRect = list(oRect[random.randint(1, 3)])

        vRect[1] += m / 2
        aRect.setdefault(kTime, vRect)
        time2 = time1

    for aKey in aRect.keys():
        rect = aRect[aKey]
        if rect is None:
            continue

        rect[1] += speed
        pygame.draw.rect(screen, black, rect)

        # Result
        a1 = [rect[0], rect[1]]
        a2 = [rect[0], rect[1] + rect[3]]
        a3 = [rect[0] + rect[2], rect[1]]
        a4 = [rect[0] + rect[2], rect[1] + rect[3]]
        if (a1[0] >= mRect[0] and a1[0] <= mRect[0] + mRect[2] and a1[1] >= mRect[1] and a1[1] <= mRect[1] + mRect[3]
            and a3[0] >= mRect[0] and a3[0] <= mRect[0] + mRect[2] and a3[1] >= mRect[1] and a3[1] <= mRect[1] + mRect[3]
            or a2[0] >= mRect[0] and a2[0] <= mRect[0] + mRect[2] and a2[1] >= mRect[1] and a2[1] <= mRect[1] + mRect[3]
            and a4[0] >= mRect[0] and a4[0] <= mRect[0] + mRect[2] and a4[1] >= mRect[1] and a4[1] <= mRect[1] + mRect[3]):
            aRect[aKey] = None
            good += 1
        elif a2[1] >= h + m and a4[1] >= h + m:
            aRect[aKey] = None
            miss += 1
#             key = None

    clock.tick(FPS)
    pygame.display.update()
