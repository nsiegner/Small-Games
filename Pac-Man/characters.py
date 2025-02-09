import pygame

class characters(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, type):
        
        if type == "PacMan":
            self.image = pygame.image.load("Character.png")
            self.image = pygame.transform.scale(self.image,(30,30))
            self.rect = self.image.get_rect()
            self.rect.topleft = (pos_x,pos_y)



if __name__ == "__main__":
    ch1 = characters(100,100,"PacMan")