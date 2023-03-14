# The sys library is only used to close the game.
import pygame, sys
from settings import *

# Create the game object and use settings.py to get window size.
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        
    def run(self)
        # This is the main game loop.
        while True:
            # This checks if we're closing the game.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Grabbing Delta time.
            dt = self.clock.tick() / 1000
            # Update the game display.
            pygame.display.update()