import Object
import utility
import random

#unit initialize---------------------------------------------------------
unitList = []
for i in range(1,42):
    filename = '\c' + str(i)+'.png'
    unitList.append(r'resource\character\unit' + filename)
#------------------------------------------------------------------------


enemyList =[]
timePass=0
once = True
def SpawnEnemy(spawnPoint,attackPoint):
    global timePass,once
    timePass = timePass + utility.timeTick()
    if once:#timePass > 1000:
        timePass = 0
        newObject = Object.Enemy(unitList[3])
        newObject.SetDirection([32, 96], [32, 32], [32, 64], [32, 0], [32, 32])
        newObject.SetMaxIndex(1)
        index = random.randint(0,3)
        newObject.SetPosition(spawnPoint[index])
        newObject.FindNearPoint(attackPoint)
        enemyList.append(newObject)
        once = False

    for enemy in enemyList:
        enemy.update(utility.timeTick()*10)