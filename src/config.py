import math

class Configuration:
    def __init__(self):
        self.display_height = 640
        self.display_width = self.display_height
        self.score_height = self.display_height / 3.2
        self.font_size = math.floor(self.display_height / 12.8)
        self.colours = {
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