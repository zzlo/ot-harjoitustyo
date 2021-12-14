import pygame
from level import Level
from ui.ui import Ui
from config import Configuration

def main():
    conf = Configuration()
    display_height = conf.display_height
    display_width = conf.display_width
    score_height = conf.score_height

    pygame.init()

    ui = Ui(display_width, display_height + score_height, score_height)

    clock = pygame.time.Clock()
    level = Level(display_height, score_height)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    level.move("l")
                if event.key == pygame.K_RIGHT:
                    level.move("r")
                if event.key == pygame.K_UP:
                    level.move("u")
                if event.key == pygame.K_DOWN:
                    level.move("d")
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if display_width * 0.07 <= mouse[0] <= display_width * 0.07 + 128 and score_height/1.5 <= mouse[1] <= score_height/1.5 + 32:
                    level = Level(display_height, score_height)
            elif event.type == pygame.QUIT:
                exit()

        ui.draw_background()
        level.all_sprites.draw(ui.screen)

        mouse = pygame.mouse.get_pos()

        pygame.draw.rect(ui.screen, (143,122,102), [display_width * 0.07, score_height/1.5, 128, 32])

        ui.draw_scoreboard(level.game_score, level.record_score)
        ui.screen.blit(level.text_surface, (0,0))
        ui.screen.blit(ui.text_surface, (0,0))
        ui.update_ui()

        clock.tick(60)


if __name__ == "__main__":
    main()
