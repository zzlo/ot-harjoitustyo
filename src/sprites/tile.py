import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_x=0, tile_y=0, value = 2):
        super().__init__()

        width = 64
        height = width

        self.image = pygame.Surface([width, height])
        self._fill_with_colour(value)

        self.rect = self.image.get_rect()

        self.rect.x = tile_x
        self.rect.y = tile_y

    def _fill_with_colour(self, value):
        colours = {
            0: (205, 193, 180),
            2: (238, 228, 218),
            4: (238, 225, 201),
            8: (243, 178, 122),
            16: (246, 150, 100),
            32: (246, 129, 96),
            64: (247, 95, 59),
            128: (237, 208, 115),
            256: (237, 204, 97),
            512: (237, 200, 80),
            1024: (237, 197, 63),
            2048: (237, 194, 46),
            4096: (94, 218, 146),
            8192: (39, 187, 103),
            16384: (35, 140, 81)
        }

        self.image.fill(colours[value])
