import pygame
import sys
from logic import *
from DataBase import *

mas = [[0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0],
       ]
logo = pygame.image.load("images/2048.png")
mas[2][3] = 2
mas[3][1] = 4
colours = {
    0: (130, 130, 130),
    2: (200, 159, 69),
    4: (115, 93, 94),
    8: (126, 166, 57),
    16: (238, 224, 23),
    32: (234, 156, 117),
    64: (58, 58, 128),
    128: (16, 243, 190),
    256: (5, 6, 99),
    512: (176, 38, 0),
    1024: (172, 56, 1),
    2048: (209, 55, 218),
    4096: (255, 0, 0)
}
white = (255, 255, 255)
gray = (130, 130, 130)
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)
orange = (255, 127, 0)

BLOCKS = 4
BLOCK_SIZE = 110
MARGIN = 10
WIDTH = BLOCKS * BLOCK_SIZE + (BLOCKS + 1) * MARGIN
HEIGTH = WIDTH + 110
HEADER = pygame.Rect(0, 0, WIDTH, 110)
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGTH))

total_on_screen = None
max_value = None
control_keys = (
pygame.K_RIGHT, pygame.K_LEFT, pygame.K_DOWN, pygame.K_UP, pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d)
PLAYERS_RECORD = top_score()
insert_db('1qS56g1234332',0)

def results():  # DISPLAYING 3 BEST RESULTS OF PLAYERS FROM DATA BASE
    text_header = pygame.font.SysFont("comicsanms", 28)
    text_res = pygame.font.SysFont("comicsanms", 22)
    header_text = text_header.render("Best Records: ", True, orange)
    screen.blit(header_text, (250, 5))
    for i, v in enumerate(PLAYERS_RECORD):
        if v[0]!="1qS56g1234332":
            result_text = text_res.render(f"{v[0]}-    "
                                          f""
                                          f"{v[1]}", True, orange)
            screen.blit(result_text, (250, (30 + (20 * i))))


def draw_menu():  # CREATION OF PRE GAME MENU INPUT NICKNAME OF THE PLAYER
    font = pygame.font.SysFont("ROG FONTS", 40)
    pressfont = pygame.font.SysFont("ROG FONTS", 22)
    menu_img = pygame.image.load('images/menu.png')
    name = "Your name"
    name_not_exists = True
    while name_not_exists:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if name == "Your name":
                    name = ""
                elif event.unicode.isalpha() or event.unicode.isnumeric():
                    name += event.unicode
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                elif event.key == pygame.K_RETURN:
                    if len(name) > 2 and len(name) < 12:
                        global USERNAME
                        USERNAME = name
                        name_not_exists = False
        screen.blit(menu_img, (0, 0))
        name_text = font.render(name, True, white)
        press_text = pressfont.render("Write your name to start", True, black)
        name_rect = name_text.get_rect()
        name_rect.center = screen.get_rect().center
        # screen.blit(welcome_text, (100,sfd 250))
        screen.blit(name_text, name_rect)
        screen.blit(press_text, (55, 355))
        pygame.display.update()
    screen.fill(black)


def draw_game_over_menu():  # CREATION OF GAME OVER MENU AND ADDING RESULTS TO DATA BASE
    global max_value, mas, total_on_screen
    game_over_img = pygame.image.load('images/gameover.png')
    font = pygame.font.SysFont("ROG FONTS", 24)
    font2 = pygame.font.SysFont("ROG FONTS", 20)
    game_over_text = font.render(f"Best record:{PLAYERS_RECORD[0][1]}", True, white)
    game_space_text = font2.render(f"Press SPACE to restart", True, white)
    if max_value > PLAYERS_RECORD[0][1]:
        player_game_over_text = font.render(f"You ROCK!: {max_value}", True, white)
    else:
        player_game_over_text = font.render(f"Your record:{max_value}", True, white)
    insert_db(USERNAME, max_value)
    restart_game = True
    while restart_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    mas, total_on_screen, max_value = zero_values()
                    restart_game = False
        screen.blit(game_over_img, (0, 0))
        screen.blit(game_over_text, (25, 225))
        screen.blit(player_game_over_text, (25, 275))
        screen.blit(game_space_text, (25, 475))
        pygame.display.update()
    screen.fill(black)


def draw_game(total, max):  # DRAWING THE INTERFACE OF GAME ITSELF SHOWING MAX AND CURENT MAX VALUES
    max = int(max)
    pygame.draw.rect(screen, white, HEADER)
    font = pygame.font.SysFont("comicsanms", 70)
    score_font = pygame.font.SysFont("ROG FONTS", 20)
    total_text = score_font.render(f"Score:{total}", True, orange)
    max_text = score_font.render(f"Max:{max}", True, orange)
    screen.blit(total_text, (20, 25))
    screen.blit(max_text, (20, 55))
    results()
    for row in range(BLOCKS):
        for col in range(BLOCKS):
            value = mas[row][col]
            text = font.render(f'{value}', True, white)
            col_pos = col * BLOCK_SIZE + (col + 1) * MARGIN
            row_pos = row * BLOCK_SIZE + (row + 1) * MARGIN + 110
            pygame.draw.rect(screen, colours[value], (col_pos, row_pos, 110, 110))
            if value != 0:
                font_w, font_h = text.get_size()
                text_x = col_pos + (110 - font_w) / 2
                text_y = row_pos + (110 - font_h) / 2
                screen.blit(text, (text_x, text_y))


def game_algorithm():
    global total_on_screen, max_value, mas
    total_on_screen, max_value = 0, 0
    draw_game(total_on_screen, max_value)
    pygame.display.update()

    while is_zero_in_mas(mas) or can_move(mas):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    mas = move_left(mas)
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    mas = move_right(mas)
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    mas = move_up(mas)
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    mas = move_down(mas)
                if (event.key in control_keys):
                    if is_zero_in_mas(mas):
                        empty = get_empty_list(mas)
                        random.shuffle(empty)
                        rand_number = empty.pop()
                        x, y = get_index_from_number(rand_number)
                        mas = get_2_or_4(mas, x, y)
                    pretty_print(mas)
                    total_on_screen = total(mas)
                    max_value = max_element(mas)
                    max_value = int(max_value)
                    draw_game(total_on_screen, max_value)
                else:
                    continue
        pygame.display.update()


while True:
    pygame.display.set_icon(logo)
    pygame.display.set_caption("2048 GAME")
    PLAYERS_RECORD = top_score()
    draw_menu()
    game_algorithm()
    draw_game_over_menu()
