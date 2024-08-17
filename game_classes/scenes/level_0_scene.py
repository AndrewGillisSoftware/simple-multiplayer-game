from game_classes.scenes.scene import *

class LevelZeroScene(Scene):
    def __init__(self, app):
        super().__init__(app)

        self.player = Player((100,100))
        self.player1 = Player((139,100),True,1)

        super().add_entity(self.player)
        super().add_entity(self.player1)
    
    def draw(self):
        self.app.screen.fill("lightblue")
        super().draw()