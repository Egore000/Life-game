import pygame
import sys
import time 
import config as cfg
import random
from tools import Screen, Cell, Surface

# инициализация pygame
pygame.init()

screen = pygame.display.set_mode((Screen.WIDTH, Screen.HEIGHT))

# создание поверхности, заполненной "мёртвыми" клетками
cells = {}
for x in range(Surface.X_MIN, Surface.X_MAX, Cell.SIZE):
    for y in range(Surface.Y_MIN, Surface.Y_MAX, Cell.SIZE):
        cells[(x, y)] = Cell(x, y, 0, cells)

flag = False
running = False
while True:
    if not running:
        for event in pygame.event.get():

            # условие выхода из игры
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # отслеживание нажатия при рисовании
            if event.type == pygame.MOUSEBUTTONDOWN:
                flag = True

            # рисование
            if flag:
                x, y = pygame.mouse.get_pos()
                x = x // Cell.SIZE * Cell.SIZE
                y = y // Cell.SIZE * Cell.SIZE
                if Surface.X_MIN <= x <= Surface.X_MAX and Surface.Y_MIN <= y <= Surface.Y_MAX:
                    cells[(x, y)].status = 1
                    cells[(x, y)].color = Cell.COLOR[random.choice(Cell.ALIVE)]
            
            if event.type == pygame.MOUSEBUTTONUP:
                flag = False

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                running = True
        
    else:
        for event in pygame.event.get():
            # Пауза
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                running = False
                
        alive = 0
        cells, changes = Cell.life(cells)
    
        for cell in cells.values():
            alive += cell.status

            pygame.draw.rect(screen, cell.color, cell.body)
        
        time.sleep(1/cfg.FPS)
        pygame.display.update()

        # условия окончания игры
        if not alive or not changes:
            running = False
            print('finish!')

    screen.fill(Screen.COLOR)     
    for cell in cells.values():
        pygame.draw.rect(screen, cell.color, cell.body)
    
    pygame.display.flip()