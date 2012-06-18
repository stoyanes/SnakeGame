import pygame
import random
from pygame.locals import *

RIGHT = 1
LEFT = 2
DOWN = 3
UP = 4

class Snake(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((15, 15))
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.rect = pygame.draw.rect(self.image, (0, 255, 255), self.rect)
        
        self.curr_direction = RIGHT
        self.new_direction = RIGHT
        #self.old_direction = -1
        self.snake_container = [(0, 0)];
        self.coord_x = 0
        self.coord_y = 0
        self.is_alife = True
        self.length = 1
    
    def grow(self):
        self.length = self.length + 1
    
    def dead(self):
        self.is_alife = False

    def change_direction(self, direction):
        if self.curr_direction == RIGHT and self.new_direction == LEFT:
            return
        elif self.curr_direction == LEFT and self.new_direction == RIGHT:
            return
        elif self.curr_direction == DOWN and self.new_direction == UP:
            return
        elif self.curr_direction == UP and self.new_direction == DOWN:
            return
        else:
            self.new_direction = direction

    def move(self):
        if self.new_direction == 1:
            self.curr_direction = 1
            self.coord_x += 10
            if self.coord_x > 630:
                self.coord_x = 630
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
            if self.coord_y > 470:
                self.coord_y = 470
                self.is_alife = False
                return

        elif self.new_direction == 4: # up
            self.curr_direction = 4
            self.coord_y -= 10
            if self.coord_y < 0:
                self.coord_y = 0
                self.is_alife = False
                return

        #for segment in self.snake_container[:]:
            #if (segment[0] == self.rect.left) and (segment[1] == self.rect.top):
                #touched self (segment), omg died!
                #self.is_alife = False
                #return

        self.snake_container.insert(0, (self.rect.left, self.rect.top))
        self.snake_container = self.snake_container[0:self.length-1]	

        if self.length < 3: # 3 is the minimum length of snake
            self.length += 1

        # Update the rect for drawing later
        self.rect.left = self.coord_x
        self.rect.top = self.coord_y

    def update(self):
        pass

class Piece(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((11, 11))
        self.rect = self.image.get_rect()
        self.rect = pygame.draw.rect(self.image, color,self.rect)
        self.rect.left = x
        self.rect.top = y

class Food(Piece):
    def __init__(self, color):
        Piece.__init__(self,color, random.randint(0,30)*20, random.randint(0,20)*20 )
    def update(self):
        pass

class Obstancle(Piece):
    def __init__(self, color):
        Piece.__init__(self, color, random.randint(0,30)*20, random.randint(0,20)*20)

    def update(self):
        pass
        
class Game(object):
    def run(self, screen):
        score = 0
        pygame.display.set_caption('SnakeGame')
        background = pygame.Surface(screen.get_size())
        background = background.convert()
        background.fill((0, 0, 0))
        screen.blit(background, (0, 15))
        pygame.display.flip()
        
        snake = Snake()
        food = Food((255, 255, 0))
        obstancles = [Obstancle((255, 0, 0))]
        allsprites = pygame.sprite.RenderPlain((snake, food, obstancles[0]))
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
            
            if snake.rect.collidepoint(food.rect.left, food.rect.top):
                score += 17
                food.__init__((255, 255, 0))
                snake.grow()
                obstancles.insert(0, Obstancle((255, 0, 0)))
                
            for obstancle in obstancles:
                if (snake.rect.collidepoint(obstancle.rect.left, obstancle.rect.top)):
                    snake.dead()

            screen.blit(background, (0, 0))
            
            if snake.is_alife == False:
                print(score)
                return
            else:
                allsprites.update()
                allsprites.draw(screen)

                for segment in snake.snake_container:
                    screen.blit(snake.image, segment)
                    
                for obstancle in obstancles:
                    screen.blit(obstancle.image, obstancle)

                pygame.display.flip()
                
            pygame.time.delay(100)

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    Game().run(screen)