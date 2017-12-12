from pico2d import *
import copy
from math import *
import json

class Ally:
    RANGE=0
    ATTACK_TYPE=1

    PIXEL_PER_METER = (32.0 / 3)
    RUN_SPEED_KMPH = 10.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
    TIME_PER_ACTION = 1

    MOVE_UP = 0
    MOVE_DOWN = 1
    STOP = 2

    imageList = None
    soundList = None
    statList = None

    def __init__(self,tag=0):
        if Ally.imageList == None:
            Ally.imageList = []
            Ally.soundList = []
            for i in range(1, 26):
                filename = '\c' + str(i) + '-'
                temp1 = load_image(r'resource\character\allies' + filename + '1.png')
                temp2 = load_image(r'resource\character\allies' + filename + '2.png')
                temp3 = load_image(r'resource\character\allies' + filename + '3.png')
                temp4 = load_image(r'resource\character\allies' + filename + '4.png')
                Ally.imageList.append([temp1, temp2, temp3, temp4])
            for i in range(1,2):
                temp = load_wav("resource/music/laser1.wav")
                temp.set_volume(32)
                Ally.soundList.append(temp)
            allyStatFile = open('Ally.json','r')
            Ally.statList= json.load(allyStatFile)
            allyStatFile.close()
        self.animationIndex = 0
        self.x = 0
        self.y = 0
        self.moving = [0, 0]
        self.total_frames = 0.0
        self.state = self.MOVE_DOWN
        self.mousePosition = (0,440)
        self.tag = tag
        self.image = Ally.imageList[tag]
        self.effectType = Ally.statList[tag]["effectType"]
        self.attackPoint = Ally.statList[tag]["attackPoint"]
        self.attackSound = Ally.soundList[Ally.statList[tag]["attackSound"]]

    def SetPosition(self,pos):
        self.x = pos[0]
        self.y = pos[1]
        self.mousePosition = pos

    def Update(self,frameTime):
        self.total_frames += frameTime
        if (self.total_frames > self.TIME_PER_ACTION):
            self.animationIndex += 1
            self.total_frames = 0
        if self.animationIndex > 1:
            self.animationIndex = 0
        self.Move()
        self.y = max(380, self.y + self.moving[1] * self.RUN_SPEED_PPS * frameTime)
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





