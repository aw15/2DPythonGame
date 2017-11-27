from pico2d import *
import copy
from math import *

class Ally:
    RANGE=0
    ATTACK_TYPE=1

    PIXEL_PER_METER = (1.0 / 1.0)
    RUN_SPEED_KMPH = 150.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 1

    MOVE_UP = 0
    MOVE_DOWN = 1
    STOP = 2

    def __init__(self,image,tag=0):
        self.animationIndex = 0
        self.x = 0
        self.y = 0
        self.moving = [0, 0]
        self.total_frames = 0.0
        self.state = self.MOVE_DOWN
        self.image = image
        self.tag = tag
        self.mousePosition = (0,440)
        if tag==0:
            self.stat = [80,0]
    def SetPosition(self,pos):
        self.x = pos[0]
        self.y = pos[1]
        self.mousePosition = pos
    def GetPosition(self):
        return (self.x,self.y)

    def Update(self,frameTime):
        self.total_frames += frameTime
        if (self.total_frames > self.TIME_PER_ACTION):
            self.animationIndex += 1
            self.total_frames = 0
        if self.animationIndex > 1:
            self.animationIndex = 0
        self.Move()
        self.y = max(430, self.y + self.moving[1] * self.RUN_SPEED_PPS * frameTime)
        self.x =self.x+ self.moving[0]*self.RUN_SPEED_PPS*frameTime
    def Draw(self,frameTime):
        if (self.state == self.MOVE_UP):
            self.image[self.animationIndex].draw(self.x, self.y)
        if (self.state == self.MOVE_DOWN):
            self.image[self.animationIndex+2].draw( self.x, self.y)
    def SetMoveDirection(self,mouseinput):
        self.mousePosition = copy.deepcopy(mouseinput)
    def Move(self):
       # print(self, "   " ,self.input)
        deltaX = self.mousePosition[0]-  self.x
        deltaY = self.mousePosition[1] - self.y
        length = math.sqrt(pow(deltaX, 2) + pow(deltaY, 2))
        if length < 10:
            self.moving = [0, 0]
            return
        self.moving = (deltaX) / length, (deltaY) / length
        if deltaY > 0:
            self.state = self.MOVE_UP
        else:
            self.state = self.MOVE_DOWN
    def isDead(self):
        if self.hp<=0:
            return True
        return False





