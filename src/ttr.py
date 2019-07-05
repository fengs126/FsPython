'''
Created on 2019/05/23

@author: Fengs
'''
import sys
import pygame
import random
import time


def mainInit():
    screen.fill(white)
    textImage = pygame.font.SysFont(pygame.font.get_fonts()[10], 20).render("Press [1] to start.", True, black)
    screen.blit(textImage, (20, 100))
    textImage = pygame.font.SysFont(pygame.font.get_fonts()[10], 20).render("Press [2] to easy mode.", True, black)
    screen.blit(textImage, (20, 130))
    textImage = pygame.font.SysFont(pygame.font.get_fonts()[10], 20).render("Press [3] to no space mode.", True, black)
    screen.blit(textImage, (20, 160))
    textSpeed = pygame.font.SysFont(pygame.font.get_fonts()[10], 15).render("Speed:" + str(speed), True, black)
    screen.blit(textSpeed, (20, 5))
    pygame.display.update()


white = 255, 255, 255
black = 0, 0, 0
blue = 0, 0, 255
plum1 = 255, 187, 255
pink1 = 255, 181, 197
wheat1 = 255, 231, 186
lightYellow1 = 255, 255, 224
darkOliveGreen1 = 202, 255, 112
darkSlateGray1 = 151, 255, 255
gold1 = 255, 215, 0
coral1 = 255, 114, 86
khaki1 = 255 , 246, 143
red1 = 255, 0 , 0
orange1 = 255 , 165, 0
yellow1 = 255, 255, 0
green1 = 0 , 255 , 0
cyan = 0 , 255, 255
deepSkyBlue = 0, 191 , 255
violet = 238, 130 , 238

FPS = 60
clock = pygame.time.Clock()
key = None
m = 50
w = 350
h = 500
x = w / 2 - m / 2
y = h - m
oRect = [0, 0, m, m / 2], [50, 0, m, m / 2], [100, 0, m, m / 2], [150, 0, m, m / 2], [200, 0, m, m / 2], [250, 0, m, m / 2], [300, 0, m, m / 2]
pRect = {}
mode = 0
speed = 1
time0 = 1
time1 = 0
time2 = 0
good = 0
miss = 0
add = 0
sub = 0
key_s = 0
key_d = 0
key_f = 0
key_sp = 0
key_j = 0
key_k = 0
key_l = 0
rect_s = None
rect_d = None
rect_f = None
rect_sp = None
rect_j = None
rect_k = None
rect_l = None
flg1_s = False
flg2_s = False
flg1_d = False
flg2_d = False
flg1_f = False
flg2_f = False
flg1_sp = False
flg2_sp = False
flg1_j = False
flg2_j = False
flg1_k = False
flg2_k = False
flg1_l = False
flg2_l = False

