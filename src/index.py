import pygame
from level import Level

def main():
    height = 5
    width = 5
    display_height = 64 * height
    display_width = width * 64

    pygame.init()

    screen = pygame.display.set_mode((display_width, display_height))

    pygame.display.set_caption("2048")

    clock = pygame.time.Clock()
    level = Level(display_height)

    screen.fill((187,173,160))
    pygame.display.flip()

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
            elif event.type == pygame.QUIT:
                exit()

        screen.fill((187,173,160))
        level.all_sprites.draw(screen)
        screen.blit(level.text_surface, (0,0))
        pygame.display.flip()
        
        clock.tick(60)


if __name__ == "__main__":
    main()