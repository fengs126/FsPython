'''
Created on 2019/05/21

@author: Administrator
'''
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 14:42:51 2017

@author: zhang
"""

background_filename = 'sushiplate.jpg'
mouse_filename = 'fugu.png'

import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((640, 480), RESIZABLE, 32)
mouse_cursor = pygame.display.set_caption('hello world!')

background = pygame.image.load(background_filename).convert()
# mouse_cursor = pygame.image.load(mouse_filename).convert_alpha()

clock = pygame.time.Clock()
x = 0
speed = 250
while True:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                pygame.quit()
                if event.type == VIDEORESIZE:
                    SCREEN_SIZE = event.size
                    screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)

                    screen_width, screen_height = SCREEN_SIZE

    screen.blit(background, (0, 0))
#     screen.blit(mouse_cursor, (x, 100))

    time_passed = clock.tick()
    time_passed_seconds = time_passed / 1000
    distance = speed * time_passed_seconds

    x += distance
    if x > 640:
        x -= 640

    pygame.display.update()
