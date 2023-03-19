import pygame
from settings import *
from player import Player
from layers import Generic
from pytmx.util_pygame import load_pygame

# this class will actually render the player, environment, enemies.
class LevelSetup:
    def __init__(self):
        
        # grab the display surface called in __main__ so that the level object can draw to it
        self.display_surface = pygame.display.get_surface()

        # create the sprite group. Sprite groups are a part of pygame
        self.all_sprites = CameraGroup()

        # here we call the setup method which creates the player
        self.setup()

    def setup(self):
        #load_pygame('../data/town.tmx')
        self.player = Player((SCREEN_WIDTH/2,SCREEN_HEIGHT/2), self.all_sprites)

        #For now this draws the background as a reference point.
        Generic(
            pos = (0,0),
            surf = pygame.image.load('assets/testmap.png').convert_alpha(),
            groups = self.all_sprites,
            z = LAYERS['backdrop'])
        
    def run(self,dt): 
        self.display_surface.fill('black')
        self.all_sprites.custom_draw(self.player)
        self.all_sprites.update(dt)


# the class that allows us to draw the sprite rect and sprite image separately.
class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()

    # draw things in order of y-position for overlap
    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - SCREEN_WIDTH / 2
        self.offset.y = player.rect.centery - SCREEN_HEIGHT / 2

        for layer in LAYERS.values(): 
            for sprite in self.sprites():
                    if sprite.z == layer:
                        offset_rect = sprite.rect.copy()
                        offset_rect.center -= self.offset
                        self.display_surface.blit(sprite.image, offset_rect)
                        print("O: ", offset_rect.center)
                        print("P: ", player.pos)
