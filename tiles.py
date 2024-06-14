import pygame


screen_width = 400
class Tile(pygame.sprite.Sprite):
    def __init__(self,x,y,size,color=(0,0,0),touched=False):
        super().__init__()
        self.touched=touched
        self.color=color
        self.image = pygame.Surface((size,size*2))
        self.image.fill(self.color)
        self.rect = self.image.get_rect(topleft = (x,y))
    def update(self):
        self.rect.y += 10