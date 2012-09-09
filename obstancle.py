#!/usr/bin/env/ python
import pygame
import random
from piece import *
from snakegamesysdata import *


class Obstancle(Piece):
    def __init__(self, color, obstan_position_ratio):
        coord_x = random.randint(0, DISPLAY_SIZE[0])
        coord_y = random.randint(0, DISPLAY_SIZE[1]) + obstan_position_ratio
        Piece.__init__(self, color, coord_x, coord_y, OBSTAN_REC)
