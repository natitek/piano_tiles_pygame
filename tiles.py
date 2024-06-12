import pygame
import main

screen_width = main.screen_width
class tile():
    def __init__(self,x,y):
        self.tiles = pygame.sprite.Group()
        self.x = x
        self.y = y
        self.width = screen_width/4
        self.height = 40
        self.create_tiles()
    def create_tiles(self):
        tile  = pygame.rect.Rect(self.x,self.y,self.width,self.height)
        tiles = self.tiles.add(tile)
        return tiles
    def update(self):
        self.y += 10
        