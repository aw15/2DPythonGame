from pico2d import *
import Object
import utility
import time

mouseInput = [0,0]
isClick = False
isMotion =False
#InputEvent
def handle_events():
    global mouseInput, isClick, isMotion
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            pass
        elif event.type==SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            pass
        elif event.type==SDL_MOUSEMOTION:
            isMotion = True
            #print('motion')
        elif event.type == SDL_MOUSEBUTTONDOWN:
            isClick = True
           # print('click')
            mouseInput[0] = event.x
            mouseInput[1] = 600 - event.y




open_canvas()

image = load_image('resource\grass.png')
wall_image = load_image('resource\wall.png')

#unit initialize---------------------------------------------------------
unitList = []
for i in range(1,42):
    filename = '\c' + str(i)+'.png'
    unitList.append(r'resource\character\unit' + filename)
#------------------------------------------------------------------------
spawnPoint = [(20,100),(20,300),(20,500),(20,700)]

enemies =[]
timePass=0
#0 = UP 1 = DOWN 2=RIGHT 3= LEFT---------mainloop
while(True):
    clear_canvas()
    for i in range(0,8):
        for j in range(0,6):
            image.draw(50+i*100,50+j*100)
    for i in range(0,6):
        wall_image.draw(500,50+i*100)
    handle_events()

    timePass = timePass + utility.timeTick()
    if timePass>1:
        timePass=0
        newObject = Object.Object(unitList[3])
        newObject.SetDirection([32, 96], [32, 32], [32, 64], [32, 0], [32, 32])
        newObject.SetMaxIndex(1)
        newObject.SetPosition(spawnPoint[0][0],spawnPoint[0][1])
        newObject.SetMoving((300,300))
        enemies.append(newObject)
    for enemy in enemies:
        enemy.update(1)

    delay(0.08)
    update_canvas()
close_canvas()


