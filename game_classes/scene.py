import pygame
from game_classes.globals import *
from game_classes.sprite import *
from game_classes.player.player import *
from game_classes.sprite_sheet.animated_sprite import *

class Scene:
    def __init__(self, app):
        self.app = app

        self.sprites = pygame.sprite.Group()
        self.entity = Entity([self.sprites])
        Entity([self.sprites], position=(100,100))
        Entity([self.sprites], position=(200,200))

        self.player = Player((100,100))
    
    def update(self):
        self.player.update()
        self.sprites.update()

    def draw(self):
        self.app.screen.fill("lightblue")
        self.sprites.draw(self.app.screen)
        self.player.draw(self.app)