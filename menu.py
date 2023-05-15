import sys
import random
import pygame



pygame.init()
clk = pygame.time.Clock()

w = 1280
h = 960

screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("retro")

bg = pygame.Color('black')
white = (255, 255, 255)

font = pygame.font.SysFont('arial', 100)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                with open("Snake.py", "r") as rnf:
                    exec(rnf.read())
            if event.key == pygame.K_2:
                with open("Pong.py", "r") as rnf:
                    exec(rnf.read())
            if event.key == pygame.K_3:
                with open("minesweeper.py", "r") as rnf:
                    exec(rnf.read())
    text = font.render(f'RETRO', False, white)
    text2 = font.render(f'1)SNAKE\n2)PONG\n3)MINESWEEPER', False, white)
    screen.fill(bg)
    screen.blit(text, (300, 10))
    screen.blit(text2, (300, 200))
    pygame.display.update()