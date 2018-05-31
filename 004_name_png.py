#!/usr/bin/env python
#-*- coding:utf-8 -*-
#       FileName:  004_name_png.py
#
#    Description:
#
#        Version:  1.0
#        Created:  2018-05-31 11:32:23
#  Last Modified:  2018-05-31 11:34:21
#       Revision:  none
#       Compiler:  gcc
#
#         Author:  zt ()
#   Organization:

my_name = "zzz"
import pygame

pygame.init()
my_font = pygame.font.SysFont("arial", 64)
name_surface = my_font.render(my_name, True, (0, 0, 0), (255, 255, 255))
pygame.image.save(name_surface, "zzz.png")
