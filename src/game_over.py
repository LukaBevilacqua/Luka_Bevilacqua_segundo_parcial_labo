import pygame
from functions import *
from config import *


def game_over_screen(screen, score: int, scores: list):
    pygame.mixer.music.stop()
    clock = pygame.time.Clock()

    # Guardar el puntaje en el archivo .json
    name = get_user_name(screen)
    save_data("scores.json", scores, name, score)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                running = False
                from initial_menu import main_menu
                main_menu(screen)

        screen.fill(BLACK)
        background_game_over = pygame.transform.scale(pygame.image.load("./src/assets/dead.png"),
                                                    SIZE_SCREEN)
        screen.blit(background_game_over, background_game_over.get_rect())
        font = pygame.font.SysFont(None, 48)
        show_text(screen, "Game Over", font, (WIDTH//2, 20), RED)
        show_text(screen, f"Score: {score}", font, (WIDTH // 2, HEIGHT // 2), YELLOW)
        show_text(screen, "press SPACE to continue", font, (WIDTH//2, HEIGHT - 70), RED)

        pygame.display.flip()
        clock.tick(FPS)
