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
        self.image = pygame.Surface((10, 10))
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.rect = pygame.draw.rect(self.image, (255, 255, 255), self.rect)
        
        self.curr_direction = RIGHT
        self.new_direction = RIGHT
        #self.old_direction = -1
        self.snake_container = [(25, 25)];
        self.coord_x = 25
        self.coord_y = 25
        self.is_alife = True
        self.length = 1
    
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
            if self.coord_x > 620:
                self.coord_x = 620
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
            if self.coord_y > 420:
                self.coord_y = 420
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

        # This part is a little tricky. self.train is an array, and so we want to insert
        # our current location into the *front* of the array.
        self.snake_container.insert(0, (self.rect.left, self.rect.top))
        # And then we'll chop off the end of the array if needed (to convey a sense of movement)
        self.snake_container = self.snake_container[0:self.length-1]	

        if self.length < 3: # 3 is the minimum length of snake
            self.length += 1

        # Update the rect for drawing later
        self.rect.left = self.coord_x
        self.rect.top = self.coord_y

class Piece(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.rect = self.image.get_rect()
        self.rect = pygame.draw.rect(self.image, (25, 200, 25),self.rect)
        self.rect.left = x
        self.rect.top = y

class Food(Piece):
    def __init__(self):
        Piece.__init__(self, random.randint(0,30)*20, random.randint(0,20)*20 )

class Obstancle(Piece):
    def __init__(self):
        Piece.__init__(self, random.randint(0,30)*20, random.randint(0,20)*20)
        
class Game(object):
    def run(self, screen):
        pygame.display.set_caption('SnakeGame')
        background = pygame.Surface(screen.get_size())
        background = background.convert()
        background.fill((125, 250, 125))
        screen.blit(background, (0, 15))
        pygame.display.flip()
        
        snake = Snake()
        food = Food()
        obstancle = Obstancle()
        allsprites = pygame.sprite.RenderPlain((snake, food))
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        return
                if event.type == KEYDOWN:
                    if event.key == K_RIGHT:
                        #presscount += 1
                        snake.change_direction(RIGHT)
                    if event.key == K_LEFT:
                        #presscount += 1
                        snake.change_direction(LEFT)
                    if event.key == K_DOWN:
                        #presscount += 1
                        snake.change_direction(DOWN)
                    if event.key == K_UP:
                        #presscount += 1
                        snake.change_direction(UP)
            snake.move()
            if (snake.rect.left == food.rect.left) and (snake.rect.top == food.rect.top):
                score += 17
                yumfruit.__init__()
                player.length += 1

            screen.blit(background, (0, 0))
            
            if snake.is_alife == False:
                #text = font.render("you totally lost!", 1, white)
                #textpos = text.get_rect(centerx = screen.get_width()/2, centery = screen.get_height()/2 - 60)
                #screen.blit(text, textpos)

                #text = font.render("final score: %d" % (score), 1, white)
                #textpos = (text.get_rect(centerx = screen.get_width()/2)[0], textpos[1] + 80)
                #screen.blit(text, textpos)
				
				# Show them
                pygame.display.flip()

				# Pause for 3 seconds so the user can notice that he or she has lost
                #Pause(3000)	
                return
            else:
                # Draw the fruit and stuff
                allsprites.update()
                allsprites.draw(screen)

                # Draw each bit of the snake
                for segment in snake.snake_container:
                    screen.blit(snake.image, segment)

                # Statusbar fun!
                #screen.blit(statusBar, (0, 440))
                
                #if score != 0: # Compute the efficiency of the player
                    #eff = "%.3f" % (100 - 4*(presscount / (score / 100.0)))
                #text = font.render("score: %d   lives left: %d   eff: %s" % (score, lives, eff), 1, black)
                #textpos = (text.get_rect(centerx = screen.get_width()/2)[0], 440)
                #screen.blit(text, textpos)

                # Show the complete, updated frame
                pygame.display.flip()
                
            pygame.time.delay(100)

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    Game().run(screen)

