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
    global timePass,five , attackPoint, spawnPoint, enemyImageList, alliesImageList, enemyList, alliesList
    print(enemyImageList[1])
    elapsedTime = utility.timeTick()
    timePass = timePass +elapsedTime
    #if timePass > 2:
    if five<5:
        five= five+1
        timePass = 0
        newObject = Object.Object(ENEMY)
        newObject.SetSprite(enemyImageList[4],1)
        index = random.randint(0,3)
        newObject.SetPosition(spawnPoint[index])
        enemyList.append(newObject)

    for enemy in enemyList:
        enemy.FindNearPoint(attackPoint)
        enemy.update(elapsedTime*0.1)