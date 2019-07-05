'''
Created on 2019/05/21

@author: Fengs
'''

import sys
import pygame

white = 255, 255, 255
black = 0, 0, 0

pygame.init()
pygame.display.set_caption("Snake")
screen = pygame.display.set_mode((600, 500))

FPS = 30
clock = pygame.time.Clock()
key = 0
x = 300
y = 250
z = 10

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                key = 1
            elif event.key == pygame.K_DOWN:
                key = 2
            elif event.key == pygame.K_LEFT:
                key = 3
            elif event.key == pygame.K_RIGHT:
                key = 4

    if key == 1:
        y -= z
    elif key == 2:
        y += z
    elif key == 3:
        x -= z
    elif key == 4:
        x += z

    screen.fill(white)
    rect = x, y, z, z
    pygame.draw.rect(screen, black, rect)
#     pygame.draw.rect(screen, white, rect)
#     y -= 1

    pygame.display.update()
    clock.tick(FPS)
    print(FPS)
