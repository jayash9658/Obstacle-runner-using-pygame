import pygame
from random import randint
from sys import exit
pygame.init()

#display score
def display_score():
    current_time = pygame.time.get_ticks() - start_time
    score_surf = test_font.render(f"Score:{int(current_time/250)}",False,(64,64,64))
    score_rect = score_surf.get_rect(center = (400,43))
    screen.blit(score_surf,score_rect)
    return current_time

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            if obstacle_rect.bottom == 300: screen.blit(snail_surface,obstacle_rect)
            else: screen.blit(fly_surf, obstacle_rect)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

        return obstacle_list
    else: return []

def collisions(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect): return False
    return True
#creating a window
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
test_font = pygame.font.Font("Pixeltype.ttf", 50)
game_active = False
start_time = 0
score = 0


sky_surface = pygame.image.load("Sky.png").convert() #adding sky to background
ground_surface = pygame.image.load("ground.png").convert() #adding ground to background

# text_surface = test_font.render("My game", False , "Blue") #adding text to the screen

#obstacles
snail_surface = pygame.image.load("snail/snail1.png").convert_alpha() #inserting a snail into the background
fly_surf = pygame.image.load("fly1.png").convert_alpha()
# snail_rect = snail_surface.get_rect(midbottom=(600,300))
# snail_x_pos=600
obstacle_rect_list = []



player_surf = pygame.image.load("player_walk_1.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))

# score_text = test_font.render("Score:", False, "white" ) #adding text using rectangles
# score_rect = score_text.get_rect(center = (100,35))

player_gravity = 0

player_stand = pygame.image.load("player_stand.png").convert_alpha()
player_stand = pygame.transform.scale2x(player_stand)
player_stand_rect = player_stand.get_rect(center = (400,200))

title_start = test_font.render("RUNNER",False, (111,196,169))
title_rect = title_start.get_rect(center = (400,85))
start_game = test_font.render("Please Click Space To Start",False, (111,196,169))
start_game_rect = start_game.get_rect(center = (400,320))

#timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,1500)

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
                    snail_surface.get_rect(midbottom=(randint(900,1100),300)).left = 800
                    game_active = True
                    start_time = pygame.time.get_ticks()
        if event.type == obstacle_timer and game_active:
            if randint(0,2):
                obstacle_rect_list.append(snail_surface.get_rect(midbottom=(randint(900,1100),300)))
            else:
                obstacle_rect_list.append(fly_surf.get_rect(midbottom=(randint(900, 1100), 210)))

    if game_active:
        screen.blit(sky_surface, (0,0))
        screen.blit(ground_surface, (0, 300))
        # screen.blit(text_surface, (325, 20))
        # pygame.draw.rect(screen,"Light Blue",score_rect)
        # pygame.draw.rect(screen,"Light Blue",score_rect,10)#colouring the background of the text
        # screen.blit(score_text, score_rect) #adding text using rectangles
        score = display_score()


        # snail_rect.x+=-4 #animation of the snail using rectangle
        # if snail_rect.left < -100:  #if you take smail_rect.x it takes any point x
        #     snail_rect.left = 800
        # screen.blit(snail_surface, snail_rect)

        #Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player_surf,player_rect)

        #obstacle_movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)


        #collision with snail   this quits the game if snail collides with player
        game_active = collisions(player_rect, obstacle_rect_list)
        # if snail_surface.get_rect(midbottom=(randint(900,1100),300)).colliderect(player_rect):
        #     game_active = False
    else:
        screen.fill((94,129,162))
        screen.blit(player_stand, player_stand_rect)  #adding start screen in pygame
        obstacle_rect_list.clear()
        player_rect.midbottom  = (80,300)
        player_gravity = 0

        score_message = test_font.render(f'Your Score: {int(score/250)}', False, (111,196,169))
        score_rect = score_message.get_rect(center= (400,330))

        screen.blit(title_start, title_rect)
        if score == 0:
            screen.blit(start_game, start_game_rect)
        else:
            screen.blit(score_message, score_rect)

    pygame.display.update()
    clock.tick(60)
