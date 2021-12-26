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

    def test_move_up(self):
        self.level.game_state = [[2,0,0,0],[0,2,2,0],[2,2,2,2],[2,0,0,2]]

        self.level._move_up()

        expected = [[4,4,4,4],[2,0,0,0],[0,0,0,0],[0,0,0,0]]

        self.assertEqual(self.level.game_state, expected)

    def test_move_down(self):
        self.level.game_state = [[2,0,0,0],[0,2,2,0],[2,2,2,2],[2,0,0,2]]

        self.level._move_down()

        expected = [[0,0,0,0],[0,0,0,0],[2,0,0,0],[4,4,4,4]]

        self.assertEqual(self.level.game_state, expected)

    def test_move_left(self):
        self.level.game_state = [[2,0,2,0],[0,2,2,0],[0,2,0,2],[0,0,0,2]]

        self.level._move_left()

        expected = [[4,0,0,0],[4,0,0,0],[4,0,0,0],[2,0,0,0]]

        self.assertEqual(self.level.game_state, expected)

    def test_move_right(self):
        self.level.game_state = [[2,0,2,0],[0,2,2,0],[0,2,0,2],[0,0,0,2]]

        self.level._move_right()

        expected = [[0,0,0,4],[0,0,0,4],[0,0,0,4],[0,0,0,2]]

        self.assertEqual(self.level.game_state, expected)

    def test_game_over(self):
        self.level.game_state = [[2,4,3,5],[7,6,8,9],[14,12,13,11],[15,16,17,19]]

        value = self.level._game_over()

        self.assertEqual(value, True)

        self.level.game_state = [[2,0,2,0],[0,2,2,0],[0,2,0,2],[0,0,0,2]]

        value = self.level._game_over()

        self.assertEqual(value, False)
