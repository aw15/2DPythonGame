import Object
import random
from Enemy import *
from pico2d import *




class ObjectManager:

    BUILDING=0
    ENEMY=1
    ALLIES=2

    #unit initialize---------------------------------------------------------
    ENEMY_ATTACKPOINT =10
    ALLIES_ATTACKPOINT =10


    wallHp = 10000

    def __init__(self):
        self.enemyList = []
        self.alliesList = []
        self.alliesImageList=[]
        self.enemyImageList=[]
        self.activeUnit = None
        self.timePass = 0
        for i in range(1, 11):
            filename = '\c' + str(i) + '-'
            temp1 = load_image(r'resource\character\allies' + filename + '1.png')
            temp2 = load_image(r'resource\character\allies' + filename + '2.png')
            temp3 = load_image(r'resource\character\allies' + filename + '3.png')
            temp4 = load_image(r'resource\character\allies' + filename + '4.png')
            self.alliesImageList.append([temp1, temp2, temp3, temp4])

        for i in range(1, 9):
            filename = '\e' + str(i) + '-'
            temp1 = load_image(r'resource\character\enemy' + filename + '1.png')
            temp2 = load_image(r'resource\character\enemy' + filename + '2.png')
            temp3 = load_image(r'resource\character\enemy' + filename + '3.png')
            temp4 = load_image(r'resource\character\enemy' + filename + '4.png')
            self.enemyImageList.append([temp1, temp2, temp3, temp4])

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
                    self.activeUnit.Input(mouseInput)

    def Draw(self,elapsedTime):
        for enemy in self.enemyList:
            enemy.Draw(elapsedTime)
        pass

    def SpawnEnemy(self):
        choose = random.randint(0,7)
        newObject = Enemy(self.enemyImageList[choose],0)
        x = random.randint(20,750)
        newObject.SetPosition([x,-20])
        self.enemyList.append(newObject)



    def Recruit(self,mouseInput):
        choose = random.randint(0,9)
        newObject = Object.Ally(self.alliesImageList[choose],0)
        newObject.SetPosition((mouseInput[0],mouseInput[1]-50))
        self.alliesList.append(newObject)


    def Update(self, elapsedTime):
        self.timePass = self.timePass +elapsedTime
        if(self.timePass>1):
            self.SpawnEnemy()
            self.timePass = 0
        for enemy in self.enemyList:
            enemy.Update(elapsedTime)
            current_pos = enemy.GetPosition()
            if(current_pos[1]>380):#벽에 가까이 오면 성벽 체력 달기
                #wallHp = wallHp - (enemy.hp*elapsedTime)
                pass
        for allies in self.alliesList:
            allies.update(elapsedTime,self.enemyList)