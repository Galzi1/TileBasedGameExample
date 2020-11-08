import os

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# game options / settings
TITLE = "Tile Example"
WIDTH = 1024
HEIGHT = 768
FPS = 30
BGCOLOR = DARKGREY

# set up directories
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")

# settings for tile-based game
TILESIZE = 32
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

