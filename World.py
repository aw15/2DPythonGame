from pico2d import *
from TileMap import *

class World:



    def __init__(self):
        self.buildingImage = None
        self.wallImage = None
        self.stage1 = load_tile_map("json/stage1.json")
        self.stage2 = load_tile_map("json/stage2.json")
        self.stage3 = load_tile_map("json/stage2.json")
        self.stage4 = load_tile_map("json/stage2.json")
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.activeStage = 1
    def Draw(self, stage):
        if(self.activeStage ==1):
            self.stage1.clip_draw_to_origin(0,0, self.canvas_width, self.canvas_height, 0, 0)
        if (self.activeStage == 2):
            self.stage2.clip_draw_to_origin(0, 0, self.canvas_width, self.canvas_height, 0, 0)
        if (self.activeStage == 3):
            self.stage3.clip_draw_to_origin(0, 0, self.canvas_width, self.canvas_height, 0, 0)
        if (self.activeStage == 4):
            self.stage4.clip_draw_to_origin(0, 0, self.canvas_width, self.canvas_height, 0, 0)

