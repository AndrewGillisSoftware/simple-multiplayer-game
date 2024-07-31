import pygame

class SpriteSheet():
    def __init__(self, image_path, sprite_size, sprite_scale, frame_count):
        self.frames = []
        self.sheet = pygame.image.load(image_path).convert_alpha()
        self.sprite_width = sprite_size[0]
        self.sprite_height = sprite_size[1]
        self.sprite_scale = sprite_scale
        self.frame_count = frame_count

        # Build Frames and add to frame list
        for i in range(frame_count):
            self.frames.append(self.__build_frame(i))

    def __build_frame(self, frame):
        image = pygame.Surface((self.sprite_width, self.sprite_height)).convert_alpha()
        image.blit(self.sheet, (0, 0), ((frame * self.sprite_width), 0, self.sprite_width, self.sprite_height))
        image = pygame.transform.scale(image, (self.sprite_width * self.sprite_scale, self.sprite_height * self.sprite_scale))
        image.set_colorkey((1,1,1))

        return image
    
    def get_frame(self, frame):
        return self.frames[frame]