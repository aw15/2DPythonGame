import Object
import utility
import random
from pico2d import *


BUILDING=0
ENEMY=1
ALLIES=2

#unit initialize---------------------------------------------------------

enemyImageList =[]
alliesImageList =[]
wallHp = 10000
alliesAttackPoint = 5
enemyAttackPoint =10


timePass=0
five = False

def SetUnitList(allies, enemy):
    global enemyImageList, alliesImageList
    enemyImageList = enemy
    alliesImageList = allies

enemyList = []
alliesList = []

def SpawnEnemy():
    global  enemyImageList, enemyList,enemyAttackPoint
    choose = random.randint(0,7)
    newObject = Object.Object(ENEMY,(choose+1)*enemyAttackPoint)
    newObject.SetSprite(enemyImageList[choose],1)
    x = random.randint(20,750)
    newObject.SetPosition([x,-20])
    enemyList.append(newObject)



def Recruit(mouseInput):
    global alliesImageList,  alliesList, alliesAttackPoint,isMoving
    choose = random.randint(0,9)
    newObject = Object.Object(ALLIES,(choose+1)*alliesAttackPoint)
    newObject.SetSprite(alliesImageList[choose], 1)
    newObject.SetPosition(mouseInput)
    alliesList.append(newObject)
    return newObject

current_time = get_time()
elapsedTime = None

isMoving =False
activeUnitList = []

def SetInput(mouseInput,click,space):
    global activeUnitList,alliesList
    global isMoving#유닛 뽑은 상태가 아닌 유닛 선택후 이동 상태인지


    if(click):
        if(mouseInput < [320, 570] and mouseInput[0] > 280 and mouseInput[1] > 520):
            Recruit(mouseInput)
        else:
            for unit in alliesList:
                unitPosition = unit.GetPosition()
                if(unitPosition[0]>mouseInput[0]-10 and unitPosition[1]>mouseInput[1]-15 and unitPosition[0]<mouseInput[0]+10 and unitPosition[1]<mouseInput[1]+15):
                    activeUnitList.append(unit)
                    break
        print(activeUnitList)
        for unit in activeUnitList:
            unit.SetMouseInput(mouseInput)


def Update():
    global enemyList, alliesList, timePass, current_time,elapsedTime
    global wallHp
    elapsedTime = get_time()-current_time
    timePass = timePass +elapsedTime
    if(timePass>1):
        SpawnEnemy()
        timePass = 0
    for enemy in enemyList:
        enemy.Move()
        enemy.update(elapsedTime)
        current_pos = enemy.GetPosition()
        if(current_pos[1]>380):#벽에 가까이 오면 성벽 체력 달기
            wallHp = wallHp - (enemy.hp*elapsedTime)
    for allies in alliesList:
        allies.AlliesMove()
        allies.update(elapsedTime)

    current_time+=elapsedTime