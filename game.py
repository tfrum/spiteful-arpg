import pygame, sys, time, random

from pygame.locals import *
pygame.init()
pygame.display.set_caption('The Diablo Scrolls VII')
screen = pygame.display.set_mode((900, 900),0,32)
display = pygame.Surface((400, 400))

grass_img = pygame.image.load('Art/grasstile.png').convert()

#Sets the color to treat as transparent in the background

grass_img.set_colorkey((0, 0, 0))

f = open('Maps/testmap.txt')
map_data = [[int(c) for c in row] for row in f.read().split('\n')]
f.close()

while True:

    #Fills the screen with black
    display.fill((0,0,0))


    for y, row in enumerate(map_data):
        for x, tile in enumerate(row):
            if tile:

                #pygame.draw.rect(display, (255, 255, 255), pygame.Rect(x * 10, y * 10, 10, 10), 1)
                display.blit(grass_img, (200 + x * 10 - y * 10, 100 + x * 5 + y * 5))

                #This snippet would be the start of rendering the next layer of blocks or assets.
                #The nested if statement runs if we have a tile then 50/50 adds another. The final number
                #is the offset to set up that tile.
                if random.randint(0, 1):
                    display.blit(grass_img, (200 + x * 10 - y * 10, 100 + x * 5 + y * 5 - 14))

    #This is how we exit the game. It's all the beginning of grabbing inputs.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

    screen.blit(pygame.transform.scale(display, screen.get_size()), (0, 0))
    pygame.display.update()
    time.sleep(1)
