from Ally import *
import random
from Enemy import *
from pico2d import *
from EffectManager import *




class ObjectManager:

    #ally 0~9
    #enemy 0~7

    wallHp = 10000
    font = None
    gold = 0
    stage = 1

    def __init__(self):
        self.enemyList = []
        self.alliesList = []
        self.activeUnit = None
        self.timePass = 0
        self.effectManager = Effect()
        ObjectManager.font = load_font('resource\HMKMMAG.ttf', 20)

    def handle_events(self,event):
        if (event.type) == (SDL_MOUSEBUTTONDOWN):
            mouseInput = [event.x, 600 - event.y]
            if (mouseInput < [320, 550] and mouseInput[0] > 280 and mouseInput[1] > 520):
                self.Recruit(mouseInput)
            else:
                for unit in self.alliesList:
                    unitPosition = unit.GetPosition()
                    if (unitPosition[0] > mouseInput[0] - 10 and unitPosition[1] > mouseInput[1] - 15 and unitPosition[
                        0] < mouseInput[0] + 10 and unitPosition[1] < mouseInput[1] + 15):
                        self.activeUnit = unit
                        break
                if (self.activeUnit != None):
                    self.activeUnit.SetMoveDirection(mouseInput)



    def SpawnEnemy(self):
        choose = random.randint(0,7)
        newObject = Enemy(0)
        x = random.randint(20,750)
        newObject.SetPosition([x,-20])
        self.enemyList.append(newObject)



    def Recruit(self,mouseInput):
        choose = random.randint(0,9)
        newObject = Ally(0)
        newObject.SetPosition((mouseInput[0],mouseInput[1]-50))
        self.alliesList.append(newObject)

    def Draw(self,elapsedTime):
        for enemy in self.enemyList:
            enemy.Draw(elapsedTime)
        for ally in self.alliesList:
            ally.Draw(elapsedTime)
        ObjectManager.font.draw(550, 580, '스테이지: %d' % ObjectManager.stage, (1, 1, 1))
        ObjectManager.font.draw(700, 580, '골드: %d G' % ObjectManager.gold, (255, 255, 0))

    def Update(self, frameTime):
        self.timePass = self.timePass +frameTime
        if(self.timePass>1):
            self.SpawnEnemy()
            self.timePass = 0

        for enemy in self.enemyList:
            enemy.Update(frameTime)
            current_pos = enemy.GetPosition()
            if(current_pos[1]>380):#벽에 가까이 오면 성벽 체력 달기
                self.WallDamage(enemy.Attack()*frameTime)
        for allies in self.alliesList:
            allies.Update(frameTime)
            allyPos = allies.GetPosition()
            for enemy in self.enemyList:
                enemyPos = enemy.GetPosition()
                if pow(allyPos[0] - enemyPos[0],2)+pow(allyPos[1] - enemyPos[1],2)>10000:
                    self.effectManager.Draw(frameTime)
    def WallDamage(self,damage):
        ObjectManager.wallHp -= damage