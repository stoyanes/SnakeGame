import pygame
from snakegamesysdata import *


class Snake(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.curr_direction = RIGHT
        self.new_direction = RIGHT
        self.snake_elements = [(1, 1)]
        self.coord_x = 1
        self.coord_y = 1
        self.is_alife = True
        self.length = 3

    def born(self):
        self.image = pygame.Surface(SNAKE_REC)
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.rect = pygame.draw.rect(self.image, CYAN, self.rect)

    def grow(self):
        self.length = self.length + 1

    def get_length(self):
        return self.length

    def die(self):
        self.is_alife = False

    def change_direction(self, direction):
        '''Takes one parameter 'direction' which will be eventually the new
           direction to move. If the 'direction' is not common with the current
           the method just returns.

        '''
        if self.curr_direction == RIGHT and direction == LEFT:
            return
        elif self.curr_direction == LEFT and direction == RIGHT:
            return
        elif self.curr_direction == DOWN and direction == UP:
            return
        elif self.curr_direction == UP and direction == DOWN:
            return
        else:
            self.new_direction = direction

    def move(self):
        '''Method which moves the snake in the direction set in 'new_direction'
           or sets the flag 'is_alive' to false through die() method.
        '''
        if self.new_direction == RIGHT:
            self.curr_direction = RIGHT
            self.coord_x += 10
            if self.coord_x >= DISPLAY_SIZE[0]:
                self.die()
                return

        elif self.new_direction == LEFT:
            self.curr_direction = LEFT
            self.coord_x -= 10
            if self.coord_x < 0:
                self.die()
                return

        elif self.new_direction == DOWN:
            self.curr_direction = DOWN
            self.coord_y += 10
            if self.coord_y >= DISPLAY_SIZE[1]:
                self.die()
                return

        elif self.new_direction == UP:
            self.curr_direction = UP
            self.coord_y -= 10
            if self.coord_y < 0:
                self.die()
                return

        for element in self.snake_elements:
            if element[0] == self.rect.left and element[1] == self.rect.top:
                self.die()
                return

        self.snake_elements.insert(0, (self.rect.left, self.rect.top))
        self.snake_elements = self.snake_elements[0:self.length - 1]

        self.rect.left = self.coord_x
        self.rect.top = self.coord_y

