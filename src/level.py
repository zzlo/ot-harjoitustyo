import os
import random
import pygame
from sprites.tile import Tile
from config import Configuration

class Level:
    def __init__(self, display_size, highscore_height):
        conf = Configuration()
        self.highscore_height = highscore_height
        self.display_size = display_size
        self.text_surface = pygame.Surface((display_size, display_size + highscore_height), pygame.SRCALPHA)
        self.font = pygame.font.SysFont("Helvetica", conf.font_size)
        self.tiles = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.victory = False

        self.game_state = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

        self.game_score = 0
        self.record_score = self._read_score()

        self._initialize_sprites()

    def _initialize_sprites(self):
        """[summary]
        """
        self._create_new_tile()
        self._create_new_tile()
        self.game_score = 0

        self._add_sprites()

    def _add_sprites(self):
        tile_height = self.display_size / 5
        tile_width = tile_height

        spacing = tile_height/5

        self.all_sprites.empty()
        self.tiles.empty()
        self.text_surface.fill((0,0,0,0))

        for y in range(4):
            for x in range(4):
                normalized_x = x * tile_width + (x+1) * spacing
                normalized_y = y * tile_height + (y+1) * spacing + self.highscore_height

                self.tiles.add(Tile(normalized_x, normalized_y, tile_width, self.game_state[y][x]))

                if self.game_state[y][x] != 0:
                    text = self.font.render(f"{self.game_state[y][x]}", True, (0,0,0))
                    self.text_surface.blit(text,
                    (normalized_x + tile_width/2 - spacing/2,
                    normalized_y + tile_height/2 - spacing))

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

        if self.game_score > self.record_score:
            self.record_score = self.game_score
            self._save_score(self.game_score)
            self._add_sprites()

        if self._game_over():
            text = self.font.render("gameover!", True, (0,0,0))
            self.text_surface.blit(text,(self.display_size/3, self.highscore_height/3))
        elif self.victory:
            text = self.font.render("voitit!", True, (0,0,0))
            self.text_surface.blit(text,(self.display_size/3, self.highscore_height/3))

    def _game_over(self):
        """Tarkistaa onko pelilaudalla jäljellä laillisia siirtoja. Jos siirtoja ei ole, peli päättyy.

        Returns:
            True, jos siirtoja ei enää ole (peli ohi). False, jos siirtoja voi edelleen tehdä.
        """
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
        """Työntää laatat vasempaan reunaan, poistaen tyhjät laatat numerollisten laattojen välistä.
        """
        new_state = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

        for x in range(4):
            help_var = 0
            for y in range(4):
                if self.game_state[x][y] != 0:
                    new_state[x][help_var] = self.game_state[x][y]
                    help_var += 1
        self.game_state = new_state

    def _combine(self):
        """Yhdistää vaakatasossa vierekkäin olevat laatat (vasempaan suuntaan), poistamalla molemmat laatat ja luomalla yhden kaksi kertaa suuremman laatan.
        """
        for x in range(4):
            for y in range(3):
                if self.game_state[x][y] == 0:
                    continue

                if self.game_state[x][y] == self.game_state[x][y+1]:
                    self.game_state[x][y] *= 2
                    self.game_score += self.game_state[x][y]
                    self.game_state[x][y+1] = 0

                    if self.game_state[x][y] == 2048:
                        self.victory = True

    def _reverse(self):
        """Kääntää laatat vaakatasossa päinvastaiseksi.
        """
        new_state = []
        for x in range(4):
            new_state.append([])
            for y in range(4):
                new_state[x].append(self.game_state[x][3 - y])

        self.game_state = new_state

    def _change_axis(self):
        """Vaihtaa x- ja y-akselin paikat keskenään.
        """
        new_state = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

        for x in range(4):
            for y in range(4):
                new_state[x][y] = (self.game_state[y][x])

        self.game_state = new_state

    def _create_new_tile(self):
        """Arpoo jonkun tyhjän ruudun koordinaatit, ja luo sen paikalle joko 2- tai 4-arvoisen laatan.
        """
        x = random.randint(0,3)
        y = random.randint(0,3)

        while self.game_state[x][y] != 0:
            x = random.randint(0,3)
            y = random.randint(0,3)

        tile_randomizer = random.randint(0,99) + 1

        if tile_randomizer > 90:
            self.game_state[x][y] = 4
        else:
            self.game_state[x][y] = 2

    def _move_up(self):
        """Siirtää laatat yläreunaan, yhdistäen samanarvoiset, vierekkäiset laatat. Funktio vaihtaa pelilaudan akselit keskenään alussa ja lopussa,
        koska flatten siirtää laatat vasempaan reunaan.
        """
        self._change_axis()
        self._flatten()
        self._combine()
        self._flatten()
        self._change_axis()

    def _move_down(self):
        """Siirtää laatat alareunaan, yhdistäen samanarvoiset, vierekkäiset laatat. Funktio vaihtaa pelilaudan akselit keskenään sekä kääntää lisäksi laatat, alussa ja lopussa,
        koska flatten siirtää laatat vasempaan reunaan.
        """
        self._change_axis()
        self._reverse()
        self._flatten()
        self._combine()
        self._flatten()
        self._reverse()
        self._change_axis()

    def _move_left(self):
        """Siirtää laatat vasempaan reunaan, yhdistäen samanarvoiset, vierekkäiset laatat.
        """
        self._flatten()
        self._combine()
        self._flatten()

    def _move_right(self):
        """Siirtää laatat oikeaan reunaan, yhdistäen samanarvoiset, vierekkäiset laatat. Funktio kääntää laatat alussa ja lopussa, koska
        flatten siirtää laatat vasempaan reunaan.
        """
        self._reverse()
        self._flatten()
        self._combine()
        self._flatten()
        self._reverse()

    def _save_score(self, score):
        """Tallentaa score-muuttujassa annetun tuloksen highscore-tiedostoon.

        Args:
            score: Tiedostoon tallennettava luku.
        """
        file_path = "./"
        file_name = "highscore.txt"

        name = os.path.join(file_path, file_name)
        f = open(name, "w")
        f.write(str(score))
        f.close()

    def _read_score(self):
        file_path = "./"
        file_name = "highscore.txt"
        name = os.path.join(file_path, file_name)

        if not os.path.isfile(name):
            return 0

        f = open(name, "r")
        
        score = int(f.read())
        f.close()

        return score
