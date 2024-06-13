# Example file showing a basic pygame "game loop"
import pygame
from tiles import Tile
screen_width = 400
screen_height = 600
        


# pygame setup
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True

def update_GFX():
    x = 0
    while x < 4:
        newTile = Tile((x*100),0,100)
        x += 1
        tilesGroup.add(newTile)
        newTile.update()
        tilesGroup.draw(screen)
        continue
def draw_lines():
    for x in range(1,4):
        pygame.draw.lines(screen,"white",True,[(100*x,0),(100*x,screen_height)],2)
    
# newTile = Tile(0,0,100)
tilesGroup = pygame.sprite.Group()
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")
    
    update_GFX()
    draw_lines()
    
    # RENDER YOUR GAME HERE
    


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
