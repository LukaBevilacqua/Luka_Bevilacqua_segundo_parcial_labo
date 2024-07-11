import pygame
from functions import *
from config import *


def show_ranking(screen, scores):
    clock = pygame.time.Clock()
    
    
    background_ranking = pygame.transform.scale(pygame.image.load("./src/assets/background_ranking.jpg"), 
                                                SIZE_SCREEN)
    
    # Leer los scores desde un archivo .json
    scores = load_data("scores.json")

    sort_players(scores)

    quit_button = pygame.Rect(5, 5, 50, BUTTON_HEIGHT)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 5 < event.pos[1] < 5 + quit_button.height:
                    running = False

        screen.blit(background_ranking, background_ranking.get_rect())

        font = pygame.font.SysFont(None, 48)

        show_text(screen, "RANKING", font, (WIDTH//2, 50), BLACK)

        create_button(screen, quit_button, 'X', RED, RED_PERSONALIZED)

        y_offset = 100
        number = 1
        for score in scores:
            score_text = font.render(f'{number} - {score["name"]}: {score["score"]}', True, BLACK)
            screen.blit(score_text, (100, y_offset))
            y_offset += 40
            number += 1

        pygame.display.flip()
        clock.tick(FPS)
