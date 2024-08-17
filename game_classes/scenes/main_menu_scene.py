from game_classes.scenes.scene import *

class MainMenuScene(Scene):
    def __init__(self, app):
        super().__init__(app)
    
    def draw(self):
        self.app.screen.fill("red")
        super().draw()