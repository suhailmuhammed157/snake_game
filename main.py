import pygame
import time

from pygame.locals import *

if __name__ == "__main__":
    pygame.init()

    surface = pygame.display.set_mode((500,500))
    surface.fill((92,25,84))
    pygame.display.flip()


running = True

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False