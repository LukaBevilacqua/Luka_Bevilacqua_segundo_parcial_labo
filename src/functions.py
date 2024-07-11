def create_block(left = 0, top = 0, width = 50, height = 50, colour = (255, 255, 255),
                direction = 3, edge = 0, radius = -1, speed_x = 5, speed_y = 5, img = None)-> dict:
    """crea un bloque usando pygame.

    Args:
        left (int, optional): posicion en x. Defaults to 0.
        top (int, optional): posicion en y. Defaults to 0.
        width (int, optional): ancho del bloque. Defaults to 50.
        height (int, optional): altura del bloque. Defaults to 50.
        colour (tuple, optional): color del bloque. Defaults to (255, 255, 255).
        direction (int, optional): direccion del bloque. Defaults to 3.
        edge (int, optional): borde del bloque. Defaults to 0.
        radius (int, optional): radio del bloque. Defaults to -1.
        speed_x (int, optional): velocidad en el eje x. Defaults to 5.
        speed_y (int, optional): velocidad en el eje y. Defaults to 5.
        img (_type_, optional): imagen del bloque. Defaults to None.

    Returns:
        dict: bloque en un diccionario
    """
    import pygame
    if img:
        img = pygame.transform.scale(img, (width, height))
    rect = pygame.Rect(left, top, width, height)
    return {"rect": rect, "color": colour, "dir": direction, "edge": edge, "radius": radius, "speed_x": speed_x, "speed_y": speed_y, "img": img}

def show_text(surface, text: str, font: str, pos: tuple[int, int],
            color_font: tuple[int, int, int], color_background: tuple[int, int, int] = None) -> None:
    """muestra el texto en la pantalla.

    Args:
        surface (surface): superficie donde se va a mostrar el texto
        text (str): texto a mostrar
        font (str): fuente con la que se escribe el texto
        pos (tuple[int, int]): posicion del texto
        color_font (tuple[int, int, int]): color de las letras del texto
        color_background (tuple[int, int, int], optional): color del rectangulo del texto. Defaults to None.
    """
    surface_text = font.render(text, True, color_font, color_background)
    rect_text = surface_text.get_rect(center = pos)
    surface.blit(surface_text, rect_text)


def finish()-> None:
    """termina un bucle de pygame.
    """
    import pygame, sys
    pygame.quit()
    sys.exit()


def show_text_button(surface, text: str, x: int, y: int, font_size: int = 36,
                    colour: tuple[int, int, int] = (0, 0, 0))-> None:
    """muestra el texto de un boton.

    Args:
        surface (surface): superficie donde se va a mostrar el texto
        text (str): texto a mostrar
        x (int): posicion del texto en la coordenada x
        y (int): posicion del texto en la coordenada y
        font_size (int, optional): tamaño de la fuente. Defaults to 36.
        colour (tuple[int, int, int], optional): color del texto. Defaults to (0, 0, 0).
    """
    import pygame
    font = pygame.font.SysFont(None, font_size)
    render = font.render(text, True, colour)
    rect_text = render.get_rect(center = (x, y))
    surface.blit(render, rect_text)

def create_button(screen, rect, text: str, colour_button: tuple, colour_hover: tuple)-> None:
    """crea un boton y lo muestra en pantalla.

    Args:
        screen (surface): superficie donde se va a mostrar el boton
        rect (rect): rectangulod el boton
        text (str): texto del boton a mostrar
        colour_button (tuple): color del boton cuando no esta por ser utilizado
        colour_hover (tuple): color del boton cuando va a ser utilizado
    """
    import pygame
    mouse_position = pygame.mouse.get_pos()
    if rect.collidepoint(mouse_position):
        pygame.draw.rect(screen, colour_hover, rect, border_radius=10)
    else:
        pygame.draw.rect(screen, colour_button, rect, border_radius=10)
    show_text_button(screen, text, rect.centerx, rect.centery)

