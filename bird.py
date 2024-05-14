import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

class Bird:
    def __init__(self, image_path, jump_sound_path):
        self.image = pygame.transform.scale(pygame.image.load(image_path), (70, 70))
        self.x = SCREEN_WIDTH // 4
        self.y = SCREEN_HEIGHT // 2
        self.y_velocity = 0
        self.gravity = 0.5
        self.jump_sound = pygame.mixer.Sound(jump_sound_path)
        self.jump_sound.set_volume(0.2)

    def jump(self):
        self.y_velocity = -8
        self.jump_sound.play()

    def update(self):
        self.y_velocity += self.gravity
        self.y += self.y_velocity

    def draw(self, screen):
        angle = 10 if self.y_velocity < 0 else -10
        rotated_bird = pygame.transform.rotate(self.image, angle)
        rotated_bird_rect = rotated_bird.get_rect(center=(self.x + 35, self.y + 35))
        screen.blit(rotated_bird, rotated_bird_rect.topleft)

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
