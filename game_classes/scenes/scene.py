import pygame
from game_classes.globals import *
from game_classes.sprite import *
from game_classes.player.player import *
from game_classes.sprite_sheet.animated_sprite import *

class Scene:
    def __init__(self, app):
        self.app = app
        self.sprites = []
    
    def add_entity(self, entity):
        self.sprites.append(entity)
    
    def update(self):
        for sprite in self.sprites:
            sprite.update()

    def draw(self):
        for sprite in self.sprites:
            sprite.draw(self.app)