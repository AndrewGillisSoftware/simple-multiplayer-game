import pygame
import sys
from game_classes.globals import *
from game_classes.scene import Scene

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.scene = Scene(self)

    def run(self):
        self.running = True
        while self.running:
            self.update()
            self.draw()
        self.close()

    def update(self):
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    self.running = False

        self.scene.update()
        self.clock.tick(FPS)

    def draw(self):
        self.screen.fill('blue')
        self.scene.draw()

    def close(self):
        pygame.quit()
        sys.exit()
