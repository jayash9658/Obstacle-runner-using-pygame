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

score_text = test_font.render("Score:", False, "white" ) #adding text using rectangles
score_rect = score_text.get_rect(center = (100,35))

player_gravity = 0
game_active = True
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.bottom >= 300:
                    if player_rect.collidepoint(event.pos):
                        player_gravity = -20
            if event.type == pygame.KEYDOWN:
                if player_rect.bottom >= 300:
                    if event.key == pygame.K_SPACE:
                        player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    snail_rect.left = 800
                    game_active = True

    if game_active:
        screen.blit(sky_surface, (0,0))
        screen.blit(ground_surface, (0, 300))
        screen.blit(text_surface, (325, 20))
        pygame.draw.rect(screen,"Light Blue",score_rect)
        pygame.draw.rect(screen,"Light Blue",score_rect,10)#colouring the background of the text
        screen.blit(score_text, score_rect) #adding text using rectangles


        snail_rect.x+=-4 #animation of the snail using rectangle
        if snail_rect.left < -100:  #if you take smail_rect.x it takes any point x
            snail_rect.left = 800
        screen.blit(snail_surface, snail_rect)

        #Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player_surf,player_rect)

        #collision with snail   this quits the game if snail collides with player
        if snail_rect.colliderect(player_rect):
            game_active = False
    else:
        screen.fill("Blue")



    pygame.display.update()
    clock.tick(60)
