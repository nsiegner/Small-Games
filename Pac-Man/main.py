import pygame
from characters import characters


pygame.init()


SCREEN_WIDTH = 810
SCREEN_HEIGHT = 900


WIDTH = 30

#27x30

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

init_pos = [405,675]

player = characters(pos_x=init_pos[0]-WIDTH/2,pos_y=init_pos[1]-WIDTH/2,type="PacMan")


running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")


    screen.blit(player.image, player.rect)



    pygame.display.flip()

pygame.quit()