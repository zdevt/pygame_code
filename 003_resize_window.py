#!/usr/bin/env python
#-*- coding:utf-8 -*-
#       FileName:  003_resize_window.py
#
#    Description:
#
#        Version:  1.0
#        Created:  2018-05-31 10:00:32
#  Last Modified:  2018-05-31 10:07:41
#       Revision:  none
#       Compiler:  gcc
#
#         Author:  zt ()
#   Organization:

background_image_filename = './lena.jpg'

import pygame
from pygame.locals import *
from sys import *

SCREEN_SIZE = (640, 480)
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)
background = pygame.image.load(background_image_filename).convert()

while True:
    event = pygame.event.wait()
    if event.type == QUIT:
        exit()
    if event.type == VIDEORESIZE:
        SCREEN_SIZE = event.size
        screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)
        pygame.display.set_caption("window resized to" + str(event.size))
    screen_width, screen_height = SCREEN_SIZE

    for y in xrange(0, screen_height, background.get_height()):
        for x in xrange(0, screen_width, background.get_width()):
            screen.blit(background, (x, y))
    pygame.display.update()
