import pygame

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
        self.old_direction = -1
        self.snake_container = [(25, 25)];
        self.coord_x = 25
        self.coord_y = 25
        self.is_alife = True
    
    def change_direction(self, direction):
        if self.curr_direction == RIGHT and direction == LEFT:
            return
        elif self.curr_direction == LEFT and direction == RIGHT:
            return
        elif self.curr_direction == UP and direction == DOWN:
            return
        elif self.curr_direction == DOWN and direction == UP:
            return
        else:
            self.old_direction = self.curr_direction
            self.new_direction = direction

class Game(object):
    def run(self, screen):
        pygame.display.set_caption('SnakeGame')
        background = pygame.Surface(screen.get_size())
        background = background.convert()
        background.fill((125, 250, 125))
        screen.blit(background, (0, 15))
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        return


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    Game().run(screen)

