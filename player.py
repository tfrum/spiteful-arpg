import pygame
from settings import *

# create a player class that inherits from pygame.sprite.Sprite
# this is because the player is a sprite, lmao
class Player(pygame.sprite.Sprite):

    # we're just going to pass the position (pos) and the group for now.
    def __init__(self, pos, group):

        # super() is being used to initialize the parent/superclass Sprite which player inherits from.
        super().__init__(group)

        # this is the image that the player will be using, defines height and width.
        # nice
        self.image = pygame.Surface((69,32))
        self.image.fill ('blue')
        
        # this is the rect that the player will be using. These are used for detection, collision, etc.
        # it gets cenetered on the position of the player.
        self.rect = self.image.get_rect(center = pos)