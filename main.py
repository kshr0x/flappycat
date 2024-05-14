import os
import sys
import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT
from menu import Menu
from game import Game

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('FlappyCat')
    menu = Menu(screen, resource_path)
    game = Game(screen, resource_path)
    menu.run()
    game.run()
    pygame.quit()

if __name__ == "__main__":
    main()
