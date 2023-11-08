import pygame
import sys

# инициализация pygame
pygame.init()

# def normalize(x, y):
#     x //= Screen.WIDTH * Cell.SIZE
#     y //= Screen.HEIGHT * Cell.SIZE
#     return x, y 

class Screen:
    WIDTH = 640
    HEIGHT = 480
    COLOR = (0, 0, 0)

class Cell:
    SIZE = 10
    COLOR = (255, 255, 255)

    def __init__(self, x, y, status, neighbours):
        self.x = x
        self.y = y
        self.status = status
        self.neighbours = neighbours
        self.body = pygame.Rect(x, y, Cell.SIZE, Cell.SIZE)

screen = pygame.display.set_mode((Screen.WIDTH, Screen.HEIGHT))

running = True
cells = []
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONUP:
            x, y = pygame.mouse.get_pos()
            # x, y = normalize(x, y)
            cells.append(Cell(x, y, 1, 0))

    screen.fill(Screen.COLOR)     
    for cell in cells:
        pygame.draw.rect(screen, Cell.COLOR, cell.body, 0)
    pygame.display.flip()