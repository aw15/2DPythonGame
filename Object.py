from pico2d import *

class Object:
    def __init__(self, name):
        self.image = load_image(name)
        self.animationIndex = 0
        self.up = []
        self.down = []
        self.left = []
        self.right = []
        self.increase = []
        self.x = 0
        self.y = 0
    def SetPosition(self,x,y):
        self.x = x
        self.y = y
    def SetDirection(self,up,down,right, left, increase):
        self.up = up
        self.down = down
        self.left=left
        self.right = right
        self.increase = increase
    def update(self, dir):
        if (dir == 0):
            self.image.clip_draw(self.animationIndex*self.up[0],self.up[1],self.increase[0],self.increase[1],self.x,self.y)
        if (dir == 1):
            self.image.clip_draw(self.animationIndex * self.down[0], self.down[1], self.increase[0], self.increase[1], self.x, self.y)
        if (dir == 2):
            self.image.clip_draw(self.animationIndex * self.right[0], self.down[1], self.increase[0], self.increase[1], self.x, self.y)
        if (dir == 3):
            self.image.clip_draw(self.animationIndex * self.left[0], self.left[1], self.increase[0], self.increase[1], self.x, self.y)
        self.animationIndex+=1
        self.animationIndex%=3