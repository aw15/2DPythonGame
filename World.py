from pico2d import *

class World:
    buildingImage = []
    wallImage = []


    def __init__(self):
        if(len(World.buildingImage)==0):
            World.buildingImage.append( load_image(r'resource\map\big.png'))
            World.buildingImage.append(load_image(r'resource\map\small1.png'))
            World.buildingImage.append(load_image(r'resource\map\small2.png'))
            World.buildingImage.append(load_image(r'resource\map\medium.png'))
            World.wallImage.append(load_image(r'resource\map\wall_height.png'))
            World.wallImage.append(load_image(r'resource\map\wall_width.png'))


    def Draw(self):
        World.buildingImage[1].draw(300, 550)
        for i in range(0, 10):
            World.wallImage[1].draw(134 * i, 400)

