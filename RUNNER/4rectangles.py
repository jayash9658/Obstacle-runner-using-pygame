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
snail_rect = snail_surface.get_rect(midbottom=(600,300))
snail_x_pos=600

player_surf = pygame.image.load("player_walk_1.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (325, 20))
    snail_rect.left+=-3 #animation of the snail using rectangle
    if snail_rect.left < -100:  #if you take smail_rect.x it takes any point x
        snail_rect.left = 800
    screen.blit(snail_surface, snail_rect)
    screen.blit(player_surf,player_rect)

    pygame.display.update()
    clock.tick(60)
