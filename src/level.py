import random
import pygame
from sprites.tile import Tile

class Level:
    def __init__(self, display_size, highscore_height):
        self.highscore_height = highscore_height
        self.display_size = display_size
        self.text_surface = pygame.Surface((display_size, display_size + highscore_height), pygame.SRCALPHA)
        self.font = pygame.font.SysFont("Helvetica", 25)
        self.tiles = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()

        self.game_state = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

        self.game_score = 0

        self._initialize_sprites()

    def _initialize_sprites(self):
        self._create_new_tile()
        self._create_new_tile()

        self._add_sprites()

    def _add_sprites(self):
        height = 4
        width = 4
        spacing = 12.8

        tile_height = 64
        tile_width = tile_height

        self.all_sprites.empty()
        self.tiles.empty()
        self.text_surface.fill((0,0,0,0))

        for y in range(height):
            for x in range(width):
                normalized_x = x * 64 + (x+1) * spacing
                normalized_y = y * 64 + (y+1) * spacing + self.highscore_height

                self.tiles.add(Tile(normalized_x, normalized_y, self.game_state[y][x]))

                if self.game_state[y][x] != 0:
                    text = self.font.render(f"{self.game_state[y][x]}", True, (0,0,0))
                    self.text_surface.blit(text,
                    (normalized_x + tile_width/2 - spacing/2,
                    normalized_y + tile_height/2 - spacing))

        text = self.font.render(f"highscore: {self.game_score}", True, (0,0,0))
        self.text_surface.blit(text,(self.display_size/3, self.highscore_height/3))

        self.all_sprites.add(
            self.tiles
        )

    def move(self, key):
        placeholder = self.game_state

        if key == "r":
            self._move_right()
        elif key == "l":
            self._move_left()
        elif key == "u":
            self._move_up()
        elif key == "d":
            self._move_down()

        if placeholder != self.game_state:
            self._create_new_tile()
            self._add_sprites()

        if self._game_over():
            print("***game over***")
            print("---------------")
            print(self.game_score)
            text = self.font.render("gameover!", True, (0,0,0))
            self.text_surface.blit(text,(self.display_size/3, self.highscore_height/3 - 25))

    def _game_over(self):
        for x in range(4):
            for y in range(4):
                if self.game_state[x][y] == 0:
                    return False

        for x in range(3):
            for y in range(3):
                if self.game_state[x][y] == self.game_state[x+1][y] or self.game_state[x][y] == self.game_state[x][y+1]:
                    return False

        for i in range(3):
            if self.game_state[3][i] == self.game_state[3][i+1] or self.game_state[i][3] == self.game_state[i+1][3]:
                return False

        return True

    def _flatten(self):
        new_state = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

        for x in range(4):
            help_var = 0
            for y in range(4):
                if self.game_state[x][y] != 0:
                    new_state[x][help_var] = self.game_state[x][y]
                    help_var += 1
        self.game_state = new_state

    def _combine(self):
        for x in range(4):
            for y in range(3):
                if self.game_state[x][y] == 0:
                    continue

                if self.game_state[x][y] == self.game_state[x][y+1]:
                    self.game_state[x][y] *= 2
                    self.game_score += self.game_state[x][y]
                    self.game_state[x][y+1] = 0

    def _reverse(self):
        new_state = []
        for x in range(4):
            new_state.append([])
            for y in range(4):
                new_state[x].append(self.game_state[x][3 - y])

        self.game_state = new_state

    def _change_axis(self):
        new_state = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

        for x in range(4):
            for y in range(4):
                new_state[x][y] = (self.game_state[y][x])

        self.game_state = new_state

    def _create_new_tile(self):
        x = random.randint(0,3)
        y = random.randint(0,3)

        while self.game_state[x][y] != 0:
            x = random.randint(0,3)
            y = random.randint(0,3)

        tile_randomizer = random.randint(0,99) + 1

        if tile_randomizer > 90:
            self.game_state[x][y] = 4
            self.game_score += 4
        else:
            self.game_state[x][y] = 2
            self.game_score += 2

    def _move_up(self):
        self._change_axis()
        self._flatten()
        self._combine()
        self._flatten()
        self._change_axis()

    def _move_down(self):
        self._change_axis()
        self._reverse()
        self._flatten()
        self._combine()
        self._flatten()
        self._reverse()
        self._change_axis()

    def _move_left(self):
        self._flatten()
        self._combine()
        self._flatten()

    def _move_right(self):
        self._reverse()
        self._flatten()
        self._combine()
        self._flatten()
        self._reverse()
