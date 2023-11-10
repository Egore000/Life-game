import pygame
import config as cfg 
import random

class Screen:
    WIDTH = cfg.WIDTH
    HEIGHT = cfg.HEIGHT
    COLOR = cfg.BACKGROUNG_COLOR

class Cell:
    SIZE = cfg.CELL_SIZE
    COLOR = cfg.CELL_COLOR
    ALIVE = list(cfg.CELL_COLOR.keys())[1:]

    def __init__(self, x, y, status, cells):
        self.x = (x // Cell.SIZE) * Cell.SIZE
        self.y = (y // Cell.SIZE) * Cell.SIZE
        self.status = status
        self.color = Cell.COLOR[status]
        self.body = pygame.Rect(self.x, self.y, Cell.SIZE, Cell.SIZE)

    def get_neigbours(self, cells):
        nb = []
        for x in range(self.x - Cell.SIZE, self.x + 2*Cell.SIZE, Cell.SIZE):
            for y in range(self.y - Cell.SIZE, self.y + 2*Cell.SIZE, Cell.SIZE):
                try:
                    if x == self.x and y == self.y:
                        continue

                    if Surface.X_MIN <= x <= Surface.X_MAX and \
                        Surface.Y_MIN <= y <= Surface.Y_MAX and \
                        cells[(x, y)].status == 1:
                            nb.append(cells[(x, y)])
                except:
                    pass
                
        return nb
    
    def life(cells):
        changes = 0

        for cell in cells.values():
            neighbours = len(cell.get_neigbours(cells))
            if cell.status == 0 and neighbours == 3:
                changes += 1
                cell.status = 1
                cell.color = Cell.COLOR[random.choice(Cell.ALIVE)]
            elif cell.status and neighbours in (2, 3):
                pass
            elif cell.status and (neighbours not in (2, 3)):
                changes += 1
                cell.status = 0
                cell.color = Cell.COLOR[0]

        return cells, changes
        
class Surface:
    X_MIN = cfg.X_MIN
    X_MAX = cfg.X_MAX
    Y_MIN = cfg.Y_MIN
    Y_MAX = cfg.Y_MAX

