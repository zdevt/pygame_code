#!/usr/bin/env python
#-*- coding:utf-8 -*-
#       FileName:  004_name_chn.py
#
#    Description:
#
#        Version:  1.0
#        Created:  2018-05-31 11:36:27
#  Last Modified:  2018-05-31 13:26:37
#       Revision:  none
#       Compiler:  gcc
#
#         Author:  zt ()
#   Organization:

import pygame
from pygame.locals import *
from sys import *

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)
font = pygame.font.Font("UbuntuMono-R.ttf", 40)
text_surface = font.render(u"你好", True, (0, 0, 255))
x = 0
y = (480 - text_surface.get_height()) / 2
background = pygame.image.load("./chessboard.png").convert()
background = pygame.transform.smoothscale(background, (640, 480))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    screen.blit(background, (0, 0))
    x -= 2
    if x < -text_surface.get_width():
        x = 640 - text_surface.get_width()

    screen.blit(text_surface, (x, y))
    pygame.display.update()
