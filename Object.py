from pico2d import *
import copy
from math import *


class Object:
    BUILDING=0
    ENEMY=1
    ALLIES=2

    PIXEL_PER_METER = (1.0 / 1.0)
    RUN_SPEED_KMPH = 150.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 1

    MOVE_UP = 0
    MOVE_DOWN = 1
    STOP = 2

    def __init__(self,type,image,tag):
        self.animationIndex = 0
        self.x = 0
        self.y = 0
        self.maxIndex =0
        self.moving= [0,0]
        self.total_frames = 0.0
        self.state = self.MOVE_DOWN
        self.image = image
        self.type=type
        self.tag = tag
    def SetPosition(self,pos):
        self.x = pos[0]
        self.y = pos[1]
    def GetPosition(self):
        return (self.x,self.y)

    def Move(self):
        pass

    def Damage(self,damage):
        self.hp = self.hp - damage
    def update(self,  elapsedTime):
        if (self.state == self.MOVE_UP):
            self.image[self.animationIndex].draw(self.x, self.y)
        if (self.state == self.MOVE_DOWN):
            self.image[self.animationIndex+2].draw( self.x, self.y)

        self.total_frames +=elapsedTime
        if(self.total_frames>self.TIME_PER_ACTION):
            self.animationIndex += 1
            self.total_frames =0
        if self.animationIndex>1:
            self.animationIndex=0

    def isDead(self):
        if self.hp<=0:
            return True
        return False

class Ally(Object):
    RANGE=0
    ATTACK_TYPE=1
    def __init__(self,type,image,tag=0):
        super(Ally, self).__init__(type, image, tag)
        self.input = (0,440)
        if tag==0:
            self.stat = [80,0]
    def update(self,elapsedTime, enemyList):
        super().update(elapsedTime)
        self.Move()
        self.Attack(enemyList,elapsedTime)
        self.y = max(430, self.y + self.moving[1] * self.RUN_SPEED_PPS * elapsedTime)
        self.x =self.x+ self.moving[0]*self.RUN_SPEED_PPS*elapsedTime

    def Input(self,mouseinput):
        self.input = copy.deepcopy(mouseinput)
    def Move(self):
       # print(self, "   " ,self.input)
        deltaX = self.input[0]-  self.x
        deltaY = self.input[1] - self.y
        length = math.sqrt(pow(deltaX, 2) + pow(deltaY, 2))
        if length < 10:
            self.moving = [0, 0]
            return
        self.moving = (deltaX) / length, (deltaY) / length
        if deltaY > 0:
            self.state = self.MOVE_UP
        else:
            self.state = self.MOVE_DOWN
    def Attack(self, enemyList,elapsedTime):
        for enemy in enemyList:
            enemyPos = enemy.GetPosition()
            distance = sqrt(pow(enemyPos[0]-self.x,2)+pow(enemyPos[1] - self.y,2))
            # if(self.stat[self.RANGE]>distance):
            #     Effect.effectManager.ResisterPosition(enemyPos)





class Enemy(Object):
    def __init__(self,type, image,tag=0):
        super(Enemy,self).__init__(type,image ,tag)

    def Move(self):
        deltaX = 0
        deltaY = 390 - self.y
        length = math.sqrt(pow(deltaX, 2) + pow(deltaY, 2))
        if length < 10:
            self.moving = [0, 0]
            return
        self.moving = (deltaX) / length, (deltaY) / length
        if deltaY > 0:
            self.state = self.MOVE_UP
        else:
            self.state = self.MOVE_DOWN

    def update(self, elapsedTime):
        super().update(elapsedTime)
        self.Move()
        self.y = self.y + self.moving[1] * self.RUN_SPEED_PPS * elapsedTime
        self.x = self.x + self.moving[0] * self.RUN_SPEED_PPS * elapsedTime



