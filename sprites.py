#THIS IS BASICALLY THE DRAWING ENGINE

import pygame
from settings import *

#This class refers back to level and imports the position, surface, and rect separately
class Generic(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups, z = LAYERS['main']):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)
        self.z = z
