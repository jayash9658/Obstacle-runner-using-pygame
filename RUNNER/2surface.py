import pygame
from sys import exit
pygame.init()


screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
test_font = pygame.font.Font("Pixeltype.ttf", 50)

# test_surface = pygame.Surface((100,200)) #adding a surface
# test_surface.fill(("Red"))

sky_surface = pygame.image.load("Sky.png") #adding sky to background
ground_surface = pygame.image.load("ground.png") #adding ground to background
text_surface = test_font.render("My game", False , "Blue") #adding text to the screen

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (325, 20))

    pygame.display.update()
    clock.tick(60)
