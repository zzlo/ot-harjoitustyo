import pygame

class Ui:
    def __init__(self, display_width, display_height, score_height):
        self.display_width = display_width
        self.score_height = score_height
        self.screen = pygame.display.set_mode((display_width, display_height))
        self.font = pygame.font.SysFont("Helvetica", 25)
        self.text_surface = pygame.Surface((display_width, display_height), pygame.SRCALPHA)

        pygame.display.set_caption("2048")
        self.draw_background()
        self.update_ui()

    def draw_background(self):
        """Piirtää taustan.
        """
        self.screen.fill((187,173,160))

    def update_ui(self):
        """Päivittää ruudun.
        """
        pygame.display.flip()

    def draw_scoreboard(self, game_score, record_score):
        """Piirtää pistetilastot sisältävän tulostaulun ohjelman yläreunaan.

        Args:
            game_score: Nykyisen pelin pistesaldo
            record_score: Ennätyspistesaldo
        """
        self.text_surface.fill((0,0,0,0))

        self.text = self.font.render("new game", True, (0,0,0))
        self.text_surface.blit(self.text, (self.display_width * 0.07 + 9, self.score_height/1.5))

        text = self.font.render(f"current: {game_score}", True, (0,0,0))
        self.text_surface.blit(text,(self.display_width * 0.55, self.score_height/1.5))

        text = self.font.render(f"record: {record_score}", True, (0,0,0))
        self.text_surface.blit(text,(self.display_width * 0.57, self.score_height/5))