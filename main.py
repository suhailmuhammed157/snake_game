import pygame
import time

from pygame.locals import *


class Snake:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.block = pygame.image.load("resources/block.jpg").convert()
        self.x = 100
        self.y = 100
        self.snake_direction = "right"

    def draw(self):
        self.parent_screen.fill((92, 25, 84))
        self.parent_screen.blit(self.block, (self.x, self.y))
        pygame.display.flip()

    def move_up(self):
        self.snake_direction = "up"

    def move_down(self):
        self.snake_direction = "down"

    def move_left(self):
        self.snake_direction = "left"

    def move_right(self):
        self.snake_direction = "right"

    def walk(self):
        if self.snake_direction == "up":
            self.y -= 10
        if self.snake_direction == "down":
            self.y += 10
        if self.snake_direction == "left":
            self.x -= 10
        if self.snake_direction == "right":
            self.x += 10
        self.draw()


class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((500, 500))
        self.surface.fill((92, 25, 84))
        self.snake = Snake(parent_screen=self.surface)
        self.snake.draw()

    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_UP:
                        self.snake.move_up()

                    if event.key == K_DOWN:
                        self.snake.move_down()

                    if event.key == K_LEFT:
                        self.snake.move_left()

                    if event.key == K_RIGHT:
                        self.snake.move_right()

                elif event.type == QUIT:
                    running = False

            self.snake.walk()
            time.sleep(0.2)


if __name__ == "__main__":
    game = Game()
    game.run()
