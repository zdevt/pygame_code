#!/usr/bin/env python
#-*- coding:utf-8 -*-
#       FileName:  005_01_save_all_color.py
#
#    Description:
#
#        Version:  1.0
#        Created:  2018-05-31 13:40:50
#  Last Modified:  2018-05-31 13:53:59
#       Revision:  none
#       Compiler:  gcc
#
#         Author:  zt ()
#   Organization:

import pygame
pygame.init()

#screen = pygame.display.set_mode((640, 480))
all_colors = pygame.Surface((4096, 4096), depth=24)

for r in xrange(256):
    print(r + 1, " out of 256")
    x = (r & 15) * 256
    y = (r >> 4) * 256
    for g in xrange(256):
        for b in xrange(256):
            all_colors.set_at((x + g, x + b), (r, g, b))

pygame.image.save(all_colors, "all_colors.bmp")
