import pygame
import os
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLACK
from background import Background
from bird import Bird
from pipe import Pipe
from scoremanager import ScoreManager

class Game:
    def __init__(self, screen, resource_path):
        self.screen = screen
        self.resource_path = resource_path
        self.background = Background(self.resource_path('assets/background.png'))
        self.bird = Bird(self.resource_path('assets/bird.png'), self.resource_path('assets/jump.wav'))
        self.pipe = Pipe()
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('comicsansms', 35)
        self.point_sound = pygame.mixer.Sound(self.resource_path('assets/point.wav'))
        self.point_sound.set_volume(2)
        pygame.mixer.music.load(self.resource_path('assets/background_music.wav'))
        pygame.mixer.music.set_volume(0.05)
        pygame.mixer.music.play(-1)
        self.FPS = 60
        self.score = 0
        self.high_score_manager = ScoreManager()
        self.high_score = self.high_score_manager.load_high_score()
        self.game_over = False

    def display_message(self, message, color):
        text = self.font.render(message, True, color)
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.screen.blit(text, text_rect)
        pygame.display.update()

    def check_collision(self):
        bird_rect = self.bird.get_rect()
        if bird_rect.colliderect(self.pipe.get_top_rect()) or bird_rect.colliderect(self.pipe.get_bottom_rect()):
            return True
        if self.bird.y > SCREEN_HEIGHT or self.bird.y < 0:
            return True
        return False

    def run(self):
        running = True
        passed_pipe = False
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and not self.game_over:
                        self.bird.jump()
                    if event.key == pygame.K_r and self.game_over:
                        self.__init__(self.screen, self.resource_path)  # перезапуск игры
                    if event.key == pygame.K_q:
                        running = False

            if not self.game_over:
                self.bird.update()
                if self.pipe.update():
                    passed_pipe = False

                self.background.update(self.pipe.velocity)

                if self.pipe.x + self.pipe.width < self.bird.x and not passed_pipe:
                    self.score += 1
                    passed_pipe = True
                    self.point_sound.play()
                    if self.score % 10 == 0:
                        self.pipe.velocity += 0.1
                        self.bird.gravity += 0.01

                if self.check_collision():
                    self.game_over = True
                    if self.score > self.high_score:
                        self.high_score = self.score
                        self.high_score_manager.save_high_score(self.high_score)

                self.screen.fill(WHITE)
                self.background.draw(self.screen)
                self.bird.draw(self.screen)
                self.pipe.draw(self.screen)
                score_text = self.font.render("Score: " + str(self.score), True, BLACK)
                high_score_text = self.font.render("High Score: " + str(self.high_score), True, BLACK)
                self.screen.blit(score_text, [10, 10])
                self.screen.blit(high_score_text, [10, 50])
                pygame.display.flip()
                self.clock.tick(self.FPS)
            else:
                self.display_message("Press 'R' to restart", BLACK)
