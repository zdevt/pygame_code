#!/usr/bin/env python
#-*- coding:utf-8 -*-
#       FileName:  002_event.py
#
#    Description:
#
#        Version:  1.0
#        Created:  2018-05-31 08:56:20
#  Last Modified:  2018-05-31 09:08:14
#       Revision:  none
#       Compiler:  gcc
#
#         Author:  zt ()
#   Organization:

import pygame
from pygame.locals import *
from sys import exit

pygame.init()
SCREEN_SIZE = (640, 480)
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
font = pygame.font.SysFont("arial", 16)
font_height = font.get_linesize()
event_text = []

while True:
    event = pygame.event.wait()
    event_text.append(str(event))
    event_text = event_text[-SCREEN_SIZE[1] / font_height:]

    if event.type == QUIT:
        exit()

    screen.fill((255, 255, 255))
    y = SCREEN_SIZE[1] - font_height

    for text in reversed(event_text):
        screen.blit(font.render(text, True, (0, 0, 0)), (0, y))
        y -= font_height

    pygame.display.update()
