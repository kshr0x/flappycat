import pygame
import random
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, draw_gradient_rect, GREEN, DARK_GREEN

class Pipe:
    def __init__(self, width=80, gap=200, velocity=3):
        self.width = width
        self.gap = gap
        self.x = SCREEN_WIDTH
        self.height = random.randint(150, 450)
        self.velocity = velocity

    def update(self):
        self.x -= self.velocity
        if self.x < -self.width:
            self.x = SCREEN_WIDTH
            self.height = random.randint(150, 450)
            return True
        return False

    def draw(self, screen):
        draw_gradient_rect(screen, (self.x, 0, self.width, self.height), GREEN, DARK_GREEN)
        pygame.draw.rect(screen, DARK_GREEN, (self.x - 10, self.height - 20, self.width + 20, 20))
        bottom_pipe_top = self.height + self.gap
        draw_gradient_rect(screen, (self.x, bottom_pipe_top, self.width, SCREEN_HEIGHT - bottom_pipe_top), DARK_GREEN, GREEN)
        pygame.draw.rect(screen, DARK_GREEN, (self.x - 10, bottom_pipe_top, self.width + 20, 20))

    def get_top_rect(self):
        return pygame.Rect(self.x, 0, self.width, self.height)

    def get_bottom_rect(self):
        return pygame.Rect(self.x, self.height + self.gap, self.width, SCREEN_HEIGHT - (self.height + self.gap))
