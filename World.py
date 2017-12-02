from pico2d import *

class World:



    def __init__(self):
        self.buildingImage = None
        self.wallImage = None
        if(self.buildingImage==None):
            self.wallImage=[]
            self.buildingImage=[]
            self.buildingImage.append( load_image(r'resource\map\big.png'))
            self.buildingImage.append(load_image(r'resource\map\small1.png'))
            self.buildingImage.append(load_image(r'resource\map\small2.png'))
            self.buildingImage.append(load_image(r'resource\map\medium.png'))
            self.wallImage.append(load_image(r'resource\map\wall_height.png'))
            self.wallImage.append(load_image(r'resource\map\wall_width.png'))


    def Draw(self):
        self.buildingImage[1].draw(300, 550)
        self.buildingImage[0].draw(100, 550)
        for i in range(0, 10):
            self.wallImage[1].draw(134 * i, 400)

