#!/usr/bin/env/ python
import pygame
import random
from snakegamesysdata import *
from piece import *

class Food(Piece):
    def __init__(self, color, obstancles):
        coord_x = random.randint(0, DISPLAY_SIZE[0] - SNAKE_REC[1])
        coord_y = random.randint(0, DISPLAY_SIZE[1] - SNAKE_REC[1])

        if len(obstancles) != 0:
            flag = False
            while True:
                for obstancle in obstancles:
                    if not obstancle.rect.collidepoint(coord_x, coord_y):
                        flag = True
                        break
                if flag == True:
                    break
                else:
                    coord_x = random.randint(0, DISPLAY_SIZE[0] - SNAKE_REC[1])
                    coord_y = random.randint(0, DISPLAY_SIZE[1] - SNAKE_REC[1])

        Piece.__init__(self, color, coord_x, coord_y, FOOD_REC)

