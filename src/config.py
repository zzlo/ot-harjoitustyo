import math

class Configuration:
    def __init__(self):
        self.display_height = 640
        self.display_width = self.display_height
        self.score_height = self.display_height / 3.2
        self.font_size = math.floor(self.display_height / 12.8)