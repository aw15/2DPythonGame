import Object
import random
from pico2d import *


BUILDING=0
ENEMY=1
ALLIES=2

#unit initialize---------------------------------------------------------
ENEMY_ATTACKPOINT =10
ALLIES_ATTACKPOINT =10

enemyImageList =[]
alliesImageList =[]
wallHp = 10000


timePass=0
current_time = get_time()
elapsedTime = None

enemyList = []
alliesList = []


def SetUnitList(allies, enemy):
    global enemyImageList, alliesImageList
    enemyImageList = enemy
    alliesImageList = allies



def SpawnEnemy():
    global  enemyImageList, enemyList, ENEMY_ATTACKPOINT
    choose = random.randint(0,7)
    newObject = Object.Enemy(ENEMY,enemyImageList[choose],0)
    x = random.randint(20,750)
    newObject.SetPosition([x,-20])
    enemyList.append(newObject)



def Recruit(mouseInput):
    global alliesImageList,  alliesList, ALLIES_ATTACKPOINT
    choose = random.randint(0,9)
    newObject = Object.Ally(ALLIES,alliesImageList[choose],0)
    newObject.SetPosition((mouseInput[0],mouseInput[1]-50))
    alliesList.append(newObject)


activeUnit = None
def SetInput(mouseInput,click):
    global activeUnit,alliesList
    global isMoving#유닛 뽑은 상태가 아닌 유닛 선택후 이동 상태인지
    if(click):
        if(mouseInput < [320, 550] and mouseInput[0] > 280 and mouseInput[1] > 520):
            Recruit(mouseInput)
        else:
            for unit in alliesList:
                unitPosition = unit.GetPosition()
                if(unitPosition[0]>mouseInput[0]-10 and unitPosition[1]>mouseInput[1]-15 and unitPosition[0]<mouseInput[0]+10 and unitPosition[1]<mouseInput[1]+15):
                    activeUnit = unit
                    break
            if(activeUnit != None):
                activeUnit.Input(mouseInput)

def Update():
    global enemyList, alliesList, timePass, current_time,elapsedTime
    global wallHp
    elapsedTime = get_time()-current_time
    timePass = timePass +elapsedTime
    if(timePass>1):
        SpawnEnemy()
        timePass = 0

    for enemy in enemyList:
        enemy.update(elapsedTime)
        current_pos = enemy.GetPosition()
        if(current_pos[1]>380):#벽에 가까이 오면 성벽 체력 달기
            #wallHp = wallHp - (enemy.hp*elapsedTime)
            pass
    for allies in alliesList:
        allies.update(elapsedTime,enemyList)
    current_time+=elapsedTime