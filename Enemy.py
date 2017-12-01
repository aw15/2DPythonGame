from pico2d import *
import json
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

    imageList = None
    statList = None
    def __init__(self,tag):
        if Enemy.imageList==None:
            Enemy.imageList = []

            for i in range(1,16):
                filename = '\e' + str(i) + '-'
                print(filename)
                temp1 = load_image(r'resource\character\enemy' + filename + '1.png')
                temp2 = load_image(r'resource\character\enemy' + filename + '2.png')
                temp3 = load_image(r'resource\character\enemy' + filename + '3.png')
                temp4 = load_image(r'resource\character\enemy' + filename + '4.png')
                Enemy.imageList.append([temp1, temp2, temp3, temp4])
            enemyStatText = open('Enemy.json','r')
            Enemy.staList = json.load(enemyStatText)
            enemyStatText.close()
        self.animationIndex = 0
        self.x = 0
        self.y = 0
        self.moving = [0, 0]
        self.total_frames = 0.0
        self.state = self.MOVE_DOWN
        self.image = Enemy.imageList[tag]
        self.gold = 10
        self.hp = 10
        self.attackPoint = 10


    def SetPosition(self, pos):
        self.x = pos[0]
        self.y = pos[1]


    def Move(self):
        pass

    def Damage(self, damage):
        self.hp = self.hp - damage

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

