#!/usr/bin/env/ python
import pygame
import random
from pygame.locals import *
from snakegamesysdata import *
from snake import *
from piece import *
from food import *
from obstancle import *


class Player(object):
    def __init__(self):
        self.score = 0

    def get_score(self):
        return self.score

    def increase_score(self):
        self.score += 5


class Game(object):

    def __init__(self):
        self.speed = START_SPEED
        self.obstancles = []
        self.food = Food(GREEN, [])
        self.level = 0
        self.levels_table = set([11, 29, 47, 71, 97, 113])
        self.eat_sound = pygame.mixer.Sound('sounds/eat.wav')

    def get_obstancles(self):
        return self.obstancles

    def draw_welcome_mess(self, screen):
        image = pygame.image.load('images/well_mess.png')
        screen.blit(image, (0, 0))
        pygame.display.flip()

    def draw_game_over_mess(self, screen, score):
        image = pygame.image.load('images/game_over_mess.png')
        screen.blit(image, (0, 0))
        pygame.display.flip()
        pygame.mixer.Sound('sounds/game_over.wav').play()

        #font = pygame.font.Font(None, 60)
        font = pygame.font.SysFont('Stencil', 60)
        text = font.render(str(score), 1, RED)
        width = screen.get_width() / 2
        height = screen.get_height() / 2
        text_pos = text.get_rect(centerx=width, centery=height)
        screen.blit(text, text_pos)
        pygame.display.flip()
        pygame.time.wait(5000)

    def draw_get_ready_mess(self, screen):
        image = pygame.image.load('images/get_ready_mess.png')
        screen.blit(image, (0, 0))
        pygame.display.flip()
        pygame.time.wait(3000)

    def draw_go_mess(self, screen):
        image = pygame.image.load('images/go_mess.png')
        screen.blit(image, (0, 0))
        pygame.display.flip()
        pygame.time.wait(1000)

    def increase_level(self, score, length):
        if length in self.levels_table:
            self.speed -= 15
            pygame.mixer.Sound('sounds/level_up.wav').play()

    def get_start_option(self):
        while True:
            for event in pygame.event.get():
                if event.type == KEYDOWN and event.key == K_s:
                    return REGULAR_START
                if event.type == KEYDOWN and event.key == K_r:
                    return RANDOM_START
                if event.type == KEYDOWN and event.key == K_q:
                    return QUIT_GAME

    def generate_random_level(self):
        self.speed = random.randint(START_SPEED / 2, START_SPEED)
        num_of_obstan = int((DISPLAY_SIZE[0] * DISPLAY_SIZE[1]) * 0.00005)
        for item in range(0, num_of_obstan):
            self.obstancles.insert(0, Obstancle(RED, 50))

    def run(self, screen):
        pygame.display.set_caption('SnakeGame')
        background = pygame.Surface(screen.get_size())

        self.draw_welcome_mess(screen)

        start_type = self.get_start_option()

        if start_type == QUIT_GAME:
            return
        if start_type == RANDOM_START:
            self.generate_random_level()

        self.draw_get_ready_mess(screen)

        self.draw_go_mess(screen)

        snake = Snake()
        snake.born()
        player = Player()
        sprites = pygame.sprite.RenderPlain((snake, self.food))
        start_time = 0
        end_time = 0
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == KEYDOWN and event.key == K_ESCAPE:
                    return
                if event.type == KEYDOWN:
                    if event.key == K_RIGHT:
                        snake.change_direction(RIGHT)
                    if event.key == K_LEFT:
                        snake.change_direction(LEFT)
                    if event.key == K_DOWN:
                        snake.change_direction(DOWN)
                    if event.key == K_UP:
                        snake.change_direction(UP)

            snake.move()

            if snake.rect.colliderect(self.food.rect):
                player.increase_score()
                self.obstancles.insert(0, Obstancle(RED, 0))
                self.increase_level(player.get_score(), snake.get_length())
                self.food.__init__(GREEN, self.obstancles)
                start_time = pygame.time.get_ticks()
                snake.grow()
                self.eat_sound.play()

            for obstancle in self.get_obstancles():
                if (snake.rect.colliderect(obstancle.rect)):
                    snake.die()

            screen.blit(background, (0, 0))

            if snake.is_alife == False:
                self.draw_game_over_mess(screen, player.get_score())
                return
            else:
                sprites.update()
                sprites.draw(screen)

                for rect in snake.snake_elements:
                    screen.blit(snake.image, rect)

                for obstancle in self.get_obstancles():
                    screen.blit(obstancle.image, obstancle)

                pygame.display.flip()

            end_time = pygame.time.get_ticks()

            if (end_time - start_time) / 1000 >= TIME_DISAPPEAR:
                self.food.__init__(GREEN, self.obstancles)
                start_time = pygame.time.get_ticks()

            pygame.time.wait(self.speed)


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY_SIZE)
    Game().run(screen)
