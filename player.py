import pygame
import math
from settings import *
from support import *

# create a player class that inherits from pygame.sprite.Sprite
# this is because the player is a sprite, lmao
class Player(pygame.sprite.Sprite):

    # initialize only position (pos) and the group for now
    def __init__(self, pos, group):
        super().__init__(group)
        
        # attributes
        self.z = LAYERS['main']
        self.status = 'south'

        # animation
        self.import_assets()
        self.frame_index = 0
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center = pos)


        # movement variables
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 150

    # Mouse input for the player object
    # this will need to be updated to not run if player has clicked on an entity

    def import_assets(self):
        self.animations = {'south':[]}
        #self.animations = {'north':[], 'northeast':[], 'east':[], 'southeast':[],
        #                   'south':[], 'southwest':[], 'west':[], 'northwest':[]}

        for animation in self.animations.keys():
            full_path = 'assets/player/animations/' + animation
            self.animations[animation] = import_folder(full_path)

    def animate(self, dt):
        self.frame_index += 4 * dt
        if self.frame_index >= len(self.animations[self.status]):
            self.frame_index = 0

        self.image = self.animations[self.status][int(self.frame_index)]

    def input(self):
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pressed()

        # making player move with mouse - This isn't working as expected.

        if mouse[0]:
            # update the direction vector based on the mouse position
            mouse_pos = pygame.mouse.get_pos()

            self.directionCartesian = pygame.math.Vector2(mouse_pos) - pygame.math.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
            # In order to normalize  the vector it can't be zero.
            if self.directionCartesian.magnitude() > 0:
                self.directionCartesian.normalize_ip()


        else:
           # reset the direction when mouse released to stop movement
           self.directionCartesian = pygame.math.Vector2(0, 0)
        
    def move(self,dt):
        # convert cartesian directional inputs to pseudo-isometric

        self.pos.x += self.directionCartesian.x * self.speed * dt
        self.pos.y += self.directionCartesian.y * self.speed * .7 * dt
        self.rect.center = self.pos
        print(round(self.pos.x, 0), round(self.pos.y, 0))

    # run the update method passed from all_sprites group
    def update(self, dt):
        self.input()
        self.move(dt)
        self.animate(dt)
