import sys
import pygame
import pygame.freetype
from pygame.sprite import Sprite
from enum import Enum
from pygame.rect import Rect


# Window Size, Logo & Game Name
game_title = "Lieyapath"
game_image = "Dragon_Head.gif"
game_window_width = 640
game_window_height = 480


# Game Backgrounds
bg1 = pygame.image.load("Background 1.jpg")

# Font Colours
WHITE = (255, 255, 255)
BLACK = (000, 000, 000)
RED = (255, 000, 000)
GREEN = (000, 255, 000)
BLUE = (000, 000, 255)
BROWN = (101, 67, 33)

# Clock
clock = pygame.time.Clock()


def load_image(image: str):
    image = pygame.image.load(image)
    return image


def draw_text(text: str, font_size: int, font_colour: tuple):

    font = pygame.freetype.Font("ARCADECLASSIC.TTF", font_size)
    font_obj, _ = font.render(text, fgcolor=font_colour)
    return font_obj.convert_alpha()


class App:
    @ staticmethod
    def start_up():
        # Game icon & Name
        pygame.display.set_caption(game_title)
        icon = pygame.image.load(game_image)
        pygame.display.set_icon(icon)

        # Window Size
        window = pygame.display.set_mode((game_window_width, game_window_height))
        return window


class Button(Sprite):

    def __init__(self, center_pos: tuple, text: str, font_size: int, colour: tuple, action):
        super().__init__()
        self.mouse_over = False

        text_not_clicked = draw_text(text, font_size, colour)

        text_clicked = draw_text(text, font_size, WHITE)

        self.texts = [text_not_clicked, text_clicked]
        self.positions = [
            text_not_clicked.get_rect(center=center_pos),
            text_clicked.get_rect(center=center_pos)]
        self.action = action

    @property
    def text(self):
        return self.texts[1] if self.mouse_over else self.texts[0]

    @property
    def position(self):
        return self.positions[1] if self.mouse_over else self.positions[0]

    def update(self, mouse_pos, mouse_pressed):
        if self.position.collidepoint(mouse_pos):
            self.mouse_over = True
            if mouse_pressed:
                return self.action
        else:
            self.mouse_over = False

    def draw(self, surface):
        surface.blit(self.text, self.position)


class UserInput:
    def __init__(self, screen, x_pos, y_pos, width, height, colour):
        self.screen = screen
        self.rect_size = pygame.Rect(x_pos, y_pos, width, height)
        self.border_colour = colour
        pygame.draw.rect(self.screen, self.border_colour, self.rect_size, 2)


class GameStates(Enum):
    QUIT = -1
    TITLE = 0
    START = 2
    LOAD = 3
    NAME = 4


# Main Loop
def main():
    pygame.init()
    # Game State
    Game_states = GameStates.TITLE
    while True:
        if Game_states == GameStates.TITLE:
            Game_states = title_screen(App.start_up())

        if Game_states == GameStates.START:
            Game_states = start_screen(App.start_up())

        if Game_states == GameStates.LOAD:
            Game_states = load_screen(App.start_up())

        if Game_states == GameStates.QUIT:
            pygame.quit()
            sys.exit()
        clock.tick(60)


def title_screen(screen):

    start_btn = Button(
        (300, 200),
        "Start",
        30,
        BLACK,
        action=GameStates.START
    )

    load_btn = Button(
        (300, 240),
        "Load",
        30,
        BLACK,
        action=GameStates.LOAD
    )

    quit_btn = Button(
        (300, 280),
        "Quit",
        30,
        BLACK,
        action=GameStates.QUIT
    )
    buttons = [start_btn, load_btn, quit_btn]

    while True:
        mouse_pressed = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_pressed = True
        screen.blit(bg1, (0, 0))

        for button in buttons:
            ui_action = button.update(pygame.mouse.get_pos(), mouse_pressed)
            if ui_action is not None:
                return ui_action
            button.draw(screen)

        pygame.display.flip()


def start_screen(screen):

    user_text = ""

    OK_btn = Button(
        (300, 280),
        "OK",
        30,
        BLACK,
        action=GameStates.NAME
    )

    buttons = [OK_btn]

    while True:
        mouse_pressed = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_pressed = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_text += user_text[0:-1]
                else:
                    user_text += event.unicode
            return mouse_pressed
        screen.blit(bg1, (0, 0))

        for button in buttons:
            ui_action = button.update(pygame.mouse.get_pos(), mouse_pressed)
            if ui_action is not None:
                return ui_action
            button.draw(screen)

        pygame.display.flip()


def load_screen(screen):
    user_text = ""

    OK_btn = Button(
        (300, 280),
        "OK",
        30,
        BLACK,
        action=GameStates.NAME
    )

    buttons = [OK_btn]

    while True:
        mouse_pressed = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_pressed = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_text += user_text[0:-1]
                else:
                    user_text += event.unicode
            return mouse_pressed
        screen.blit(bg1, (0, 0))

        for button in buttons:
            ui_action = button.update(pygame.mouse.get_pos(), mouse_pressed)
            if ui_action is not None:
                return ui_action
            button.draw(screen)

        pygame.display.flip()


main()
