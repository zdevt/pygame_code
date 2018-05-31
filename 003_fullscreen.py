#!/usr/bin/env python
#-*- coding:utf-8 -*-
#       FileName:  003_fullscreen.py
#
#    Description:
#
#        Version:  1.0
#        Created:  2018-05-31 09:49:34
#  Last Modified:  2018-05-31 09:59:10
#       Revision:  none
#       Compiler:  gcc
#
#         Author:  zt ()
#   Organization:

background_images_filename = "./lena.jpg"

import pygame
from pygame.locals import *
from sys import *

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)
background = pygame.image.load(background_images_filename).convert()

Fullscreen = False

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    if event.type == KEYDOWN:
        if event.key == K_f:
            Fullscreen = not Fullscreen
            if Fullscreen:
                screen = pygame.display.set_mode((640, 480), FULLSCREEN, 32)
            else:
                screen = pygame.display.set_mode((640, 480), 0, 32)
    screen.blit(background, (0, 0))
    pygame.display.update()
