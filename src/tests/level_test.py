import unittest
import pygame
from level import Level

class TestLevel(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.level = Level(320, 100)

    def test_create_new_tile(self):
        placeholder_state = []
        for x in range(4):
            placeholder_state.append(self.level.game_state[x].copy())

        self.level._create_new_tile()

        self.assertNotEqual(placeholder_state, self.level.game_state)

    def test_flatten(self):
        self.level.game_state = [[2,0,2,0],[0,2,2,0],[0,2,0,2],[0,0,0,2]]

        self.level._flatten()

        expected = [[2,2,0,0],[2,2,0,0],[2,2,0,0],[2,0,0,0]]

        self.assertEqual(self.level.game_state, expected)

    def test_combine(self):
        self.level.game_state = [[2,2,0,0],[4,4,0,0],[2,2,9,9],[0,0,0,2]]

        self.level._combine()

        expected = [[4,0,0,0],[8,0,0,0],[4,0,18,0],[0,0,0,2]]

        self.assertEqual(self.level.game_state, expected)

    def test_reverse(self):
        self.level.game_state = [[2,0,2,0],[0,2,2,0],[0,2,0,2],[0,0,0,2]]

        self.level._reverse()

        expected = [[0,2,0,2],[0,2,2,0],[2,0,2,0],[2,0,0,0]]

        self.assertEqual(self.level.game_state, expected)

    def test_change_axis(self):
        self.level.game_state = [[2,0,0,0],[0,2,2,0],[2,2,2,2],[2,0,0,2]]

        self.level._change_axis()

        expected = [[2,0,2,2],[0,2,2,0],[0,2,2,0],[0,0,2,2]]

        self.assertEqual(self.level.game_state, expected)