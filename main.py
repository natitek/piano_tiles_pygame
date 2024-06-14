# Example file showing a basic pygame "game loop"
import pygame
import random
from tiles import Tile
import pygame.mixer as mixer
screen_width = 400
screen_height = 600

# pygame setup
pygame.init()
mixer.init()
screen = pygame.display.set_mode((screen_width, screen_height))                 
clock = pygame.time.Clock()
running = True
game_over=False
touched=mixer.Sound("music/touched.mp3")
gameover=mixer.Sound("music/gameover.mp3")
    
def draw_lines():
    for x in range(1,4):
        pygame.draw.lines(screen,"White",True,[(100*x,0),(100*x,screen_height)],2)
    
# newTile = Tile(0,0,100)
tilesGroup = pygame.sprite.Group()
newTile = Tile((100),-200,100)
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    keys=pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")
    if newTile.rect.y > screen_height:
    
        if not(newTile.touched):
            game_over=True
            gameover.play()
        x = random.randrange(0,4)
        newTile = newTile = Tile((100*x),-200,100)
        
    
    tilesGroup.add(newTile)
    if(newTile.rect.y>0 and newTile.rect.y+100<screen_height):
        if keys[pygame.K_a] and newTile.rect.x==0 and not(game_over) and not(newTile.touched):
            touched.stop()
            newTile.touched=True
            for tile in tilesGroup.sprites():
                newTile = newTile=Tile(0,newTile.rect.y,100,(80,80,80),newTile.touched)
                if tile.color==(0,0,0):
                    tile.kill()
            touched.play()
        if keys[pygame.K_s] and newTile.rect.x==100 and not(game_over) and not(newTile.touched):
            touched.stop()
            newTile.touched=True
            for tile in tilesGroup.sprites():
                newTile = newTile=Tile(100,newTile.rect.y,100,(80,80,80),newTile.touched)
                if tile.color==(0,0,0):
                    tile.kill()
            touched.play()
        if keys[pygame.K_d] and newTile.rect.x==200 and not(game_over) and not(newTile.touched):
            touched.stop()
            newTile.touched=True
            for tile in tilesGroup.sprites():
                newTile = newTile=Tile(200,newTile.rect.y,100,(80,80,80),newTile.touched)
                if tile.color==(0,0,0):
                    tile.kill()
            touched.play()
        if keys[pygame.K_f] and newTile.rect.x==300 and not(game_over) and not(newTile.touched):
            touched.stop()
            newTile.touched=True
            for tile in tilesGroup.sprites():
                newTile = newTile=Tile(300,newTile.rect.y,100,(80,80,80),newTile.touched)
                if tile.color==(0,0,0):
                    tile.kill()
            touched.play()
        if (keys[pygame.K_s] or keys[pygame.K_d] or keys[pygame.K_f]) and newTile.rect.x==0 and not(game_over):
            game_over=True
            gameover.play()
            if keys[pygame.K_s]:
                tilesGroup.add(Tile(100,newTile.rect.y,100,(255,0,0)))
            elif keys[pygame.K_d]:
                tilesGroup.add(Tile(200,newTile.rect.y,100,(255,0,0)))
            elif keys[pygame.K_f]:
                tilesGroup.add(Tile(300,newTile.rect.y,100,(255,0,0)))
        if (keys[pygame.K_a] or keys[pygame.K_d] or keys[pygame.K_f]) and newTile.rect.x==100 and not(game_over):
            game_over=True
            gameover.play()
            if keys[pygame.K_a]:
                tilesGroup.add(Tile(0,newTile.rect.y,100,(255,0,0)))
            elif keys[pygame.K_d]:
                tilesGroup.add(Tile(200,newTile.rect.y,100,(255,0,0)))
            elif keys[pygame.K_f]:
                tilesGroup.add(Tile(300,newTile.rect.y,100,(255,0,0)))
        if (keys[pygame.K_s] or keys[pygame.K_a] or keys[pygame.K_f]) and newTile.rect.x==200 and not(game_over):
            game_over=True
            gameover.play()
            if keys[pygame.K_s]:

                tilesGroup.add(Tile(100,newTile.rect.y,100,(255,0,0)))
            elif keys[pygame.K_a]:
                tilesGroup.add(Tile(0,newTile.rect.y,100,(255,0,0)))
            elif keys[pygame.K_f]:
                tilesGroup.add(Tile(300,newTile.rect.y,100,(255,0,0)))
        if (keys[pygame.K_s] or keys[pygame.K_d] or keys[pygame.K_a]) and newTile.rect.x==300 and not(game_over):
            game_over=True
            gameover.play()
            if keys[pygame.K_s]:
                tilesGroup.add(Tile(100,newTile.rect.y,100,(255,0,0)))
            elif keys[pygame.K_d]:
                tilesGroup.add(Tile(200,newTile.rect.y,100,(255,0,0)))
            elif keys[pygame.K_a]:
                tilesGroup.add(Tile(0,newTile.rect.y,100,(255,0,0)))
    if not(game_over):
        newTile.update()
    tilesGroup.draw(screen)
    draw_lines()
    
    # RENDER YOUR GAME HERE
    


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
