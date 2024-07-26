from typing import Any
import pygame
from game_classes.globals import *

class Player(pygame.sprite.Sprite):
    def __init__(self, groups, image=pygame.Surface((TILE_SIZE, TILE_SIZE)), position = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)):
        super().__init__(groups)
        self.image = image
        self.image.fill('green')
        self.rect = self.image.get_rect(topleft = position)

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rect.x -= 1

        if keys[pygame.K_d]:
            self.rect.x += 1

        if keys[pygame.K_w]:
            self.rect.y += 1

        if keys[pygame.K_s]:
            self.rect.y -= 1
    
    
    def update(self):
        self.input()