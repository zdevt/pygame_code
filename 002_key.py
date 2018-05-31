#!/usr/bin/env python
#-*- coding:utf-8 -*-
#       FileName:  002_key.py
#
#    Description:
#
#        Version:  1.0
#        Created:  2018-05-31 09:08:26
#  Last Modified:  2018-05-31 09:24:01
#       Revision:  none
#       Compiler:  gcc
#
#         Author:  zt ()
#   Organization:

background_image_filename = './lena.jpg'

import pygame
from pygame.locals import *
from sys import *

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)
background = pygame.image.load(background_image_filename)
background = pygame.transform.smoothscale(background, (640, 480))

x, y = 0, 0
move_x, move_y = 0, 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                move_x = -1
            elif event.key == K_RIGHT:
                move_x = 1
            elif event.key == K_UP:
                move_y = -1
            elif event.key == K_DOWN:
                move_y = 1
        elif event.type == KEYUP:
            move_x = 0
            move_y = 0
        x += move_x
        y += move_y

        screen.fill((0, 0, 0))
        screen.blit(background, (x, y))
        pygame.display.update()