pygame.init()
pygame.display.set_caption("TTR")
screen = pygame.display.set_mode((w, h))
mainInit()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                key = "1"
                mode = 1
                pRect.clear()
            elif event.key == pygame.K_2:
                key = "2"
                mode = 2
                pRect.clear()
            elif event.key == pygame.K_3:
                key = "3"
                mode = 3
                pRect.clear()
            elif event.key == pygame.K_UP:
                key = "UP"
                if speed < 5:
                    speed += 1
                    time0 -= 0.2
            elif event.key == pygame.K_DOWN:
                key = "DOWN"
                if speed > 1 and speed <= 5 :
                    speed -= 1
                    time0 += 0.2
                elif speed > 5:
                    speed -= 1
            elif event.key == pygame.K_s:
                if mode != 0:
                    key = "S"
                    key_s = 1
            elif event.key == pygame.K_d:
                if mode != 0:
                    key = "D"
                    key_d = 1
            elif event.key == pygame.K_f:
                if mode != 0:
                    key = "F"
                    key_f = 1
            elif event.key == pygame.K_SPACE:
                if mode != 0:
                    key = "SP"
                    key_sp = 1
            elif event.key == pygame.K_j:
                if mode != 0:
                    key = "J"
                    key_j = 1
            elif event.key == pygame.K_k:
                if mode != 0:
                    key = "K"
                    key_k = 1
            elif event.key == pygame.K_l:
                if mode != 0:
                    key = "L"
                    key_l = 1
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                if mode != 0:
                    key = "S"
                    key_s = 2
            elif event.key == pygame.K_d:
                if mode != 0:
                    key = "D"
                    key_d = 2
            elif event.key == pygame.K_f:
                if mode != 0:
                    key = "F"
                    key_f = 2
            elif event.key == pygame.K_SPACE:
                if mode != 0:
                    key = "SP"
                    key_sp = 2
            elif event.key == pygame.K_j:
                if mode != 0:
                    key = "J"
                    key_j = 2
            elif event.key == pygame.K_k:
                if mode != 0:
                    key = "K"
                    key_k = 2
            elif event.key == pygame.K_l:
                if mode != 0:
                    key = "L"
                    key_l = 2

    if key is None:
        continue
    elif key == "UP" or key == "DOWN":
        if mode == 0:
            mainInit()
            continue
    else:
        if mode == 0:
            continue

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

    screen.fill(white)
    for rect in oRect:
        pygame.draw.rect(screen, black, rect)

    textSpeed = pygame.font.SysFont(pygame.font.get_fonts()[10], 15).render("Speed:" + str(speed), True, white)
    screen.blit(textSpeed, (20, 5))
    textSpeed = pygame.font.SysFont(pygame.font.get_fonts()[10], 15).render("Good:" + str(good), True, white)
    screen.blit(textSpeed, (150, 5))
    textSpeed = pygame.font.SysFont(pygame.font.get_fonts()[10], 15).render("Miss:" + str(miss), True, white)
    screen.blit(textSpeed, (270, 5))

    # Active
    time1 = time.time()
    if time1 - time2 >= time0:
        kTime = time1
        vRect = list(oRect[random.randint(0, 6)])
        if mode == 1:
            vRect = list(oRect[random.randint(0, 6)])
        elif mode == 2:
            vRect = list(oRect[random.randint(1, 5)])
        elif mode == 3:
            vRect = list(oRect[random.choice([0, 1, 2, 4, 5, 6])])

        vRect[1] += m / 2
        vRect[3] = 10
        pRect.setdefault(kTime, vRect)
        time2 = time1

    for pKey in pRect.keys():
        rect = pRect[pKey]
        if rect is None:
            continue

        rect[1] += speed
        pygame.draw.rect(screen, black, rect)

        # Result
        p1 = [rect[0], rect[1]]
        p2 = [rect[0], rect[1] + rect[3]]
        p3 = [rect[0] + rect[2], rect[1]]
        p4 = [rect[0] + rect[2], rect[1] + rect[3]]
        if p1[1] >= y and p1[1] <= y + m / 2 or p2[1] >= y and p2[1] <= y + m / 2:
            if p1[0] == 0 and p3[0] == 50:
                rect_s = [pKey, rect]
            elif p1[0] == 50 and p3[0] == 100:
                rect_d = [pKey, rect]
            elif p1[0] == 100 and p3[0] == 150:
                rect_f = [pKey, rect]
            elif p1[0] == 150 and p3[0] == 200:
                rect_sp = [pKey, rect]
            elif p1[0] == 200 and p3[0] == 250:
                rect_j = [pKey, rect]
            elif p1[0] == 250 and p3[0] == 300:
                rect_k = [pKey, rect]
            elif p1[0] == 300 and p3[0] == 350:
                rect_l = [pKey, rect]

        if p1[1] > h:
            pRect[pKey] = None
            miss += 1

    # Me
    pygame.draw.line(screen, blue, (0, y - 2), (w, y - 2), 2)
    pygame.draw.line(screen, blue, (0, y + m / 2), (w, y + m / 2), 2)

    if key_s == 1:
        rect = [0, y, m, m / 2]
        pygame.draw.rect(screen, red1, rect)
    elif key_s == 2:
        rect = [0, y, m, m / 2]
        pygame.draw.rect(screen, white, rect)

    if key_d == 1:
        rect = [50, y, m, m / 2]
        pygame.draw.rect(screen, orange1, rect)
    elif key_d == 2:
        rect = [50, y, m, m / 2]
        pygame.draw.rect(screen, white, rect)

    if key_f == 1:
        rect = [100, y, m, m / 2]
        pygame.draw.rect(screen, yellow1, rect)
    elif key_f == 2:
        rect = [100, y, m, m / 2]
        pygame.draw.rect(screen, white, rect)

    if key_sp == 1:
        rect = [150, y, m, m / 2]
        pygame.draw.rect(screen, cyan, rect)
    elif key_sp == 2:
        rect = [150, y, m, m / 2]
        pygame.draw.rect(screen, white, rect)

    if key_j == 1:
        rect = [200, y, m, m / 2]
        pygame.draw.rect(screen, deepSkyBlue, rect)
    elif key_j == 2:
        rect = [200, y, m, m / 2]
        pygame.draw.rect(screen, white, rect)

    if key_k == 1:
        rect = [250, y, m, m / 2]
        pygame.draw.rect(screen, violet, rect)
    elif key_k == 2:
        rect = [250, y, m, m / 2]
        pygame.draw.rect(screen, white, rect)

    if key_l == 1:
        rect = [300, y, m, m / 2]
        pygame.draw.rect(screen, khaki1, rect)
    elif key_l == 2:
        rect = [300, y, m, m / 2]
        pygame.draw.rect(screen, white, rect)

    textImage = pygame.font.SysFont(pygame.font.get_fonts()[10], 20).render("[S]", True, blue)
    screen.blit(textImage, (0 + 15, y))
    textImage = pygame.font.SysFont(pygame.font.get_fonts()[10], 20).render("[D]", True, blue)
    screen.blit(textImage, (50 + 15, y))
    textImage = pygame.font.SysFont(pygame.font.get_fonts()[10], 20).render("[F]", True, blue)
    screen.blit(textImage, (100 + 15, y))
    textImage = pygame.font.SysFont(pygame.font.get_fonts()[10], 20).render("[S]", True, blue)
    screen.blit(textImage, (150 + 15, y))
    textImage = pygame.font.SysFont(pygame.font.get_fonts()[10], 20).render("[J]", True, blue)
    screen.blit(textImage, (200 + 15, y))
    textImage = pygame.font.SysFont(pygame.font.get_fonts()[10], 20).render("[K]", True, blue)
    screen.blit(textImage, (250 + 15, y))
    textImage = pygame.font.SysFont(pygame.font.get_fonts()[10], 20).render("[L]", True, blue)
    screen.blit(textImage, (300 + 15, y))

    # Result
    if rect_s is not None:
        pKey = rect_s[0]
        rect = rect_s[1]
        p1 = [rect[0], rect[1]]
        p2 = [rect[0], rect[1] + rect[3]]
        p3 = [rect[0] + rect[2], rect[1]]
        p4 = [rect[0] + rect[2], rect[1] + rect[3]]
        if p2[1] - p1[1] <= m / 2:
            if key_s == 2:
                pRect[pKey] = None
                rect_s = None
                good += 1
        else:
            if p2[1] >= y and p2[1] <= y + m / 2 and key_s == 1:
                flg1_s = True

            if p1[1] >= y and p1[1] <= y + m / 2 and key_s == 2:
                flg2_s = True

            if flg1_s and flg2_s:
                pRect[pKey] = None
                rect_s = None
                flg1_s = False
                flg2_s = False
                good += 1

        if (p1[1] < y or p1[1] > y + m / 2) and (p2[1] < y or p2[1] > y + m / 2):
            rect_s = None

    if rect_d is not None:
        pKey = rect_d[0]
        rect = rect_d[1]
        p1 = [rect[0], rect[1]]
        p2 = [rect[0], rect[1] + rect[3]]
        p3 = [rect[0] + rect[2], rect[1]]
        p4 = [rect[0] + rect[2], rect[1] + rect[3]]
        if p2[1] - p1[1] <= m / 2:
            if key_d == 2:
                pRect[pKey] = None
                rect_d = None
                good += 1
        else:
            if p2[1] >= y and p2[1] <= y + m / 2 and key_d == 1:
                flg1_d = True

            if p1[1] >= y and p1[1] <= y + m / 2 and key_d == 2:
                flg2_d = True

            if flg1_d and flg2_d:
                pRect[pKey] = None
                rect_d = None
                flg1_d = False
                flg2_d = False
                good += 1

        if (p1[1] < y or p1[1] > y + m / 2) and (p2[1] < y or p2[1] > y + m / 2):
            rect_d = None

    if rect_f is not None:
        pKey = rect_f[0]
        rect = rect_f[1]
        p1 = [rect[0], rect[1]]
        p2 = [rect[0], rect[1] + rect[3]]
        p3 = [rect[0] + rect[2], rect[1]]
        p4 = [rect[0] + rect[2], rect[1] + rect[3]]
        if p2[1] - p1[1] <= m / 2:
            if key_f == 2:
                pRect[pKey] = None
                rect_f = None
                good += 1
        else:
            if p2[1] >= y and p2[1] <= y + m / 2 and key_f == 1:
                flg1_f = True

            if p1[1] >= y and p1[1] <= y + m / 2 and key_f == 2:
                flg2_f = True

            if flg1_f and flg2_f:
                pRect[pKey] = None
                rect_f = None
                flg1_f = False
                flg2_f = False
                good += 1

        if (p1[1] < y or p1[1] > y + m / 2) and (p2[1] < y or p2[1] > y + m / 2):
            rect_f = None

    if rect_sp is not None:
        pKey = rect_sp[0]
        rect = rect_sp[1]
        p1 = [rect[0], rect[1]]
        p2 = [rect[0], rect[1] + rect[3]]
        p3 = [rect[0] + rect[2], rect[1]]
        p4 = [rect[0] + rect[2], rect[1] + rect[3]]
        if p2[1] - p1[1] <= m / 2:
            if key_sp == 2:
                pRect[pKey] = None
                rect_sp = None
                good += 1
        else:
            if p2[1] >= y and p2[1] <= y + m / 2 and key_sp == 1:
                flg1_sp = True

            if p1[1] >= y and p1[1] <= y + m / 2 and key_sp == 2:
                flg2_sp = True

            if flg1_sp and flg2_sp:
                pRect[pKey] = None
                rect_sp = None
                flg1_sp = False
                flg2_sp = False
                good += 1

        if (p1[1] < y or p1[1] > y + m / 2) and (p2[1] < y or p2[1] > y + m / 2):
            rect_sp = None

    if rect_j is not None:
        pKey = rect_j[0]
        rect = rect_j[1]
        p1 = [rect[0], rect[1]]
        p2 = [rect[0], rect[1] + rect[3]]
        p3 = [rect[0] + rect[2], rect[1]]
        p4 = [rect[0] + rect[2], rect[1] + rect[3]]
        if p2[1] - p1[1] <= m / 2:
            if key_j == 2:
                pRect[pKey] = None
                rect_j = None
                good += 1
        else:
            if p2[1] >= y and p2[1] <= y + m / 2 and key_j == 1:
                flg1_j = True

            if p1[1] >= y and p1[1] <= y + m / 2 and key_j == 2:
                flg2_j = True

            if flg1_j and flg2_j:
                pRect[pKey] = None
                rect_j = None
                flg1_j = False
                flg2_j = False
                good += 1

        if (p1[1] < y or p1[1] > y + m / 2) and (p2[1] < y or p2[1] > y + m / 2):
            rect_j = None

    if rect_k is not None:
        pKey = rect_k[0]
        rect = rect_k[1]
        p1 = [rect[0], rect[1]]
        p2 = [rect[0], rect[1] + rect[3]]
        p3 = [rect[0] + rect[2], rect[1]]
        p4 = [rect[0] + rect[2], rect[1] + rect[3]]
        if p2[1] - p1[1] <= m / 2:
            if key_k == 2:
                pRect[pKey] = None
                rect_k = None
                good += 1
        else:
            if p2[1] >= y and p2[1] <= y + m / 2 and key_k == 1:
                flg1_k = True

            if p1[1] >= y and p1[1] <= y + m / 2 and key_k == 2:
                flg2_k = True

            if flg1_k and flg2_k:
                pRect[pKey] = None
                rect_k = None
                flg1_k = False
                flg2_k = False
                good += 1

        if (p1[1] < y or p1[1] > y + m / 2) and (p2[1] < y or p2[1] > y + m / 2):
            rect_k = None

    if rect_l is not None:
        pKey = rect_l[0]
        rect = rect_l[1]
        p1 = [rect[0], rect[1]]
        p2 = [rect[0], rect[1] + rect[3]]
        p3 = [rect[0] + rect[2], rect[1]]
        p4 = [rect[0] + rect[2], rect[1] + rect[3]]
        if p2[1] - p1[1] <= m / 2:
            if key_l == 2:
                pRect[pKey] = None
                rect_l = None
                good += 1
        else:
            if p2[1] >= y and p2[1] <= y + m / 2 and key_l == 1:
                flg1_l = True

            if p1[1] >= y and p1[1] <= y + m / 2 and key_l == 2:
                flg2_l = True

            if flg1_l and flg2_l:
                pRect[pKey] = None
                rect_l = None
                flg1_l = False
                flg2_l = False
                good += 1

        if (p1[1] < y or p1[1] > y + m / 2) and (p2[1] < y or p2[1] > y + m / 2):
            rect_l = None

    if key_s == 2:
        key_s = 0
    if key_d == 2:
        key_d = 0
    if key_f == 2:
        key_f = 0
    if key_sp == 2:
        key_sp = 0
    if key_j == 2:
        key_j = 0
    if key_k == 2:
        key_k = 0
    if key_l == 2:
        key_l = 0

    clock.tick(FPS)
    pygame.display.update()
