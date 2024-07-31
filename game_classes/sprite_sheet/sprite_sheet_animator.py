import pygame
from game_classes.sprite_sheet.sprite_sheet import *

class SpriteSheetAnimator():
    def __init__(self, sprite_sheet: SpriteSheet):
        self.__current_image = sprite_sheet.get_frame(0)
        self.__sprite_sheet = sprite_sheet
        self.current_frame = 0
        self.play = False
        self.stop_at_frame = None
        self.update_ms = 1000
        self.loop = True
        self.flip_animation = False
        self.__last_update_time = pygame.time.get_ticks()

    def __update_animation(self):
        # Stop at frame only works with looped animations
        if self.stop_at_frame != None:
            self.loop = True
            if self.stop_at_frame == self.current_frame:
                self.play = False
                return
        
        # Increment frame based on animation direction
        if self.flip_animation:
            self.current_frame -= 1
        else:
            self.current_frame += 1

        # At end of frames in either direction
        if self.current_frame > self.__sprite_sheet.frame_count - 1 and not self.flip_animation:
            # Determine if animation should loop
            if self.loop:
                self.current_frame = 0
            else:
                self.play = False
                return

        # At end of frames in either direction
        if self.current_frame < 0 and self.flip_animation:
            # Determine if animation should loop
            if self.loop:
                self.current_frame = self.__sprite_sheet.frame_count - 1
            else:
                self.play = False
                return
        
        # Update current image
        self.__current_image = self.__sprite_sheet.get_frame(self.current_frame)

    
    def update(self):
        if self.play:
            current_time = pygame.time.get_ticks()
            if current_time - self.__last_update_time >= self.update_ms:
                self.__last_update_time = current_time
                self.__update_animation()
    
    def get_frame(self):
        return self.__current_image
    