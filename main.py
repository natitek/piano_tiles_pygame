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

piano_index = (int)(0)


sample_music =['D', 'A', 'B', 'F#', 'E', 'B', 'A', 'F#', 'G', 'D', 'A', 'F#',]
lookup = ['A','A#','B','C','C#','D','D#','E','F','F#','G','G#']
themusic = []
converted = []    
def load_piano():
    for x in range(52,64):
     newsound = mixer.Sound("music/" + (str)(x) + ".mp3")
     themusic.append(newsound)
     
     
def convert_piano():
    for s in sample_music:
        for l,x in enumerate(lookup):#l is index x is item
            if s == x:
                converted.append(l)

def play_piano():
    global piano_index
    themusic[piano_index].play()
    print(piano_index)
    piano_index += 1
    if piano_index == len(sample_music)-1:
        piano_index = 0
    
        
        

def draw_lines():
    for x in range(1,4):
        pygame.draw.lines(screen,"white",True,[(100*x,0),(100*x,screen_height)],2)
def draw_circles():
    for x in range(0,4):
        pygame.draw.circle(screen,"yellow",(50+(100*x),500),10,5)
    
# newTile = Tile(0,0,100)
tilesGroup = pygame.sprite.Group()
newTile = Tile(100,-200,100)
load_piano()
convert_piano()
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    keys=pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")
    if newTile.rect.y > 0:
        if not(newTile.touched) and newTile.rect.y > screen_height:
            game_over=True
            # gameover.play()
        x = random.randrange(0,4)
        while 100*x==newTile.rect.x:
            x = random.randrange(0,4)
        newTile = newTile = Tile((100*x),-200,100)
    tilesGroup.add(newTile)  
    
    for tille in tilesGroup.sprites():
        if(tille.rect.y>0 and tille.rect.y+100<screen_height):

            if keys[pygame.K_a] and tille.rect.x==0 and not(game_over) and not(tille.touched):
                touched.stop()
                tille.touched=True
                for tile in tilesGroup.sprites():
                    tilesGroup.add(Tile(0,tille.rect.y,100,(80,80,80),tille.touched))
                    if tile.color==(0,0,0):
                        tile.kill()
                # touched.play()
            if keys[pygame.K_s] and tille.rect.x==100 and not(game_over) and not(tille.touched):
                touched.stop()
                tille.touched=True
                for tile in tilesGroup.sprites():
                    tilesGroup.add(Tile(100,tille.rect.y,100,(80,80,80),tille.touched))
                    if tile.color==(0,0,0):
                        tile.kill()
                # touched.play()
            if keys[pygame.K_d] and tille.rect.x==200 and not(game_over) and not(tille.touched):
                touched.stop()
                tille.touched=True
                for tile in tilesGroup.sprites():
                    tilesGroup.add(Tile(200,tille.rect.y,100,(80,80,80),tille.touched))
                    if tile.color==(0,0,0):
                        tile.kill()
                # touched.play()
            if keys[pygame.K_f] and tille.rect.x==300 and not(game_over) and not(tille.touched):
                touched.stop()
                tille.touched=True
                for tile in tilesGroup.sprites():
                    tilesGroup.add(Tile(300,tille.rect.y,100,(80,80,80),tille.touched))
                    if tile.color==(0,0,0):
                        tile.kill()
                # touched.play()
            if (keys[pygame.K_s] or keys[pygame.K_d] or keys[pygame.K_f]) and tille.rect.x==0 and not(game_over):
                game_over=True
                # gameover.play()
                if keys[pygame.K_s]:
                    tilesGroup.add(Tile(100,tille.rect.y,100,(255,0,0)))
                elif keys[pygame.K_d]:
                    tilesGroup.add(Tile(200,tille.rect.y,100,(255,0,0)))
                elif keys[pygame.K_f]:
                    tilesGroup.add(Tile(300,tille.rect.y,100,(255,0,0)))
            if (keys[pygame.K_a] or keys[pygame.K_d] or keys[pygame.K_f]) and tille.rect.x==100 and not(game_over):
                game_over=True
                # gameover.play()
                if keys[pygame.K_a]:
                    tilesGroup.add(Tile(0,tille.rect.y,100,(255,0,0)))
                elif keys[pygame.K_d]:
                    tilesGroup.add(Tile(200,tille.rect.y,100,(255,0,0)))
                elif keys[pygame.K_f]:
                    tilesGroup.add(Tile(300,tille.rect.y,100,(255,0,0)))
            if (keys[pygame.K_s] or keys[pygame.K_a] or keys[pygame.K_f]) and tille.rect.x==200 and not(game_over):
                game_over=True
                # gameover.play()
                if keys[pygame.K_s]:
                    tilesGroup.add(Tile(100,tille.rect.y,100,(255,0,0)))
                elif keys[pygame.K_a]:
                    tilesGroup.add(Tile(0,tille.rect.y,100,(255,0,0)))
                elif keys[pygame.K_f]:
                    tilesGroup.add(Tile(300,tille.rect.y,100,(255,0,0)))
            if (keys[pygame.K_s] or keys[pygame.K_d] or keys[pygame.K_a]) and tille.rect.x==300 and not(game_over):
                game_over=True
                # gameover.play()
                if keys[pygame.K_s]:
                    tilesGroup.add(Tile(100,tille.rect.y,100,(255,0,0)))
                elif keys[pygame.K_d]:
                    tilesGroup.add(Tile(200,tille.rect.y,100,(255,0,0)))
                elif keys[pygame.K_a]:
                    tilesGroup.add(Tile(0,tille.rect.y,100,(255,0,0)))
    # for tile in tilesGroup:
    #     if tile.rect.y == 500:
    #         print(tile.rect.y)

    # if (keys[pygame.K_p] and pygame.KEYUP):
            # pygame.mixer.stop()
            # play_piano()
        
    if not(game_over):
        for tile in tilesGroup.sprites():
            tile.update()
    for tile in tilesGroup:
        
        if tile.rect.y >= 500 and tile.rect.y < 505:
            pygame.mixer.stop()
            play_piano()
            # print(tile.rect.y)
    tilesGroup.draw(screen)
    # draw_lines()
    draw_circles()
    
    # RENDER YOUR GAME HERE
    


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
