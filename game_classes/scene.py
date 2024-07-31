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

        self.player = Player([self.sprites])        
        self.anim = AnimatedSprite([self.sprites],
                                    "game_assets/tank/tank-tread_sprite-sheet.png",
                                    12, (5,14), (100, 100), 10)
        
        self.anim.sprite_sheet_animator.play = True
        self.anim.sprite_sheet_animator.loop = True
        self.anim.sprite_sheet_animator.flip_animation = True
        self.anim.sprite_sheet_animator.update_ms = 100

    
    def update(self):
        self.sprites.update()

    def draw(self):
        self.app.screen.fill("lightblue")
        self.sprites.draw(self.app.screen)