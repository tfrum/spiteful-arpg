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
        # this is the rect that the player will be using. Used for collision etc
        self.rect = self.image.get_rect(center = pos)

        # movement
        # Vector2(x, y) doesn't need to take arguments because it defaults to o,o
        self.direction = pygame.math.Vector2()
        # set position to be the center of the player rect
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 100

    # take input for the player object. This will be UDLR until it is mouse input
    # this will need to be updated to not run if player has clicked on an entity
    def input(self):
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pressed()

        # making player move with mouse
        if mouse[0]:
           # update the direction vector based on the mouse position
           mouse_pos = pygame.mouse.get_pos()
           self.direction = pygame.math.Vector2(mouse_pos) - pygame.math.Vector2(self.rect.center)
           self.direction.normalize_ip()
        else:
           # reset the direction when mouse released to stop movement
           self.direction = pygame.math.Vector2(0, 0)






    def move(self,dt):
        self.pos += self.direction * self.speed * dt
        self.rect.center = self.pos

    # run the update method passed from all_sprites group
    def update(self, dt):
        self.input()
        self.move(dt)