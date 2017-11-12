from pico2d import *
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

    def __init__(self,type,hp=0):
        self.animationIndex = 0
        self.x = 0
        self.y = 0
        self.maxIndex =0
        self.moving= [0,0]
        self.total_frames = 0.0
        self.state = self.MOVE_DOWN
        self.hp =hp
        self.type=type
        self.input =[0,0]
    def SetPosition(self,pos):
        self.x = pos[0]
        self.y = pos[1]
    def GetPosition(self):
        return (self.x,self.y)
    def SetMouseInput(self, input):
        self.input = input
    def AlliesMove(self):
        deltaX = self.input[0] -  self.x
        deltaY = self.input[1] - self.y
        length =  math.sqrt(pow(deltaX,2) + pow(deltaY,2))
        if length < 10:
            self.moving = [0,0]
            self.state =self.STOP
            return
        self.moving = (deltaX)/length, (deltaY)/length
        if deltaY>0:
            self.MOVE_UP
        else:
            self.MOVE_DOWN
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
    def Damage(self,damage):
        self.hp = self.hp - damage
    def SetSprite(self,image ,index):
        self.image = image
        self.maxIndex = index
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

        self.x =self.x+ self.moving[0]*self.RUN_SPEED_PPS*elapsedTime
        if(self.type == Object.ALLIES):
            self.y = max(430,self.y + self.moving[1] * self.RUN_SPEED_PPS * elapsedTime)
        else:
            self.y = self.y + self.moving[1] * self.RUN_SPEED_PPS * elapsedTime
    def isDead(self):
        if self.hp<=0:
            return True
        return False

