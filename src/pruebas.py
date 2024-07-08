import pygame
import sys
from config import *

# Inicializar Pygame
pygame.init()

# Configurar la pantalla
screen = pygame.display.set_mode(SIZE_SCREEN)
pygame.display.set_caption("Juego con Entrada de Nombre")

# Fuente
font = pygame.font.Font(None, 74)

# Función para manejar la entrada de texto
def get_user_name(screen):
    input_box = pygame.Rect(CENTER_SCREEN[0] - (BUTTON_WIDTH//2), CENTER_SCREEN[1], BUTTON_WIDTH, BUTTON_HEIGHT)
    color_inactive = GREEN
    color_active = GREEN_PERSONALIZED
    color = color_inactive
    active = False
    text = ''
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Si el usuario hace clic en el cuadro de entrada, activarlo.
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                # Cambiar el color del cuadro de entrada.
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        done = True
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.fill(WHITE)
        # Renderizar el texto
        txt_surface = font.render(text, True, color)
        # Ensanchar el cuadro de entrada si el texto es muy largo
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        # Dibujar el texto y el cuadro de entrada
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(screen, color, input_box, 2)

        pygame.display.flip()

    return text

# Reloj para controlar los FPS
clock = pygame.time.Clock()

# Bucle principal del juego
running = True
while running:
    screen.fill(WHITE)
    user_name = get_user_name(screen)
    # Puedes usar el nombre del usuario como quieras
    print(f"El nombre del usuario es: {user_name}")

    # Aquí es donde comenzaría el resto del juego

    running = False

    pygame.display.flip()
    clock.tick(60)

# Salir de Pygame
pygame.quit()
sys.exit()
