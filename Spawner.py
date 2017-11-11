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


timePass=0
five = False

def SetUnitList(allies, enemy):
    global enemyImageList, alliesImageList
    enemyImageList = enemy
    alliesImageList = allies

enemyList = []
alliesList = []

def SpawnEnemy():
    global  enemyImageList, enemyList
    choose = random.randint(0,7)
    newObject = Object.Object(ENEMY)
    newObject.SetSprite(enemyImageList[choose],1)
    x = random.randint(20,750)
    newObject.SetPosition([x,-20])
    enemyList.append(newObject)


activeUnit=[]

def Recruit(mouseInput):
    global alliesImageList,  alliesList, activeUnit
    choose = random.randint(0,9)
    newObject = Object.Object(ALLIES)
    newObject.SetSprite(alliesImageList[choose], 1)
    newObject.SetPosition(mouseInput)
    activeUnit.append(newObject)
    alliesList.append(newObject)
current_time = get_time()
elapsedTime = None


g_mouseInput = None
isClick = None


def SetInput(mouseInput,click):
    global g_mouseInput, isClick,alliesList
    g_mouseInput = mouseInput
    if(click):
        if (mouseInput < [320, 570] and mouseInput[0] > 280 and mouseInput[1] > 520):
            print(mouseInput)
            Recruit(mouseInput)
        else:
            for unit in alliesList:
                unitPosition = unit.GetPosition()
                if(unitPosition[0]>mouseInput[0]-10 and unitPosition[1]>mouseInput[1]-15 and unitPosition[0]<mouseInput[0]+10 and unitPosition[1]<mouseInput[1]+15):
                    activeUnit.clear()
                    activeUnit.append(unit)
                    print(unitPosition[0] , unitPosition[1])
                    print(mouseInput[0]-10,mouseInput[1]+10)
                    print(mouseInput[1] - 15, mouseInput[1] + 15)
            for unit in activeUnit:
                unit.AlliesMove(mouseInput)


def Update():
    global enemyList, alliesList, timePass, current_time,elapsedTime
    global g_mouseInput,isClick
    elapsedTime = get_time()-current_time
    timePass = timePass +elapsedTime
    if(timePass>1):
        SpawnEnemy()
        timePass = 0




    for enemy in enemyList:
        enemy.Move()
        enemy.update(elapsedTime)
    for allies in alliesList:
        allies.update(elapsedTime)

    current_time+=elapsedTime