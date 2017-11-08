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
    newObject.SetPosition([x,30])
    enemyList.append(newObject)

def Recruit(mouseInput):
    global alliesImageList,  alliesList
    choose = random.randint(0,9)
    newObject = Object.Object(ALLIES)
    newObject.SetSprite(alliesImageList[choose], 1)
    newObject.SetPosition(mouseInput)
    alliesList.append(newObject)
current_time = get_time()


def Update():
    global enemyList, alliesList, timePass, current_time
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