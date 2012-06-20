import pygame
import random
from pygame.locals import *

RIGHT = 1
LEFT = 2
DOWN = 3
UP = 4

LEVELS_TABLE = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200] 

class Snake(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((7, 7))
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.rect = pygame.draw.rect(self.image, (0, 255, 255), self.rect)
        
        self.curr_direction = RIGHT
        self.new_direction = RIGHT
        self.snake_container = [(20, 20)];
        self.coord_x = 20
        self.coord_y = 20
        self.is_alife = True
        self.length = 1
    
    def grow(self):
        self.length = self.length + 1
    
    def dead(self):
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
        if self.new_direction == 1:
            self.curr_direction = 1
            self.coord_x += 10
            if self.coord_x >= 640:
                self.coord_x = 640
                self.is_alife = False
                return

        elif self.new_direction == 2: # left
            self.curr_direction = 2
            self.coord_x -= 10
            if self.coord_x < 0:
                self.coord_x = 0
                self.is_alife = False
                return

        elif self.new_direction == 3: # down
            self.curr_direction = 3
            self.coord_y += 10
            if self.coord_y >= 480:
                self.coord_y = 480
                self.is_alife = False
                return

        elif self.new_direction == 4: # up
            self.curr_direction = 4
            self.coord_y -= 10
            if self.coord_y < 0:
                self.coord_y = 0
                self.is_alife = False
                return

        for segment in self.snake_container[:]:
            if (segment[0] == self.rect.left) and (segment[1] == self.rect.top):
            #if self.rect.collidepoint(segment[0], segment[1]):
                self.is_alife = False
                return

        self.snake_container.insert(0, (self.rect.left, self.rect.top))
        self.snake_container = self.snake_container[0:self.length-1]	

        if self.length < 3: # 3 is the minimum length of snake
            self.length += 1

        self.rect.left = self.coord_x
        self.rect.top = self.coord_y

    def update(self):
        pass

class Piece(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((9, 9))
        self.rect = self.image.get_rect()
        self.rect = pygame.draw.rect(self.image, color, self.rect)
        self.rect.left = x
        self.rect.top = y

class Food(Piece):
    def __init__(self, color, obstancles):
        coord_x = random.randint(5,16) * 25
        coord_y = random.randint(5,16) * 25
        index = 0
        if len(obstancles) != 0:
            flag = False
            index += 1
            while True:
                print('zaciklqm', index)
                for obstancle in obstancles:
                    if coord_x != obstancle.rect.left and coord_y != obstancle.rect.top:
                        flag = True
                        break
                if flag == True:
                    break
                else:
                    coord_x = random.randint(5,28)*20
                    coord_y = random.randint(5,20)*20
        
        Piece.__init__(self, color, coord_x, coord_y)
        
    def update(self):
        pass

class Obstancle(Piece):
    def __init__(self, color):
        Piece.__init__(self, color, random.randint(0,32)*20, random.randint(0,24)*20)

    def update(self):
        pass
  
class Game(object):

    def __init__(self):
        self.score = 0
        self.speed = 100
        self.obstancles = []
        self.food = Food((0, 255, 0), self.obstancles)
        self.level = 0
        self.levels_table = set([40, 80, 120, 160, 180, 200, 220])
    
    def get_obstancles(self):
        return self.obstancles

    def increase_score(self):
        self.score += 5
        
    def get_score(self):
        return self.score
        
    def welcome_mess(self, screen):
        font = pygame.font.Font(None, 60)
        text = font.render("HUNGRY SNAKE", 1, (0, 255, 255))
        textpos = text.get_rect(centerx = (screen.get_width()/2), centery = screen.get_height()/2 - 200)
        screen.blit(text, textpos)
        
        font = pygame.font.Font(None, 30)
        text = font.render("Try to reach ", 1, (255, 255, 255))
        textpos = text.get_rect(centerx = screen.get_width()/2 - 100, centery = (screen.get_height()/2 - 30))
        screen.blit(text, textpos)
        
        text = font.render("green rectangles", 1, (0, 255, 0))
        textpos = text.get_rect(centerx = screen.get_width()/2 + 45, centery = (screen.get_height()/2 - 30))
        screen.blit(text, textpos)
        
        text = font.render("Escape ", 1, (255, 255, 255))
        textpos = text.get_rect(centerx = screen.get_width()/2 - 122, centery = (screen.get_height()/2))
        screen.blit(text, textpos)
        
        text = font.render("red rectangles", 1, (255, 0, 0))
        textpos = text.get_rect(centerx = screen.get_width()/2 - 10, centery = (screen.get_height()/2))
        screen.blit(text, textpos)
 
        
    def get_ready(self, screen):
        font = pygame.font.Font(None, 60)
        text = font.render("GET READY!", 1, (0, 255, 255))
        textpos = text.get_rect(centerx = (screen.get_width()/2), centery = screen.get_height()/2)
        screen.blit(text, textpos)
        
    def go(self, screen):
        font = pygame.font.Font(None, 60)
        text = font.render("GO!", 1, (0, 255, 255))
        textpos = text.get_rect(centerx = (screen.get_width()/2), centery = screen.get_height()/2)
        screen.blit(text, textpos)
        
            
    def increase_level(self):
        if self.score in self.levels_table:
            self.speed -= 10
    
    def run(self, screen):
        
        pygame.display.set_caption('SnakeGame')
        background = pygame.Surface(screen.get_size())
        background = background.convert()
        background.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        pygame.display.flip()
        self.welcome_mess(screen)

        pygame.display.flip()
        pygame.time.delay(10000)
        background.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        pygame.display.flip()
        self.get_ready(screen)
        pygame.display.flip()
        pygame.time.delay(3000)
        
        background.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        pygame.display.flip()
        self.go(screen)
        pygame.display.flip()
        pygame.time.delay(1000)
        
        snake = Snake()
        allsprites = pygame.sprite.RenderPlain((snake, self.food))
        #pygame.time.delay(10000)
        pygame.event.clear()
        
        #self.get_ready(screen)
        #pygame.time.delay(1000)
        pygame.event.clear()
        while True:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
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
            
            if snake.rect.collidepoint(self.food.rect.left, self.food.rect.top):
                self.increase_score()
                self.obstancles.insert(0, Obstancle((255, 0, 0)))
                self.increase_level()
                self.food.__init__((0, 255, 0), self.obstancles)
                snake.grow()
                
                
            for obstancle in self.obstancles:
                if (snake.rect.collidepoint(obstancle.rect.left, obstancle.rect.top)):
                    snake.dead()

            screen.blit(background, (0, 0))
            
            if snake.is_alife == False:
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
    screen = pygame.display.set_mode((640, 480))
    Game().run(screen)