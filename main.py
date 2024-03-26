import random

import pygame
import time

from pygame.locals import *

SIZE = 40


class Apple:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.apple = pygame.image.load("resources/apple.jpg").convert()
        self.x = SIZE * 3
        self.y = SIZE * 3

    def draw(self):
        self.parent_screen.blit(self.apple, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(1, 25) * SIZE
        self.y = random.randint(1, 20) * SIZE


class Snake:
    def __init__(self, parent_screen, length):
        self.parent_screen = parent_screen
        self.block = pygame.image.load("resources/block.jpg").convert()
        self.length = length
        self.x = [SIZE] * length
        self.y = [SIZE] * length
        self.snake_direction = "right"

    def draw(self):
        self.parent_screen.fill((110, 110, 5))
        for i in range(self.length):
            self.parent_screen.blit(self.block, (self.x[i], self.y[i]))
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

        # Let the blocks excluding the first block take the previous position
        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        # Move the first block to SIZE pixels based on direction
        if self.snake_direction == "up":
            self.y[0] -= SIZE
        if self.snake_direction == "down":
            self.y[0] += SIZE
        if self.snake_direction == "left":
            self.x[0] -= SIZE
        if self.snake_direction == "right":
            self.x[0] += SIZE

        self.draw()


class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000, 800))
        self.surface.fill((110, 110, 5))
        self.snake = Snake(parent_screen=self.surface, length=6)
        self.snake.draw()
        self.apple = Apple(parent_screen=self.surface)
        self.apple.draw()

    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 <= x2 + SIZE:
            if y1 >= y2 and y1 <= y2 + SIZE:
                return True

        return False

    def play(self):
        self.snake.walk()
        self.apple.draw()

        if self.is_collision(self.apple.x, self.apple.y, self.snake.x[0], self.snake.y[0]):
            self.apple.move()

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

            self.play()
            time.sleep(0.2)


if __name__ == "__main__":
    game = Game()
    game.run()
