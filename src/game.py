import pygame
from random import randint
from config import *
from colisiones import *
from functions import *


def game_loop(screen):
    clock = pygame.time.Clock()

    # background
    background = pygame.transform.scale(pygame.image.load("./src/assets/street.jpg"), SIZE_SCREEN)

    # car
    enemy_car = pygame.transform.scale(pygame.image.load("./src/assets/car.png"), CAR_SIZE)

    # coin
    image_coin = pygame.transform.scale(pygame.image.load("./src/assets/coin.png"), (COIN_SIZE, COIN_SIZE))

    # slow_coin
    image_slow_coin = pygame.transform.scale(pygame.image.load("./src/assets/slow_coin.png"),
                                            (COIN_SIZE, COIN_SIZE))

    # truck
    enemy_truck = pygame.transform.scale(pygame.image.load("./src/assets/truck.png"), 
                                        TRUCK_SIZE)

    # motorcycle
    enemy_motorcycle = pygame.transform.scale(pygame.image.load("./src/assets/motorcycle.png"), 
                                            MOTORCYCLE_SIZE)

    # player
    image_player = pygame.transform.scale(pygame.image.load("./src/assets/frog.png"), 
                                        (BLOCK_WIDTH , BLOCK_HEIGHT))

    # cargo audio
    try:
        coin_sound = pygame.mixer.Sound("./src/assets/mario-coin.mp3")
        coin_sound.set_volume(0.3)
        pum_sound = pygame.mixer.Sound("./src/assets/PUM.mp3")
        pum_sound.set_volume(0.3)
        dead_sound = pygame.mixer.Sound("./src/assets/sad.mp3")
        dead_sound.set_volume(0.3)
    except:
        None
    playing_music = True

    # frog
    block = create_block(BLOCK_LEFT, BLOCK_TOP, width=BLOCK_WIDTH, 
                        height=BLOCK_HEIGHT,colour=GREEN, img= image_player)

    # autos
    cars = []
    load_enemies(cars, number_of_cars, CAR_SIZE, RED, enemy_car)

    # motos
    motorcycles = []
    load_enemies(motorcycles, number_of_motorcylces, MOTORCYCLE_SIZE, MAGENTA, enemy_motorcycle)

    # camiones
    trucks = []
    load_enemies(trucks, number_of_trucks, TRUCK_SIZE, LIGHT_BLUE, enemy_truck)

    from config import move_down, move_left, move_right, move_up, flag_slow_coin

    # monedas
    coins = []

    # monedas especiales
    slow_coins = []

    # evento personalizado
    EVENT_NEW_COIN = pygame.USEREVENT + 1

    pygame.time.set_timer(EVENT_NEW_COIN, 2500)

    EVENT_NEW_SLOW_COIN = pygame.USEREVENT + 2

    pygame.time.set_timer(EVENT_NEW_SLOW_COIN, 5000)
    # seteo fuente
    font = pygame.font.SysFont(None, 48)

    score = 0

    # texto monedas
    text_score = font.render(f"Score: {score}", True, BLACK)
    rect_text_score = text_score.get_rect()
    rect_text_score.midright = (WIDTH, (0 + rect_text_score.height))

    hearts = 5

    # texto vida
    text_life = font.render(f"hearts: {hearts}", True, BLACK)
    rect_text_life = text_life.get_rect()
    rect_text_life.midleft = (0, 30)

    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish()
            if event.type == EVENT_NEW_COIN:
                    handler_new_coin(coins, WIDTH, (HEIGHT - BLOCK_HEIGHT), COIN_SIZE, YELLOW, image_coin)
                    print("nueva moneda")
            if event.type == EVENT_NEW_SLOW_COIN:
                    handler_new_coin(slow_coins, WIDTH, (HEIGHT - BLOCK_HEIGHT), COIN_SIZE, BLUE, image_slow_coin)
                    print("MONEDA ESPECIAL")
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    move_right = True
                if event.key == pygame.K_a:
                    move_left = True
                if event.key == pygame.K_w:
                    move_up = True
                if event.key == pygame.K_s:
                    move_down = True
                if event.key == pygame.K_m:
                    if playing_music:
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.unpause()
                    playing_music = not playing_music
                if event.key == pygame.K_p:
                    show_text(screen, "PAUSA", font, CENTER_SCREEN, MAGENTA)
                    pygame.display.flip()
                    pygame.mixer.music.pause()
                    pause(pygame.K_p)
                    if playing_music:
                        pygame.mixer.music.unpause()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    move_right = False
                if event.key == pygame.K_a:
                    move_left = False
                if event.key == pygame.K_w:
                    move_up = False
                if event.key == pygame.K_s:
                    move_down = False


        if move_right and block["rect"].right <= (WIDTH - SPEED):
            # derecha
            block["rect"].left += SPEED

        if move_left and block["rect"].left >= SPEED:
            # izquierda
            block["rect"].left -= SPEED

        if move_up and block["rect"].top >= (0 + SPEED):
            # arriba
            block["rect"].top -= SPEED

        if move_down and block["rect"].bottom <= HEIGHT - SPEED:
            # abajo
            block["rect"].top += SPEED

            # muevo los carros
        if not flag_slow_coin:
            for car in cars:
                car["rect"].move_ip(2.5, 0)
                if car["rect"].right > WIDTH:
                    car["rect"].right = 0
            for motorcycle in motorcycles:
                motorcycle["rect"].move_ip(4, 0)
                if motorcycle["rect"].right > WIDTH:
                    motorcycle["rect"].right = 0
            for truck in trucks:
                truck["rect"].move_ip(-1, 0)
                if truck["rect"].right < 0:
                    truck["rect"].right = WIDTH
        else:
            for car in cars:
                car["rect"].move_ip(1.5, 0)
                if car["rect"].right > WIDTH:
                    car["rect"].right = 0
            for motorcycle in motorcycles:
                motorcycle["rect"].move_ip(2, 0)
                if motorcycle["rect"].right > WIDTH:
                    motorcycle["rect"].right = 0
            for truck in trucks:
                truck["rect"].move_ip(-1, 0)
                if truck["rect"].right < 0:
                    truck["rect"].right = WIDTH
            
        for coin in coins:
                if detect_collision(coin["rect"], block["rect"]):
                    coins.remove(coin)
                    score+=1
                    text_score = font.render(f"Score: {score}", True, BLACK)
                    rect_text_score = text_score.get_rect()
                    rect_text_score.midright = (WIDTH, (0 + rect_text_score.height))
                    coin_sound.play()

        for coin in slow_coins:
                if detect_collision(coin["rect"], block["rect"]):
                    slow_coins.remove(coin)
                    flag_slow_coin = True
                    time_slow_coin = 100
                    score+=1
                    text_score = font.render(f"Score: {score}", True, BLACK)
                    rect_text_score = text_score.get_rect()
                    rect_text_score.midright = (WIDTH, (0 + rect_text_score.height))
                    coin_sound.play()
                if flag_slow_coin:
                    if time_slow_coin > 0:
                        time_slow_coin -= 1
                        print(time_slow_coin)
                    elif time_slow_coin == 0:
                        flag_slow_coin = False

        for motorcycle in motorcycles[:]:
            if detect_collision(motorcycle["rect"], block["rect"]):
                collision = True
                if collision:
                    print("Chocaron")
                    motorcycles.remove(motorcycle)
                    hearts -= 1
                    text_life = font.render(f"hearts: {hearts}", True, BLACK)
                    rect_text_life = text_life.get_rect()
                    rect_text_life.midleft = (0, 30)
                    pum_sound.play()
                if len(motorcycles) < number_of_motorcylces:
                    load_enemies(motorcycles, 1, MOTORCYCLE_SIZE, MAGENTA, enemy_motorcycle)
            else:
                collision = False
        
        for truck in trucks[:]:
            if detect_collision(truck["rect"], block["rect"]):
                collision = True
                if collision:
                    print("Chocaron")
                    trucks.remove(truck)
                    hearts -= 1
                    text_life = font.render(f"hearts: {hearts}", True, BLACK)
                    rect_text_life = text_life.get_rect()
                    rect_text_life.midleft = (0, 30)
                    pum_sound.play()
                if len(trucks) < number_of_trucks:
                    load_enemies(trucks, 1, TRUCK_SIZE, LIGHT_BLUE, enemy_truck)
            else:
                collision = False

        for car in cars[:]:
            if detect_collision(car["rect"], block["rect"]):
                collision = True
                if collision:
                    print("Chocaron")
                    cars.remove(car)
                    hearts -= 1
                    text_life = font.render(f"hearts: {hearts}", True, BLACK)
                    rect_text_life = text_life.get_rect()
                    rect_text_life.midleft = (0, 30)
                    pum_sound.play()
                if len(cars) < number_of_cars:
                    load_enemies(cars, 1, CAR_SIZE, RED, enemy_car)
            else:
                collision = False
            
        if hearts == 0:
            move_down = False
            move_right = False
            move_left = False
            move_up = False
            dead_sound.play()
            running = False
    
        screen.blit(background, background.get_rect())

        screen.blit(block["img"], block["rect"])
        for coin in coins:
            screen.blit(coin["img"], coin["rect"])
        for coin in slow_coins:
            screen.blit(coin["img"], coin["rect"])
        for car in cars:
            screen.blit(car["img"], car["rect"])
        for motorcycle in motorcycles:
            screen.blit(motorcycle["img"], motorcycle["rect"])
        for truck in trucks:
            screen.blit(truck["img"], truck["rect"])
        
        screen.blit(text_life, rect_text_life)
        screen.blit(text_score, rect_text_score)
        pygame.display.flip()
    
    from game_over import game_over_screen
    from initial_menu import scores
    game_over_screen(screen, score, scores)
