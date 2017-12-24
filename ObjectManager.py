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
        self.gold = 100
        self.stage = 2
        self.totalDeadCount = 0
        self.enemySpawnRange = 0,2
        self.font = load_font('resource\HMKMMAG.ttf', 20)
        self.deadCount = 0
        self.win = False
        self.bgm = load_music('resource/music/background.mp3')
        self.bgm.set_volume(100)
        self.bgm.repeat_play()
        self.mousePos = [0,0]
        self.allSelect = False
        self.activeUnitList = []
    def handle_events(self,event):
        if(event.key, event.type) == (SDLK_a,SDL_KEYDOWN):
            self.allSelect = True
        elif(event.key, event.type) == (SDLK_a,SDL_KEYUP):
            self.allSelect = False
            self.activeUnitList.clear()
        if (event.type) == (SDL_MOUSEBUTTONDOWN):
            mouseInput = [event.x, 600 - event.y]
            self.mousePos = mouseInput
            if not(mouseInput[0] < 670and mouseInput[1]< 600 and mouseInput[0] > 570 and mouseInput[1] > 480):
                for unit in self.alliesList:
                    unitPosition = unit.x,unit.y
                    if (unitPosition[0] > mouseInput[0] - 15 and unitPosition[1] > mouseInput[1] - 20 and unitPosition[0] < mouseInput[0] + 15
                        and unitPosition[1] < mouseInput[1] + 20 and not self.allSelect):
                        self.activeUnit = unit
                        break
                    elif (unitPosition[0] > mouseInput[0] - 40 and unitPosition[1] > mouseInput[1] - 40 and unitPosition[0] < mouseInput[0] + 40
                        and unitPosition[1] < mouseInput[1] + 40 and self.allSelect):
                        self.activeUnitList.append(unit)
                if (self.activeUnit != None and not self.allSelect):
                    self.activeUnit.SetMoveDirection(mouseInput)
                elif len(self.activeUnitList) != 0:
                    for unit in self.activeUnitList:
                        unit.SetMoveDirection(mouseInput)
            else:
                if self.gold>20:
                    self.Recruit(mouseInput)

    def Combination(self):
        combinationList =[]
        for allies in self.alliesList:
            pos = allies.x, allies.y
            if (pos[0] < 160 and pos[1] < 600 and pos[0] > 60 and pos[1] > 480):

                combinationList.append(allies)
            if len(combinationList) == 2:
                break
        if len(combinationList) == 2:
            select = []
            if combinationList[0].tag > combinationList[1].tag:
                select.append( combinationList[0].tag)
            else:
                select.append(combinationList[1].tag)
            select.append(combinationList[0].tag + combinationList[1].tag + 3)
            newObject = Ally(min(24,random.randint(select[0],select[1])))
            newObject.SetPosition((110 , 450))
            self.alliesList.append(newObject)
            self.alliesList.remove(combinationList[0])
            self.alliesList.remove(combinationList[1])

    def SpawnEnemy(self):
        choose = random.randint(self.enemySpawnRange[0],self.enemySpawnRange[1])
        newObject = Enemy(choose)
        x = random.randint(20,750)
        newObject.SetPosition([x,-20])
        self.enemyList.append(newObject)



    def Recruit(self,mouseInput):
        choose = random.randint(0,2)
        newObject = Ally(choose)
        newObject.SetPosition((400+random.randint(0,100)-100,500+random.randint(0,100)-50))
        self.alliesList.append(newObject)
        self.gold -=20

    def Draw(self,frameTime):
        draw_rectangle(570, 480, 670, 600)
        draw_rectangle(60, 480, 160, 600)

        self.timePass2 = self.timePass + frameTime
        if(self.allSelect):
            draw_rectangle(self.mousePos[0]-50,self.mousePos[1]-50,self.mousePos[0]+50,self.mousePos[1]+50)
        else:
            draw_rectangle(self.mousePos[0]-15,self.mousePos[1]-20,self.mousePos[0]+15,self.mousePos[1]+15)

        for enemy in self.enemyList:
            enemy.Draw(frameTime)
            if (enemy.y > 290):  # 벽에 가까이 오면 성벽 체력 달기
                self.effectManager.Draw(enemy.x, enemy.y + random.randint(45,50), 5)
        for ally in self.alliesList:
            ally.Draw(frameTime)

            for enemy in self.enemyList:
                distance = pow(ally.x - enemy.x, 2) + pow(ally.y - enemy.y, 2)
                if distance < 15000:
                    self.effectManager.Draw(enemy.x, enemy.y, ally.effectType)
                    if(self.timePass2>1):
                        ally.attackSound.play()
                        self.timePass2=0
                    enemy.hp = enemy.hp - (ally.attackPoint*frameTime)
                if(enemy.hp<=0):
                    self.enemyList.remove(enemy)
                    self.deadCount += 1
                    self.totalDeadCount += 1
                    self.gold += 10 # 돈벌기
        self.font.draw(550, 580, '스테이지: %d' % self.stage, (1, 1, 1))
        self.font.draw(700, 580, '골드: %d G' % self.gold, (255, 255, 0))
        self.font.draw(300, 580, '성 체력: %d ' % self.wallHp, (1, 0, 0))
        self.font.draw(100, 580, '물리친 적: %d ' % self.totalDeadCount, (1, 1, 1))

    def Update(self, frameTime):
        self.timePass = self.timePass +frameTime
        self.Combination()
        if(self.timePass>1):
            self.SpawnEnemy()
            self.timePass = 0
        for enemy in self.enemyList:
            enemy.Update(frameTime)
            if(enemy.y>290):#벽에 가까이 오면 성벽 체력 달기
                self.WallDamage(enemy.attackPoint*frameTime)
        for ally in self.alliesList:
            ally.Update(frameTime)

        self.effectManager.Update(frameTime)
        if self.deadCount>200:
            self.stage+=1
            self.deadCount = 0

        if self.stage == 1:
            self.enemySpawnRange = 0,5
        elif self.stage == 2:
            self.enemySpawnRange = 5,9
        elif self.stage == 3:
            self.enemySpawnRange = 7,12
        elif self.stage == 4:
            self.enemySpawnRange = 10,15
        elif self.stage ==5:
            self.win = True

    def WallDamage(self,damage):
        self.wallHp -= damage