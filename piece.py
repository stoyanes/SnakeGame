import pygame


class Piece(pygame.sprite.Sprite):
    def __init__(self, color, coord_x, coord_y, rectan):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(rectan)
        self.rect = self.image.get_rect()
        self.rect = pygame.draw.rect(self.image, color, self.rect)
        self.rect.left = coord_x
        self.rect.top = coord_y

