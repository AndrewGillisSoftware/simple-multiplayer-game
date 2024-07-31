import pygame
from game_classes.sprite_sheet.sprite_sheet_animator import *

class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, groups, sprite_sheet_image, frame_count, size, position = (0,0), scale = 1):
        super().__init__(groups)
        self.sprite_sheet_animator = SpriteSheetAnimator(SpriteSheet(sprite_sheet_image, size, scale, frame_count))
        self.image = self.sprite_sheet_animator.get_frame()
        self.rect = self.image.get_rect(topleft = position)
    
    def update(self):
        self.sprite_sheet_animator.update()
        self.image = self.sprite_sheet_animator.get_frame()
        self.rect.x += 1
        