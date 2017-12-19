from pico2d import *
from TileMap import *

class World:



    def __init__(self):
        self.buildingImage = None
        self.wallImage = None
        self.stage1 = load_tile_map("json/stage2.json")
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()

    def Draw(self, stage):
        self.stage1.clip_draw_to_origin(0,0, self.canvas_width, self.canvas_height, 0, 0)

