import pygame
import sys
import time 

# инициализация pygame
pygame.init()

class Screen:
    WIDTH = 640
    HEIGHT = 480
    COLOR = (0, 0, 0)

class Cell:
    SIZE = 10
    COLOR = {
        0: Screen.COLOR,
        1: (255, 255, 255),
    }
    def __init__(self, x, y, status, cells):
        self.x = (x // Cell.SIZE) * Cell.SIZE
        self.y = (y // Cell.SIZE) * Cell.SIZE
        self.status = status
        self.color = Cell.COLOR[status]
        self.body = pygame.Rect(self.x, self.y, Cell.SIZE, Cell.SIZE)
        self.neighbours_coords = [
            (self.x - Cell.SIZE, self.y + Cell.SIZE), 
            (self.x - Cell.SIZE, self.y),
            (self.x - Cell.SIZE, self.y - Cell.SIZE),
            (self.x, self.y + Cell.SIZE),
            (self.x, self.y - Cell.SIZE),
            (self.x + Cell.SIZE, self.y + Cell.SIZE),
            (self.x + Cell.SIZE, self.y),
            (self.x + Cell.SIZE, self.y - Cell.SIZE)
            ]
        self.neighbours = self.count_neigbours(cells)

    def count_neigbours(self, cells):
        count = 0
        for cell in cells.keys():
            if cell in self.neighbours_coords and \
                cells[cell].status == 1:
                count += 1
        return count

def life(cells):
    for cell in cells.values():
        if cell.status == 0 and cell.neighbours == 3:
            cell.status = 1
            cell.color = Cell.COLOR[1]
        elif cell.status and cell.neighbours in (2, 3):
            pass
        elif cell.status and (cell.neighbours not in (2, 3)):
            cell.status = 0
            cell.color = Cell.COLOR[0]
    return cells

screen = pygame.display.set_mode((Screen.WIDTH, Screen.HEIGHT))

cells = {}
for x in range(0, Screen.WIDTH, Cell.SIZE):
    for y in range(0, Screen.HEIGHT, Cell.SIZE):
        cells[(x, y)] = Cell(x, y, 0, cells)

flag = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            flag = True

        if flag:
            x, y = pygame.mouse.get_pos()
            x = x // Cell.SIZE * Cell.SIZE
            y = y // Cell.SIZE * Cell.SIZE
            cells[(x, y)].status = 1
            cells[(x, y)].color = Cell.COLOR[1]
        
        if event.type == pygame.MOUSEBUTTONUP:
            flag = False

            # print(cells[(x, y)].neighbours)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            running = True
            while running:
                count_alive = 0
                cells = life(cells)
                for cell in cells.values():
                    count_alive += cell.status

                    pygame.draw.rect(screen, cell.color, cell.body)
                    pygame.display.update()

                if count_alive == 0:
                    running = False

                # if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                #     running = False

    screen.fill(Screen.COLOR)     
    for cell in cells.values():
        pygame.draw.rect(screen, cell.color, cell.body)
    
    pygame.display.flip()