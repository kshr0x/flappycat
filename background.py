import pygame

class Background:
    def __init__(self, image_path):
        self.image = pygame.image.load(image_path)
        self.width, self.height = self.image.get_size()
        self.positions = [0, self.width]

    def update(self, velocity):
        self.positions = [(pos - velocity) % (2 * self.width) - self.width for pos in self.positions]

    def draw(self, screen):
        for pos in self.positions:
            screen.blit(self.image, (pos, 0))
