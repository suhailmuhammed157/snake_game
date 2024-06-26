import random

import pygame
import time

from pygame.locals import *

SIZE = 40
BACKGROUND_COLOR = (110, 110, 5)


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
        self.x = random.randint(1, 24) * SIZE
        self.y = random.randint(1, 19) * SIZE


class Snake:
    def __init__(self, parent_screen, length):
        self.parent_screen = parent_screen
        self.block = pygame.image.load("resources/block.jpg").convert()
        self.length = length
        self.x = [SIZE] * length
        self.y = [SIZE] * length
        self.snake_direction = "right"

    def draw(self):
        self.parent_screen.fill(BACKGROUND_COLOR)
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

    def add_block(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

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
        self.surface.fill(BACKGROUND_COLOR)
        self.snake = Snake(parent_screen=self.surface, length=7)
        self.snake.draw()
        self.apple = Apple(parent_screen=self.surface)
        self.apple.draw()

    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True

        return False

    def display_score(self):
        font = pygame.font.SysFont('arial', 30)
        score = font.render(f"Score: {self.snake.length}", True, (255, 255, 255))
        self.surface.blit(score, (800, 10))

    def show_game_over(self):
        self.surface.fill(BACKGROUND_COLOR)
        font = pygame.font.SysFont('arial', 30)
        line1 = font.render(f"Game Over. Your score is: {self.snake.length}", True, (255, 255, 255))
        self.surface.blit(line1, (200, 300))
        line1 = font.render(f"Press enter to continue game. To exit press Escape", True, (255, 255, 255))
        self.surface.blit(line1, (200, 350))
        pygame.display.flip()

    def reset_game(self):
        self.snake = Snake(parent_screen=self.surface, length=7)
        self.apple = Apple(parent_screen=self.surface)

    def play(self):
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.flip()

        if self.is_collision(self.apple.x, self.apple.y, self.snake.x[0], self.snake.y[0]):
            self.snake.add_block()
            self.apple.move()

        for i in range(3, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                raise "Game Over"

    def run(self):
        running = True
        pause = False

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_RETURN:
                        pause = False

                    if not pause:
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

            try:
                if not pause:
                    self.play()
            except Exception as e:
                self.show_game_over()
                pause = True
                self.reset_game()
            time.sleep(0.2)


if __name__ == "__main__":
    game = Game()
    game.run()
