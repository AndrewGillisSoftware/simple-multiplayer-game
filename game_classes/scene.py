import pygame
from game_classes.globals import *
from game_classes.sprite import *

class Scene:
    def __init__(self, app):
        self.app = app

        self.sprites = pygame.sprite.Group()
        self.entity = Entity([self.sprites])
    
    def update(self):
        pygame.display.update()

    def draw(self):
        self.app.screen.fill("lightblue")
        self.sprites.draw(self.app.screen)