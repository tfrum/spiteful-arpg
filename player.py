import pygame
from settings import *

# create a player class that inherits from pygame.sprite.Sprite
# this is because the player is a sprite, lmao
class Player(pygame.sprite.Sprite):

    # initialize only position (pos) and the group for now
    def __init__(self, pos, group):
        # super() is being used to initialize the parent/superclass Sprite which player inherits from
        super().__init__(group)

        self.image = pygame.Surface((28,69))
        self.image.fill ('blue')
        self.rect = self.image.get_rect(center = pos)
        #This is the z position that tells the drawer which order to draw in.
        self.z = LAYERS['main']

        # movement
        # define the direction stat for the player
        self.direction = pygame.math.Vector2()
        # set position to be the center of the player rect
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 400

    # Mouse input for the player object
    # this will need to be updated to not run if player has clicked on an entity
    def input(self):
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pressed()

        # making player move with mouse - This isn't working as expected.

        if mouse[0]:
           # update the direction vector based on the mouse position
           mouse_pos = pygame.mouse.get_pos()
           self.direction = pygame.math.Vector2(mouse_pos) - pygame.math.Vector2(self.rect.center)
           # In order to normalize  the vector it can't be zero.
           if self.direction.magnitude() > 0:
                self.direction.normalize_ip()




                
        #else:
           # reset the direction when mouse released to stop movement
           #self.direction = pygame.math.Vector2(0, 0)
        
        print(self.direction)






    def move(self,dt):
        self.pos += self.direction * self.speed * dt
        self.rect.center = self.pos

    # run the update method passed from all_sprites group
    def update(self, dt):
        self.input()
        self.move(dt)