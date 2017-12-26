from pico2d import *
from TileMap import *

class World:



    def __init__(self):
        self.buildingImage = None
        self.wallImage = None
        self.stage1 = load_tile_map("stage1.json")
        self.stage2 = load_tile_map("stage2.json")
        self.stage3 = load_tile_map("stage4.json")
        self.stage4 = load_tile_map("stage5.json")
        self.stage5 = load_tile_map("stage3.json")
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
    def Draw(self,stage):
        if(stage ==1):
            self.stage1.clip_draw_to_origin(0,0, self.canvas_width, self.canvas_height, 0, 0)
        if (stage == 2):
            self.stage2.clip_draw_to_origin(0, 0, self.canvas_width, self.canvas_height, 0, 0)
        if (stage == 3):
            self.stage3.clip_draw_to_origin(0, 0, self.canvas_width, self.canvas_height, 0, 0)
        if (stage == 4):
            self.stage4.clip_draw_to_origin(0, 0, self.canvas_width, self.canvas_height, 0, 0)
        if (stage == 5):
            self.stage5.clip_draw_to_origin(0, 0, self.canvas_width, self.canvas_height, 0, 0)

