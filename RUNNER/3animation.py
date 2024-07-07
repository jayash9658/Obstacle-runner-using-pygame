import pygame
from sys import exit
pygame.init()

#creating a window
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
test_font = pygame.font.Font("Pixeltype.ttf", 50)

test_surface = pygame.Surface((100,200)) #adding a surface
test_surface.fill(("Red"))

sky_surface = pygame.image.load("Sky.png").convert() #adding sky to background
ground_surface = pygame.image.load("ground.png").convert() #adding ground to background
text_surface = test_font.render("My game", False , "Blue") #adding text to the screen


snail_surface = pygame.image.load("snail/snail1.png").convert_alpha() #inserting a snail into the background
snail_x_pos=600

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (325, 20))
    snail_x_pos+=-3 #animation of the snail
    if snail_x_pos < -100:
        snail_x_pos = 900
    screen.blit(snail_surface, (snail_x_pos,265))


    pygame.display.update()
    clock.tick(60)




