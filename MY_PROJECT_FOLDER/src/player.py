import pygame

class Player(pygame.sprite.Sprite):
    #Player Constructor function
    def __init__(self, screen, x, y):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load("../assets/Player_02.png")\
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.speed = 5

    # Player update function
    def update(self):
        self.rect.center = (self.x, self.y)
        self.screen.blit(self.image, (self.rect)

    #player move variables
    def move(self, x_movement, y_movement):
        self.x += self.speed * x_movement
        self.y += self.speed * y_movement
        
        
    
