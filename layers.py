import pygame
from settings import *

# this class refers back to level and imports the position, surface, and rect separately
# it allows us to create objects to be drawn by layers. All other types of spriteobject will
# inherit from this class.
class Generic(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups, z = LAYERS['main']):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)
        self.z = z
