'''
Created on 2019/05/21

@author: Administrator
'''
# import pygame
# from pygame.locals import *
#
# pygame.init()
# screen = pygame.display.set_mode((500, 365), 0, 32)
#
# pygame.display.set_caption("Hello, World!")
#
# while True:
#     pygame.display.update()

import sys
import pygame
from pygame.locals import *

white = 255, 255, 255
blue = 0, 0, 200

pygame.init()
screen = pygame.display.set_mode((600, 500))

myfont = pygame.font.Font(None, 60)
textImage = myfont.render("Hello Pygame", True, white)
while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()

    screen.fill(blue)
    screen.blit(textImage, (100, 100))
    color = 255, 255, 0
    position = 300, 250
    radius = 100
    width = 10
    pygame.draw.circle(screen, color, position, radius, width)

    pygame.display.update()

