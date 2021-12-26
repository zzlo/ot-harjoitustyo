import pygame
from config import Configuration

class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_x=0, tile_y=0, tile_width = 64, value = 2):
        super().__init__()

        self.conf = Configuration()
        width = tile_width
        height = width

        self.image = pygame.Surface([width, height])
        self._fill_with_colour(value)

        self.rect = self.image.get_rect()

        self.rect.x = tile_x
        self.rect.y = tile_y

    def _fill_with_colour(self, value):
        colours = self.conf.colours

        self.image.fill(colours[value])
