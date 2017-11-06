from pico2d import *

class Object:
    BUILDING=0
    ENEMY=1
    ALLIES=2
    def __init__(self,type):
        self.animationIndex = 0
        self.up = []
        self.down = []
        self.left = []
        self.right = []
        self.increase = []
        self.x = 0
        self.y = 0
        self.maxIndex =0
        self.moving= [0,0]
        self.animation_dir = 0
        self.hp =0
        self.type=type
    def SetPosition(self,pos):
        self.x = pos[0]
        self.y = pos[1]
    def Move(self, input, distance=None):
        deltaX = input[0] -  self.x
        deltaY = input[1] - self.y
        length =  math.sqrt(pow(deltaX,2) + pow(deltaY,2))
        if length < 10:
            self.moving = [0,0]
            return
        self.moving = (deltaX)/length, (deltaY)/length
        if deltaY>0:
            self.animation_dir = 0

        else:
            self.animation_dir=1
    def FindNearPoint(self, attackPoints):
        nearest = 10000
        target = ()
        currentDistance = 0
        for pos in attackPoints:
            currentDistance = math.sqrt(pow((self.x - pos[0]), 2) + pow((self.y - pos[1]), 2))
            #print(pos,"  :  ",currentDistance)
            if (nearest > currentDistance):
                nearest = currentDistance
                target = pos
        self.Move(target)
    def SetSprite(self,image ,index):
        self.image = image
        self.maxIndex = index
    def update(self,  elapsedTime):
        if (self.animation_dir == 0):
            self.image[self.animationIndex].draw(self.x, self.y)
        if (self.animation_dir == 1):
            self.image[self.animationIndex+2].draw( self.x, self.y)
        self.animationIndex = self.animationIndex+ 1
        #print(self.animationIndex)
        if(self.animationIndex > self.maxIndex):
            self.animationIndex = 0
        self.x =self.x+ self.moving[0]*elapsedTime
        self.y =self.y+ self.moving[1]*elapsedTime
    def isDead(self):
        if self.hp<=0:
            return True
        return False
