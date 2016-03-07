"""
spaceshooter.py
Author: Avery Wallis
Credit: <list sources used, if any>

Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""
from ggame import App, ImageAsset, RectangleAsset, SoundAsset
from ggame import LineStyle, Sprite, Sound, Color




SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# Background
black = Color(0, 1)
noline = LineStyle(0, black)
bg_asset = RectangleAsset(SCREEN_WIDTH, SCREEN_HEIGHT, noline, black)
bg = Sprite(bg_asset, (0,0))

class SpaceGame(App):
    """
    Tutorial4 space game example.
    """
    def __init__(self, width, height):
        super().__init__(width, height)

myapp = App(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()