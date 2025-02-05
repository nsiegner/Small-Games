import pygame
import time
import random


pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

width = 10

score = 0


screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

running = True



pos = [250-width,250-width]

pos2 = [100,100]
direction = "up"

#methods


def out_of_bounds(pos1):  
    global score
    if pos1[0] < 0 or pos1[0] > SCREEN_WIDTH or pos1[1] < 0 or pos1[1] > SCREEN_HEIGHT:
        print("Game Over")
        print("Your score is {}".format(score))
        return True
    else:
        return False


    

def move(dir):
    global running
    global player
    global fruits
    global score
    new_player = []
    
    pos1 = [player[-1].left,player[-1].top]

    #print(pos1)

    if dir == "up":
        pos1[1] -= 2*width
    if dir == "down":
        pos1[1] += 2*width
    if dir == "left":
        pos1[0] -= 2*width
    if dir == "right":
        pos1[0] += 2*width


    rec = pygame.Rect(pos1[0],pos1[1],2*width,2*width)

    player.append(rec)

    if out_of_bounds(pos1):
        running = False

    self_coll = player[-1].collidelistall(player)

    if len(self_coll) != 1:
        print("Game Over")
        print("Your score is {}".format(score))
        running = False


    coll = player[-1].collidelist(fruits)

    if coll != -1:
        fruits.pop(coll)
        score += 1
        fruits.append(generate_fruit())
    else:
        player.pop(0)

def generate_fruit():
    global player
    x = random.randint(0,SCREEN_HEIGHT/(2*width))
    y = random.randint(0,SCREEN_HEIGHT/(2*width))

    fruit = pygame.Rect(x*2*width, y*2*width, 2*width, 2*width)

    return fruit
    

turn = 0
direction_save = None



rect1 = pygame.Rect(pos[0], pos[1],2*width,2*width)
rect2 = pygame.Rect(pos[0], pos[1]+2*width,2*width,2*width)


player = [rect2,rect1]
fruits = []

for i in range(3):
    fruits.append(generate_fruit())



while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           running = False

    


    
    
    screen.fill(pygame.Color(0,170,0)) 
    for x in range(0, SCREEN_WIDTH, 2*width):
        for y in range(0, SCREEN_HEIGHT, 2*width):
            rect = pygame.Rect(x, y, 2*width, 2*width)
            pygame.draw.rect(screen, "green", rect, 1)


    #print(player)
    
    for rec in player:
        #print(rec.center, turn)
        pygame.draw.rect(screen, "red", rec)


    for fruit in fruits:
        pygame.draw.rect(screen, "purple", fruit)


    pygame.display.flip()

    time.sleep(0.1)

    

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] and direction != "down":
        direction = "up"
    if keys[pygame.K_s] and direction != "up":
        direction = "down"
    if keys[pygame.K_a] and direction != "right":
        direction = "left"
    if keys[pygame.K_d] and direction != "left":
        direction = "right"

 
    move(direction)


    if score != 0 and len(fruits)/score <= 0.25:
        fruits.append(generate_fruit())


pygame.quit()



