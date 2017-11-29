from Ally import *
import random
from Enemy import *
from pico2d import *
from EffectManager import *




class ObjectManager:

    #ally 0~9
    #enemy 0~7



    def __init__(self):
        self.enemyList = []
        self.alliesList = []
        self.activeUnit = None
        self.timePass = 0
        self.effectManager = Effect()
        self.wallHp = 10000
        self.gold = 0
        self.stage = 1
        self.enemySpawnRange = 0,3
        self.font = load_font('resource\HMKMMAG.ttf', 20)
        self.deadCount = 0
        self.win = False

    def handle_events(self,event):
        if (event.type) == (SDL_MOUSEBUTTONDOWN):
            mouseInput = [event.x, 600 - event.y]
            if (mouseInput < [320, 550] and mouseInput[0] > 280 and mouseInput[1] > 520):
                self.Recruit(mouseInput)
            else:
                for unit in self.alliesList:
                    unitPosition = unit.x,unit.y
                    if (unitPosition[0] > mouseInput[0] - 10 and unitPosition[1] > mouseInput[1] - 15 and unitPosition[
                        0] < mouseInput[0] + 10 and unitPosition[1] < mouseInput[1] + 15):
                        self.activeUnit = unit
                        break
                if (self.activeUnit != None):
                    self.activeUnit.SetMoveDirection(mouseInput)



    def SpawnEnemy(self):
        choose = random.randint(self.enemySpawnRange[0],self.enemySpawnRange[1])
        newObject = Enemy(choose)
        x = random.randint(20,750)
        newObject.SetPosition([x,-20])
        self.enemyList.append(newObject)



    def Recruit(self,mouseInput):
        choose = random.randint(0,9)
        newObject = Ally(0)
        newObject.SetPosition((mouseInput[0],mouseInput[1]-50))
        self.alliesList.append(newObject)

    def Draw(self,frameTime):
        for enemy in self.enemyList:
            enemy.Draw(frameTime)
        for ally in self.alliesList:
            ally.Draw(frameTime)

            for enemy in self.enemyList:
                distance = pow(ally.x - enemy.x, 2) + pow(ally.y - enemy.y, 2)
                if distance < 10000:
                    self.effectManager.Draw(enemy.x, enemy.y, ally.effectType)
                    enemy.hp = enemy.hp - (ally.attackPoint*frameTime)
                if(enemy.hp<=0):
                    self.enemyList.remove(enemy)
                    self.deadCount += 1
                    self.gold += enemy.gold
        self.font.draw(550, 580, '스테이지: %d' % self.stage, (1, 1, 1))
        self.font.draw(700, 580, '골드: %d G' % self.gold, (255, 255, 0))

    def Update(self, frameTime):
        self.timePass = self.timePass +frameTime
        if(self.timePass>1):
            self.SpawnEnemy()
            self.timePass = 0
        for enemy in self.enemyList:
            enemy.Update(frameTime)
            if(enemy.y>380):#벽에 가까이 오면 성벽 체력 달기
                self.WallDamage(enemy.attackPoint*frameTime)
        for ally in self.alliesList:
            ally.Update(frameTime)
        self.effectManager.Update(frameTime)
        if self.deadCount>100:
            self.stage+=1
            self.enemySpawnRange = 2,5
        elif self.deadCount>200:
            self.stage+=1
            self.enemySpawnRange = 4, 6
        elif self.deadCount>300:
            self.stage+=1
            self.enemySpawnRange = 6, 8
        elif self.deadCount>400:
            self.stage+=1
            self.enemySpawnRange = 6, 11
        elif self.deadCount>500:
            self.stage+=1
            self.enemySpawnRange = 12, 14
        elif self.deadCount>600:
            pass

    def WallDamage(self,damage):
        self.wallHp -= damage