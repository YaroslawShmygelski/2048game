import pygame
import sys
from logic import *
from DataBase import *

mas = [[0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0],
       ]

mas[2][3] = 2
mas[3][1] = 4
colours = {
    0: (130, 130, 130),
    2: (200, 159, 69),
    4: (115, 93, 94),
    8: (126, 166, 57),
    16: (238, 255, 6),
    32: (234, 156, 117),
    64: (58, 58, 128),
    128: (16, 243, 190),
    256: (5, 6, 99),
    512: (172, 141, 47),
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

total_on_screen = 0
max_value = 0

PLAYERS_RECORD = top_score()
print(PLAYERS_RECORD)


def results():  # DISPLAYING 3 BEST RESULTS OF PLAYERS FROM DATA BASE
    text_header = pygame.font.SysFont("comicsanms", 28)
    text_res = pygame.font.SysFont("comicsanms", 22)
    header_text = text_header.render("Best Records: ", True, orange)
    screen.blit(header_text, (250, 5))
    for i, v in enumerate(PLAYERS_RECORD):
        result_text = text_res.render(f"{v[0]}-    "
                                      f""
                                      f"{v[1]}", True, orange)
        screen.blit(result_text, (250, (30 + (20 * i))))



def draw_menu():  # CREATION OF PRE GAME MENU INPUT NICKNAME OF THE PLAYER
    font = pygame.font.SysFont("ROG FONTS", 40)
    pressfont = pygame.font.SysFont("ROG FONTS", 22)
    menu_img = pygame.image.load('menu.png')
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
    game_over_img = pygame.image.load('gameover.png')
    font = pygame.font.SysFont("ROG FONTS", 24)
    game_over_text = font.render(f"Best record:{PLAYERS_RECORD[0][1]}", True, white)
    if max_value > PLAYERS_RECORD[0][1]:
        player_game_over_text = font.render(f"You ROCK!: {max_value}", True, white)
    else:
        player_game_over_text = font.render(f"Your record:{max_value}", True, white)
    insert_db(USERNAME, max_value)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
        screen.blit(game_over_img, (0, 0))
        screen.blit(game_over_text, (25, 225))
        screen.blit(player_game_over_text, (25, 275))
        pygame.display.update()


def draw_game(total, max):  # DRAWING THE INTERFACE OF GAME ITSELF SHOWING MAX AND CURENT MAX VALUES
    max=int(max)
    pygame.draw.rect(screen, white, HEADER)
    font = pygame.font.SysFont("comicsanms", 70)
    score_font = pygame.font.SysFont("ROG FONTS", 20)
    score_text = score_font.render(f"Score:{total} Max:{max}", True, orange)
    screen.blit(score_text, (20, 35))
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


draw_menu()
draw_game(total_on_screen, max_value)
pygame.display.update()

while is_zero_in_mas(mas) or can_move(mas):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            sum = 0
            if event.key == pygame.K_LEFT:
                mas = move_left(mas)
            elif event.key == pygame.K_RIGHT:
                mas = move_right(mas)
            elif event.key == pygame.K_UP:
                mas = move_up(mas)
            elif event.key == pygame.K_DOWN:
                mas = move_down(mas)

            # input()
            if is_zero_in_mas(mas):
                empty = get_empty_list(mas)
                random.shuffle(empty)
                rand_number = empty.pop()
                x, y = get_index_from_number(rand_number)
                mas = get_2_or_4(mas, x, y)
            pretty_print(mas)
            total_on_screen = total(mas)
            max_value = max_element(mas)
            max_value=int(max_value)
            draw_game(total_on_screen, max_value)
    pygame.display.update()

draw_game_over_menu()
