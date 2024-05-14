import pygame
# Определяем цвета

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 128, 0)

# Задаем параметры экрана
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Вспомогательные функции
def draw_gradient_rect(screen, rect, color1, color2):
    x, y, w, h = rect
    for i in range(h):
        ratio = i / h
        color = tuple(int(color1[j] * (1 - ratio) + color2[j] * ratio) for j in range(3))
        pygame.draw.line(screen, color, (x, y + i), (x + w, y + i))
