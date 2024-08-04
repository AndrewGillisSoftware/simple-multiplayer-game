import pygame
from game_classes.globals import *
from game_classes.sprite_sheet.animated_sprite import *

class Player():
    def __init__(self, position):

        self.player_sprites = pygame.sprite.Group()

        self.position = list(position)
        self.tank_rotation = 0
        self.gunner_rotation = 0

        self.speed = PIXEL * 1

        self.left_tread = AnimatedSprite(self.player_sprites, 
                                         "game_assets/tank/tank-tread_sprite-sheet.png",
                                          12, (5,14), (0, 0), SCALE)
        self.right_tread = AnimatedSprite(self.player_sprites, "game_assets/tank/tank-tread_sprite-sheet.png",
                                          12, (5,14), (0, 0), SCALE)
        self.body = AnimatedSprite(self.player_sprites, "game_assets/tank/tank-body.png", 1, (10, 12), (0, 0), SCALE)
        self.gun = AnimatedSprite(self.player_sprites, "game_assets/tank/tank-gun.png", 1, (6, 16), (0, 0), SCALE)

        self.left_tread.sprite_sheet_animator.play = True
        self.left_tread.sprite_sheet_animator.update_ms = 100

        self.right_tread.sprite_sheet_animator.play = True
        self.right_tread.sprite_sheet_animator.current_frame = 6
        self.right_tread.sprite_sheet_animator.update_ms = 100

    def __forward(self):
        self.position[1] -= self.speed
        self.left_tread.sprite_sheet_animator.flip_animation = False
        self.right_tread.sprite_sheet_animator.flip_animation = False

    def __left(self):
        self.tank_rotation -= 1
        self.tank_rotation %= 360

    def __right(self):
        self.tank_rotation += 1
        self.tank_rotation %= 360
    
    def __backward(self):
        self.position[1] += self.speed
        self.left_tread.sprite_sheet_animator.flip_animation = True
        self.right_tread.sprite_sheet_animator.flip_animation = True
    
    def __no_movement(self):
        self.left_tread.sprite_sheet_animator.play = False
        self.right_tread.sprite_sheet_animator.play = False

    def __turn_gun(self, global_mouse_position):
        pass

    def input(self):
        keys = pygame.key.get_pressed()

        made_movement = False

        # Basic movement logic
        if keys[pygame.K_a]:
            self.__left()
            made_movement = True
        if keys[pygame.K_d]:
            self.__right()
            made_movement = True
        if keys[pygame.K_w]:
            self.__forward()
            made_movement = True
        if keys[pygame.K_s]:
            self.__backward()
            made_movement = True
        
        if not made_movement:
            self.__no_movement()
        else:
            self.left_tread.sprite_sheet_animator.play = True
            self.right_tread.sprite_sheet_animator.play = True
        
        print(self.tank_rotation)

        self.__turn_gun(pygame.mouse.get_pos())

        # Update the positions of the components
        self.__update_positions()
        self.__rotate_tank()
    
    def __rotate_tank(self):
        pass
        
    def __update_positions(self):
        # Update positions of the components relative to the player's position
        self.body.rect.topleft = (self.position[0] + (PIXEL * 2), self.position[1] + (PIXEL))
        self.gun.rect.topleft = (self.position[0] + (4 * PIXEL), self.position[1] - (5 * PIXEL))
        self.left_tread.rect.topleft = (self.position[0], self.position[1])
        self.right_tread.rect.topleft = (self.position[0] + (9 * PIXEL), self.position[1])

    def update(self):
        self.input()  # Handle player input and movement

        # Update all components
        self.left_tread.update()
        self.right_tread.update()
        self.gun.update()
        self.body.update()

    def draw(self, app):
        # Draw the components
        self.player_sprites.draw(app.screen)