def handler_new_coin(list: list, width_screen: int, height_screen: int,
                    size_coin: int, colour: tuple[int, int, int], img):
    """crea una nueva moneda y la agrega a una lista.

    Args:
        list (list): lista donde se agregan las monedas
        width_screen (int): ancho de la pantalla
        height_screen (int): alto de la pantalla
        size_coin (int): tamaño de la moneda
        colour (tuple[int, int, int]): color de la moneda
        img (_type_): imagen de la moneda
    """
    from random import randint
    list.append((create_block(randint(0, width_screen - size_coin), randint(0, height_screen - 
            size_coin), size_coin, size_coin, colour, radius = size_coin // 2, img= img)))

def get_user_name(screen)-> str:
    import pygame
    from config import CENTER_SCREEN, BUTTON_HEIGHT, BUTTON_WIDTH, GREEN, GREEN_PERSONALIZED, BLACK, WIDTH, HEIGHT
    input_box = pygame.Rect(CENTER_SCREEN[0] - (BUTTON_WIDTH//2), CENTER_SCREEN[1],
                            BUTTON_WIDTH, BUTTON_HEIGHT)
    color_inactive = GREEN
    color_active = GREEN_PERSONALIZED
    color = color_inactive
    active = False
    text = ''
    done = False

    font = pygame.font.SysFont(None, 48)

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Si el usuario hace clic en el cuadro de entrada, activarlo.
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                # Cambiar el color del cuadro de entrada.
                if active:
                    color = color_active
                else:
                    color_inactive
            
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        done = True
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.fill(BLACK)
        # Renderizar el texto
        txt_surface = font.render(text, True, color)
        # Ensanchar el cuadro de entrada si el texto es muy largo
        width = max(200, txt_surface.get_width() + 10)
        input_box.width = width
        # Dibujar el texto y el cuadro de entrada
        show_text(screen, "Ingrese su nombre", font, (WIDTH // 2, 70), GREEN)
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(screen, color, input_box, 2)

        pygame.display.flip()

    return text

def pause(button: int)-> None:
    """pausa el juego.

    Args:
        button (int): tecla a apretar para pausar el juego
    """
    import pygame
    continuar = True
    while continuar:    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish()
            if event.type == pygame.KEYDOWN:
                if event.key == button:
                    continuar = False

def load_enemies(list: list, quantity: int, enemy_size: tuple[int, int],
                color: tuple[int, int, int], image)-> None:
    """carga los enemigos.

    Args:
        list (list): lista de los enemigos
        quantity (int): cantidad de enemigos a cargar en la lista
        enemy_size (tuple[int, int]): tamaño del enemigo
        color (tuple[int, int, int]): color del enemigo
        image (_type_): imagen del enemigo
    """
    from random import randint
    from config import WIDTH, HEIGHT, BLOCK_HEIGHT
    for enemy in range(quantity):
        enemy = create_block(randint(0, WIDTH), randint(0, (HEIGHT - BLOCK_HEIGHT)),
                                width = enemy_size[0], height = enemy_size[1], colour = color, 
                                img= image)
        list.append(enemy)

def get_path(filename: str)-> str:
    """obtiene el path.

    Args:
        filename (str): nombre del archivo

    Returns:
        str: path completo
    """
    import os
    current_directory = os.path.dirname(__file__)
    return os.path.join(current_directory, filename)

def save_data(filename: str, list: list, player_name: str, score: int)-> None:
    """guarda la data del jugador en un archivo .json.

    Args:
        filename (str): nombre del archivo donde se va a guardar si no existe lo crea
        list (list): lista con lo que se va a guardar
        player_name (str): nombre del jugador
        score (int): puntuacion del jugador
    """
    import json
    player_data = {
        "name": player_name,
        "score": score
    }
    list.append(player_data)
    with open(get_path(filename), 'w', encoding="utf-8") as file:
        json.dump(list, file, indent= 4)

def load_data(filename: str)-> dict:
    """carga un archivo .json en un diccionario.

    Args:
        filename (str): nombre del archivo .json

    Returns:
        dict: diccionario con el contenido del archivo .json
    """
    import json
    try:
        with open(get_path(filename), 'r', encoding="utf-8") as file:
            player_data = json.load(file)
    except:
        player_data = {}
    return player_data

def swap_lista(lista: list, i: int, j: int)->None:
    """cambia de lugar algo dentro de una lista.

    Args:
        lista (list): lista
        i (int): elemento i
        j (int): elemento j
    """
    aux = lista[i]
    lista[i] = lista[j]
    lista[j] = aux

def sort_players(lista: list)->None:
    """ordena a los jugadores de mayor a menor, por puntuacion, y si son iguales por orden alfabetico.

    Args:
        lista (list): lista a ordenar

    Raises:
        TypeError: no es una lista
    """
    if not isinstance(lista, list):
        raise TypeError("Eso no es una lista")
    tam = len(lista)
    for i in range(tam - 1):
        for j in range(i + 1, tam):
            if lista[i]["score"] == lista[j]["score"]:
                if lista[i]["name"] > lista[j]["name"]:
                    swap_lista(lista, i, j)
            elif lista[i]["score"] < lista[j]["score"]:
                swap_lista(lista, i, j)