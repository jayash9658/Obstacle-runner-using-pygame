import pygame
from sys import exit
pygame.init()


screen = pygame.display.set_mode((800,500))
pygame.display.set_caption("Screen setup")
clock = pygame.time.Clock()


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
    clock.tick(60)
