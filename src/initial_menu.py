import pygame
from functions import *
from config import *
from game import game_loop
from ranking import show_ranking

scores = []

def main_menu(screen):
    # fondo
    background_menu = pygame.transform.scale(pygame.image.load("./src/assets/background_menu.jpg"), 
                                            SIZE_SCREEN)

    # seteo fuente
    font = pygame.font.SysFont(None, 48)

    # cargo musica de fondo
    playing_music = True
    try:
        pygame.mixer.music.load("./src/assets/background_sound.mp3")
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)
    except:
        None
    
    # # bottones
    play_button = pygame.Rect(CENTER_SCREEN[0] - BUTTON_WIDTH // 2, 250, BUTTON_WIDTH, BUTTON_HEIGHT)
    ranking_button = pygame.Rect(CENTER_SCREEN[0] - BUTTON_WIDTH // 2, 350, BUTTON_WIDTH, BUTTON_HEIGHT)
    quit_button = pygame.Rect(CENTER_SCREEN[0] - BUTTON_WIDTH // 2, 450, BUTTON_WIDTH, BUTTON_HEIGHT)
    mute_button = pygame.Rect(20, 580, BUTTON_HEIGHT, BUTTON_HEIGHT)

    running = True
    while running:
        screen.blit(background_menu, background_menu.get_rect())

        
        show_text(screen, "FROGGY", font, (WIDTH//2, 100), GREEN)

        create_button(screen, play_button, 'Play', GREEN, GREEN_PERSONALIZED)
        create_button(screen, ranking_button, 'Ranking', GREEN, GREEN_PERSONALIZED)
        create_button(screen, quit_button, 'Quit', GREEN, GREEN_PERSONALIZED)
        create_button(screen, mute_button, 'Mute', YELLOW, LIGHT_BLUE)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 250 < event.pos[1] < 250 + play_button.height:
                    game_loop(screen)
                elif 350 < event.pos[1] < 350 + ranking_button.height:
                    show_ranking(screen, scores)
                elif 450 < event.pos[1] < 450 + quit_button.height:
                    running = False
                elif 580 < event.pos[1] < 580 + mute_button.height:
                    if playing_music:
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.unpause()
                    playing_music = not playing_music




