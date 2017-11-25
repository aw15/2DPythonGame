from pico2d import *
import copy
from math import *



class Enemy:

    PIXEL_PER_METER = (1.0 / 1.0)
    RUN_SPEED_KMPH = 150.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 1

    MOVE_UP = 0
    MOVE_DOWN = 1
    STOP = 2

    def __init__(self, image, tag):
        self.animationIndex = 0
        self.x = 0
        self.y = 0
        self.maxIndex = 0
        self.moving = [0, 0]
        self.total_frames = 0.0
        self.state = self.MOVE_DOWN
        self.image = image
        self.type = type
        self.tag = tag

    def SetPosition(self, pos):
        self.x = pos[0]
        self.y = pos[1]

    def GetPosition(self):
        return (self.x, self.y)

    def Move(self):
        pass

    def Damage(self, damage):
        self.hp = self.hp - damage

    def Update(self, elapsedTime):
        pass
    def Draw(self, elapsedTime):
        if (self.state == self.MOVE_UP):
            self.image[self.animationIndex].draw(self.x, self.y)
        if (self.state == self.MOVE_DOWN):
            self.image[self.animationIndex + 2].draw(self.x, self.y)

        self.total_frames += elapsedTime
        if (self.total_frames > self.TIME_PER_ACTION):
            self.animationIndex += 1
            self.total_frames = 0
        if self.animationIndex > 1:
            self.animationIndex = 0

    def IsDead(self):
        if self.hp <= 0:
            return True
        return False

    def Update(self, elapsedTime):
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
        self.y = self.y + self.moving[1] * self.RUN_SPEED_PPS * elapsedTime
        self.x = self.x + self.moving[0] * self.RUN_SPEED_PPS * elapsedTime

