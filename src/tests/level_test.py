import unittest
import pygame
from level import Level

class TestLevel(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.level = Level(320)
    
    def test_create_new_tile(self):
        placeholder_state = []
        for x in range(4):
            placeholder_state.append(self.level.game_state[x].copy())

        self.level._create_new_tile()
        
        self.assertNotEqual(placeholder_state, self.level.game_state)