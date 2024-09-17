import pygame
import sys

pygame.init()

win_width, win_height = 800, 600
window = pygame.display.set_mode((win_width, win_height))

color = (0, 128, 255)

rect_width, rect_height = 50, 50
rect_x, rect_y = 100, 100
rect_speed_x, rect_speed_y = 5, 5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    rect_x += rect_speed_x
    rect_y += rect_speed_y

    # Перевірка виходу за межі вікна
    if rect_x < 0:
        rect_x = 0
        rect_speed_x = -rect_speed_x
    elif rect_x + rect_width > win_width:
        rect_x = win_width - rect_width
        rect_speed_x = -rect_speed_x

    if rect_y < 0:
        rect_y = 0
        rect_speed_y = -rect_speed_y
    elif rect_y + rect_height > win_height:
        rect_y = win_height - rect_height
        rect_speed_y = -rect_speed_y

    window.fill((0, 0, 0))

    pygame.draw.rect(window, color, (rect_x, rect_y, rect_width, rect_height))

    pygame.display.flip()

    pygame.time.delay(30)
