import pygame
import sys
import time 
import config as cfg
from tools import Screen, Cell, Surface

# инициализация pygame
pygame.init()

screen = pygame.display.set_mode((Screen.WIDTH, Screen.HEIGHT))

cells = {}
for x in range(Surface.X_MIN, Surface.X_MAX, Cell.SIZE):
    for y in range(Surface.Y_MIN, Surface.Y_MAX, Cell.SIZE):
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
            if Surface.X_MIN <= x <= Surface.X_MAX and Surface.Y_MIN <= y <= Surface.Y_MAX:
                cells[(x, y)].status = 1
                cells[(x, y)].color = Cell.COLOR[1]
        
        if event.type == pygame.MOUSEBUTTONUP:
            flag = False

            # print(cells[(x, y)].neighbours)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            running = True
            while running:
                count_alive = 0
                cells, cells_prev = Cell.life(cells)
              
                for cell in cells.values():
                    count_alive += cell.status

                    pygame.draw.rect(screen, cell.color, cell.body)
                
                time.sleep(1/cfg.FPS)
                pygame.display.update()

                if count_alive == 0:
                    #  or cells == cells_prev:
                    running = False

    screen.fill(Screen.COLOR)     
    for cell in cells.values():
        pygame.draw.rect(screen, cell.color, cell.body)
    
    pygame.display.flip()