import pygame
from settings import *
from player import Player

# this class will actually render the player, environment, enemies.
class Level:
    def __init__(self):
        
        # grab the display surface called in __main__ so that the level object can draw to it
        self.display_surface = pygame.display.get_surface()

        # create the sprite group. Sprite groups are a part of pygame
        self.all_sprites = pygame.sprite.Group()

        # here we call the setup method which creates the player
        self.setup()


    def setup(self):
        # create the player
        # we initialized player to take a position and a group in player.py
        # I'm going to set it to be central to the screen at all times. This will change when we have movement.
        self.player = Player((SCREEN_WIDTH/2,SCREEN_HEIGHT/2), self.all_sprites)

    # run the initialized Level
    def run(self,dt):

        # fill the underlying surface with black
        self.display_surface.fill('black')
        self.all_sprites.draw(self.display_surface)

        # this update method gets passed to all the chldren of all_sprites (player, enemies, etc)
        self.all_sprites.update(dt)