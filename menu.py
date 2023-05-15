import sys
import random
import pygame
'''
In order to run first install pygame, instructions can be found at https://pypi.org/project/pygame/

then run the menu.py file

'''

pygame.init()
clk = pygame.time.Clock()

w = 1280
h = 960

screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("retro")

bg = pygame.Color('black')
white = (255, 255, 255)

font = pygame.font.SysFont('arial', 50)

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
    
    text_rect = text.get_rect(center=(w // 2, h // 4))
    text2_rect = text2.get_rect(center=(w // 2, h // 2))
    
    screen.fill(bg)
    screen.blit(text, text_rect)
    screen.blit(text2, text2_rect)
    
    pygame.display.update()
    clk.tick(60)
