import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLACK
from background import Background

class MenuBird:
    def __init__(self, image_path):
        self.image = pygame.transform.scale(pygame.image.load(image_path), (150, 150))
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 1.6 + 100
        self.angle = 0
        self.angle_direction = 1

    def update(self):
        self.angle += self.angle_direction * 0.03
        if abs(self.angle) > 10:
            self.angle_direction *= -1

    def draw(self, screen):
        rotated_bird = pygame.transform.rotate(self.image, self.angle)
        rotated_bird_rect = rotated_bird.get_rect(center=(self.x, self.y))
        screen.blit(rotated_bird, rotated_bird_rect.topleft)

class Menu:
    def __init__(self, screen, resource_path):
        self.screen = screen
        self.resource_path = resource_path
        self.font_large = pygame.font.SysFont('comicsansms', 50)
        self.font_small = pygame.font.SysFont('comicsansms', 35)
        self.background = Background(self.resource_path('assets/background.png'))
        self.menu_bird = MenuBird(self.resource_path('assets/bird.png'))
        pygame.mixer.music.load(self.resource_path('assets/background_music.wav'))
        pygame.mixer.music.set_volume(0.05)
        pygame.mixer.music.play(-1)

    def display_message(self, message, font, y_offset, color):
        text = font.render(message, True, color)
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + y_offset))
        self.screen.blit(text, text_rect)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        running = False

            self.screen.fill(WHITE)
            self.background.update(0.05)
            self.background.draw(self.screen)
            self.display_message("FlappyCat", self.font_large, -50, BLACK)
            self.display_message("Press 'R' to Start", self.font_small, 50, BLACK)
            self.menu_bird.update()
            self.menu_bird.draw(self.screen)
            pygame.display.flip()
