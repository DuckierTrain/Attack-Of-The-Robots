# imports everything needed to make the code work
import pygame
from player import Player

# Start the game
#pygame.init()
game_width = 1000
game_height = 650
screen = pygame.display.set_mode((game_width, game_height))
clock = pygame.time.Clock()
running = True

background_image = pygame.image.load("../assets/BG_Grass.png")

playerGroup = pygame.sprite.Group()

player.containers = playerGroup

mr_player = Player(screen, game_width/2, game_height/2)




# ***************** Loop Land Below *****************
# Everything under 'while running' will be repeated over and over again
while running:
    # Makes the game stop if the player clicks the X or presses esc
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    #player input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        mr_player.move(3,0)
    if keys[pygame.K_a]:
        mr_player.move(-3,0)

    if keys[pygame.K_w]:
        mr_player.move(0,-3)
        
    if keys[pygame.K_s]:
        mr_player.move(0,3)
        
    screen.blit(background_image, (0, 0))

    mr_player.update()



    # Tell pygame to update the screen
    pygame.display.flip()
    clock.tick(40)
    pygame.display.set_caption("ATTACK OF THE ROBOTS fps: " + str(clock.get_fps()))
