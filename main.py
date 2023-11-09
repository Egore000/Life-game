import pygame
import sys

# инициализация pygame
pygame.init()

class Screen:
    WIDTH = 640
    HEIGHT = 480
    COLOR = (0, 0, 0)

class Cell:
    SIZE = 10
    COLOR = (255, 255, 255)

    def __init__(self, x, y, status, cells):
        self.x = (x // Cell.SIZE) * Cell.SIZE
        self.y = (y // Cell.SIZE) * Cell.SIZE
        self.status = status
        self.neighbours = self.count_neigbours(cells)
        self.body = pygame.Rect(self.x, self.y, Cell.SIZE, Cell.SIZE)

    def count_neigbours(self, cells):
        # neighbours_x = (self.x - Cell.SIZE, self.x, self.x + Cell.SIZE)
        # neighbours_y = (self.y - Cell.SIZE, self.y, self.y + Cell.SIZE)
        neighbours_coords = [
            (self.x - Cell.SIZE, self.y + Cell.SIZE), 
            (self.x - Cell.SIZE, self.y),
            (self.x - Cell.SIZE, self.y - Cell.SIZE),
            (self.x, self.y + Cell.SIZE),
            (self.x, self.y - Cell.SIZE),
            (self.x + Cell.SIZE, self.y + Cell.SIZE),
            (self.x + Cell.SIZE, self.y),
            (self.x + Cell.SIZE, self.y - Cell.SIZE)
            ]
        count = 0
        for cell in cells:
            if (cell.x, cell.y) in neighbours_coords:
                count += 1
        return count

    def life():
        return

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
            cell = Cell(x, y, 1, cells)
            cells.append(cell)

        # if event.type == pygame.K_ESCAPE:


    screen.fill(Screen.COLOR)     
    for cell in cells:
        pygame.draw.rect(screen, Cell.COLOR, cell.body, 0)
    pygame.display.flip()