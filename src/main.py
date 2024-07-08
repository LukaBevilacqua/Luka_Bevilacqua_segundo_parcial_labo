import pygame
from config import *
from initial_menu import main_menu


# inicializar los modulos de pygame
pygame.init()

#configuracion pantalla principal
screen = pygame.display.set_mode(SIZE_SCREEN)
pygame.display.set_caption("Froggy")

icon = pygame.transform.scale(pygame.image.load("./src/assets/icon.png"), SIZE_SCREEN)
pygame.display.set_icon(icon)

if __name__ == '__main__':
    main_menu(screen)