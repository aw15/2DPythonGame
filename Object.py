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
        self.maxIndex =0
        self.horizental=True
        self.moving= [0,0]
        self.animation_dir = 0
    def SetPosition(self,pos):
        self.x = pos[0]
        self.y = pos[1]
    def Move(self, input):
        deltaX = input[0] -  self.x
        deltaY = input[1] - self.y
        length =  math.sqrt(pow(deltaX,2) + pow(deltaY,2))
        self.moving = (deltaX)/length, (deltaY)/length
        if deltaY>0:
            self.animation_dir = 0
        else:
            self.animation_dir=1
    def SetMaxIndex(self, param,isHorizen=True):
        self.maxIndex = param
        self.horizental = isHorizen
    def SetDirection(self,up,down,right, left, increase):
        self.up = up
        self.down = down
        self.left=left
        self.right = right
        self.increase = increase
    def update(self,  elapsedTime):
        if(self.horizental):
            if (self.animation_dir == 0):
                self.image.clip_draw(self.animationIndex*self.up[0],self.up[1],self.increase[0],self.increase[1],self.x,self.y)
            if (self.animation_dir == 1):
                self.image.clip_draw(self.animationIndex * self.down[0], self.down[1], self.increase[0], self.increase[1], self.x, self.y)
            # if (dir == 2):
            #     self.image.clip_draw(self.animationIndex * self.right[0], self.right[1], self.increase[0], self.increase[1], self.x, self.y)
            # if (dir == 3):
            #     self.image.clip_draw(self.animationIndex * self.left[0], self.left[1], self.increase[0], self.increase[1], self.x, self.y)
        else:
            if (self.animation_dir == 0):
                self.image.clip_draw(self.up[0],self.animationIndex*self.up[1],self.increase[0],self.increase[1],self.x,self.y)
            if (self.animation_dir == 1):
                self.image.clip_draw( self.down[0], self.animationIndex *self.down[1], self.increase[0], self.increase[1], self.x, self.y)
            # if (dir == 2):
            #     self.image.clip_draw( self.right[0], self.animationIndex *self.right[1], self.increase[0], self.increase[1], self.x, self.y)
            # if (dir == 3):
            #     self.image.clip_draw(self.left[0],self.animationIndex *  self.left[1], self.increase[0], self.increase[1], self.x, self.y)
        self.animationIndex = self.animationIndex+ 1
        #print(self.animationIndex)
        if(self.animationIndex > self.maxIndex):
            self.animationIndex = 0
        self.x =self.x+ self.moving[0]*elapsedTime
        self.y =self.y+ self.moving[1]*elapsedTime
        print(self.moving)

class Enemy(Object):
    def __init__(self, name):
        super().__init__(name)
        self.target = ()
        pass
    def FindNearPoint(self,attackPoints):
        nearest = 10000
        for pos in attackPoints:
            print(pos)
            currentDistance = math.sqrt(pow((self.x+pos[0]),2)+pow((self.y+pos[1]),2))
            if(nearest>currentDistance):
                nearest = currentDistance
                self.target = pos
        self.Move(self.target)
        pass