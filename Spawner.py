import Object
import utility
import random

BUILDING=0
ENEMY=1
ALLIES=2

#unit initialize---------------------------------------------------------

enemyImageList =[]
alliesImageList =[]
spawnPoint = [(100,20),(200,20),(500,20),(700,20)]
attackPoint = [(200,200),(300,300),(500,500)]

timePass=0
five = False

def SetUnitList(allies, enemy):
    global enemyImageList, alliesImageList
    enemyImageList = enemy
    alliesImageList = allies

enemyList = []
alliesList = []

def SpawnEnemy():
    global spawnPoint, enemyImageList, enemyList
    choose = random.randint(0,7)
    newObject = Object.Object(ENEMY)
    newObject.SetSprite(enemyImageList[choose],1)
    index = random.randint(0,3)
    newObject.SetPosition(spawnPoint[index])
    enemyList.append(newObject)

def Recruit(mouseInput):
    global spawnPoint, alliesImageList,  alliesList
    choose = random.randint(0,9)
    newObject = Object.Object(ALLIES)
    newObject.SetSprite(alliesImageList[choose], 1)
    index = random.randint(0, 3)
    newObject.SetPosition(mouseInput)
    alliesList.append(newObject)

def Update():
    global enemyList, alliesList,attackPoint, timePass
    elapsedTime = utility.timeTick()
    timePass = timePass +elapsedTime
    if(timePass>100):
        SpawnEnemy()
        timePass = 0
    for enemy in enemyList:
        enemy.FindNearPoint(attackPoint)
        enemy.update(elapsedTime*0.1)
    for allies in alliesList:
        allies.update(elapsedTime*0.1)