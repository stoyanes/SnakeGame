import pygame
import random
from pygame.locals import *

DISPLAY_SIZE = (640, 480)

RIGHT = 1
LEFT = 2
DOWN = 3
UP = 4

GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
CYAN = (0, 255, 255)

REGULAR_START = 0
RANDOM_START = 1
QUIT_GAME = 2

SNAKE_BODY = (7, 9)
START_SPEED = 100

class Snake(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(SNAKE_BODY)
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.rect = pygame.draw.rect(self.image, (0, 255, 255), self.rect)
        
        self.curr_direction = RIGHT
        self.new_direction = RIGHT
        self.snake_container = [(20, 20)];
        self.coord_x = 20
        self.coord_y = 20
        self.is_alife = True
        self.length = 3
    
    def grow(self):
        self.length = self.length + 1
    
    def die(self):
        self.is_alife = False

    def change_direction(self, direction):
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
        if self.new_direction == RIGHT:
            self.curr_direction = RIGHT
            self.coord_x += 10
            if self.coord_x >= DISPLAY_SIZE[0]:
                self.coord_x = DISPLAY_SIZE[0]
                self.is_alife = False
                return

        elif self.new_direction == LEFT:
            self.curr_direction = LEFT
            self.coord_x -= 10
            if self.coord_x < 0:
                self.coord_x = 0
                self.is_alife = False
                return

        elif self.new_direction == DOWN:
            self.curr_direction = DOWN
            self.coord_y += 10
            if self.coord_y >= DISPLAY_SIZE[1]:
                self.coord_y = DISPLAY_SIZE[1]
                self.is_alife = False
                return

        elif self.new_direction == UP:
            self.curr_direction = UP
            self.coord_y -= 10
            if self.coord_y < 0:
                self.coord_y = 0
                self.is_alife = False
                return

        for segment in self.snake_container:
            if (segment[0] == self.rect.left) and (segment[1] == self.rect.top):
                self.is_alife = False
                return

        self.snake_container.insert(0, (self.rect.left, self.rect.top))
        self.snake_container = self.snake_container[0:self.length-1]	

        self.rect.left = self.coord_x
        self.rect.top = self.coord_y

class Piece(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.rect = self.image.get_rect()
        self.rect = pygame.draw.rect(self.image, color, self.rect)
        self.rect.left = x
        self.rect.top = y

class Food(Piece):
    def __init__(self, color, obstancles):
        coord_x = random.randint(0, DISPLAY_SIZE[0] - SNAKE_BODY[1])
        coord_y = random.randint(0, DISPLAY_SIZE[1] - SNAKE_BODY[1])
        index = 0
        if len(obstancles) != 0:
            flag = False
            while True:
                for obstancle in obstancles:
                    #if coord_x != obstancle.rect.left and coord_y != obstancle.rect.top:
                    if not obstancle.rect.collidepoint(coord_x, coord_y):
                        flag = True
                        break
                if flag == True:
                    break
                else:
                    coord_x = random.randint(0, DISPLAY_SIZE[0] - SNAKE_BODY[1])
                    coord_y = random.randint(0, DISPLAY_SIZE[1] - SNAKE_BODY[1])
        
        Piece.__init__(self, color, coord_x, coord_y)

class Obstancle(Piece):
    def __init__(self, color, obstan_position_ratio):
        coord_x = random.randint(0,DISPLAY_SIZE[0])
        coord_y = random.randint(0,DISPLAY_SIZE[1]) + obstan_position_ratio
        Piece.__init__(self, color, coord_x, coord_y)

class Game(object):

    def __init__(self):
        self.score = 0
        self.speed = START_SPEED
        self.obstancles = []
        self.food = Food((0, 255, 0), self.obstancles)
        self.level = 0
        self.levels_table = set([40, 80, 120, 160, 180, 200, 220])
        self.level_up = pygame.mixer.Sound('sounds/level_up.wav')
        self.eat_sound = pygame.mixer.Sound('sounds/eat.wav')
        self.game_over_sound = pygame.mixer.Sound('sounds/game_over.wav')
    
    def get_obstancles(self):
        return self.obstancles

    def increase_score(self):
        self.score += 5
        
    def get_score(self):
        return self.score
        
    def welcome_mess(self, screen):
        image = pygame.image.load('images/well_mess.png')
        screen.blit(image,(0, 0))
        pygame.display.flip()
        
    def game_over_mess(self, screen):
        image = pygame.image.load('images/game_over_mess.png')
        screen.blit(image,(0, 0))
        pygame.display.flip()
        self.game_over_sound.play()
        pygame.time.delay(10000)
        
    def get_ready(self, screen):
        image = pygame.image.load('images/get_ready_mess.png')
        screen.blit(image, (0, 0))
        pygame.display.flip()
        pygame.time.wait(3000)
        
    def go(self, screen):
        image = pygame.image.load('images/go_mess.png')
        screen.blit(image, (0, 0))
        pygame.display.flip()
        pygame.time.wait(1000)
            
    def increase_level(self):
        if self.score in self.levels_table:
            self.speed -= 10
            self.level_up.play()

        
    
    def wait_to_start(self):
        while True:
            for event in pygame.event.get():
                if event.type == KEYDOWN and event.key == K_s:
                    return REGULAR_START
                if event.type == KEYDOWN and event.key == K_r:
                    return RANDOM_START
                if event.type == KEYDOWN and (event.key == K_q or event.key == K_ESCAPE):
                    return QUIT_GAME
    
    def generate_random_level(self):
        self.speed = random.randint(START_SPEED/2, START_SPEED)
        number_of_obstancles = int ((DISPLAY_SIZE[0] * DISPLAY_SIZE[1]) * 0.00005)
        for item in range(0, number_of_obstancles):
            self.obstancles.insert(0, Obstancle(RED, 50))
        
    def run(self, screen):
        
        pygame.display.set_caption('SnakeGame')
        background = pygame.Surface(screen.get_size())
        
        self.welcome_mess(screen)
        
        start_type = self.wait_to_start()
        
        if start_type == QUIT_GAME:
            return
        if start_type == RANDOM_START:
            self.generate_random_level()
        
        self.get_ready(screen)

        self.go(screen)

        snake = Snake()
        allsprites = pygame.sprite.RenderPlain((snake, self.food))
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
                self.eat_sound.play()
                self.increase_score()
                self.obstancles.insert(0, Obstancle(RED, 0))
                self.increase_level()
                self.food.__init__(GREEN, self.obstancles)
                snake.grow()

            for obstancle in self.obstancles:
                if (snake.rect.colliderect(obstancle.rect)):
                    snake.die()

            screen.blit(background, (0, 0))
            
            if snake.is_alife == False:
                self.game_over_mess(screen)                
                return
            else:
                allsprites.update()
                allsprites.draw(screen)

                for segment in snake.snake_container:
                    screen.blit(snake.image, segment)
                    
                for obstancle in self.obstancles:
                    screen.blit(obstancle.image, obstancle)

                pygame.display.flip()  
            pygame.time.delay(self.speed)

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY_SIZE)
    Game().run(screen)