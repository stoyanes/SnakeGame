import unittest
from snake import *


class SnakeGameTests(unittest.TestCase):
    
    def setUp(self):
        self.snake = Snake()
        
    def test_snake_grow_after_eating(self):
        leng = self.snake.length
        self.snake.grow()
        self.assertEqual(self.snake.length, leng + 1)
        
    def test_change_direnction(self):
        self.snake.change_direction(RIGHT)
        self.assertTrue(self.snake.new_direction == RIGHT)
        
        self.snake.change_direction(LEFT)
        self.assertTrue(self.snake.new_direction != LEFT)
        
        self.snake.change_direction(UP)
        self.assertTrue(self.snake.new_direction == UP)
        
        self.snake.change_direction(DOWN)
        self.assertTrue(self.snake.new_direction == DOWN)
        
    
        
        
    
if __name__ == '__main__':
    unittest.main()