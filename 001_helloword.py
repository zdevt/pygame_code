#!/usr/bin/python
# -*- coding: utf-8 -*-

#       FileName:  001_helloword.py
#
#    Description:
#
#        Version:  1.0
#        Created:  2018-05-30 11:45:06
#  Last Modified:  2018-05-31 09:25:14
#       Revision:  none
#       Compiler:  gcc
#
#         Author:  zt ()
#   Organization:

import pygame
from pygame.locals import *
from sys import exit

background_image_filename = './lena.jpg'
mouse_image_filename = './HappyFish.jpg'

display_res = (640, 480)

pygame.init()
screen = pygame.display.set_mode(display_res, 0, 32)
pygame.display.set_caption('hello world')

background = pygame.image.load(background_image_filename)
background = pygame.transform.smoothscale(background, display_res)
mouse_cursor = pygame.image.load(mouse_image_filename)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    screen.blit(background, (0, 0))
    (x, y) = pygame.mouse.get_pos()
    x -= mouse_cursor.get_width() / 2
    y -= mouse_cursor.get_height() / 2

    screen.blit(mouse_cursor, (x, y))
    pygame.display.update()
