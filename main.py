import pygame, sys
from settings import *
# import our level renderer
from draw import LevelSetup

# create the game object and use settings.py to get window size
# "self" refers to the current instance of the class
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('spiteful-arpg')
        self.clock = pygame.time.Clock()
        # create the level object
        self.level = LevelSetup()
        
    def run(self):
        # main game loop
        while True:
            # check if we're closing the game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # grabbing deltatime from self.clock called above
            dt = self.clock.tick() / 1000
            # before we update the display we need to update the level
            # the level class needs deltatime to run
            self.level.run(dt)
            # update the game display
            pygame.display.update()

# create an instance of the game and run it
if __name__ == '__main__':
    game = Game()
    game.run()