from pico2d import *
import Object

mouseInput = [0,0]
isClick = False
#InputEvent
def handle_events():
    global mouseInput, isClick
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            pass
        elif event.type == SDL_MOUSEBUTTONDOWN:
            isClick = True
            mouseInput[0] = event.x
            mouseInput[1] = 600 - event.y
        elif event.type==SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            pass




open_canvas()

image = load_image('resource\grass.png')
wall_image = load_image('resource\wall.png')

#unit initialize---------------------------------------------------------
unitList = []
for i in range(1,42):
    filename = '\c' + str(i)+'.png'
    newObject = Object.Object(r'resource\character\unit' + filename)
    newObject.SetDirection([32,96],[32,32],[32,64],[32,0],[32,32])
    newObject.SetPosition(100,100)
    newObject.SetMaxIndex(1)
    unitList.append(newObject)
#------------------------------------------------------------------------

#0 = UP 1 = DOWN 2=RIGHT 3= LEFT---------mainloop
while(True):
    clear_canvas()
    for i in range(0,8):
        for j in range(0,6):
            image.draw(50+i*100,50+j*100)
    for i in range(0,6):
        wall_image.draw(500,50+i*100)
    handle_events()
    if(isClick):
        unitList[3].SetMoving(mouseInput)
    unitList[3].update(1)
    delay(0.08)
    update_canvas()
close_canvas()


