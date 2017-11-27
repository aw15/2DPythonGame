
from pico2d import *
import ObjectManager
from EffectManager import *


effectManager = Effect()

mouseInput = [0,0]
isClick = False
isMotion =False
effectIndex =0

open_canvas(sync=True)

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
            mouseInput[0] = event.x
            mouseInput[1] = 600 - event.y
            ObjectManager.SetInput(mouseInput, isClick)
        elif event.type ==SDL_KEYDOWN and event.key ==SDLK_SPACE:
            pass



#------------------이펙트 설정 ------------------------------------------------



#Effect.effectManager.SetEffectImage([explosion1,explosion2],[beamHit1,beamHit2,beamHit3], [beam1,beam2,beam3])

#----------------------------------모델 불러오기------------------------------------------------------
alliesList = []
enemyList = []

building_big = load_image(r'resource\map\big.png')
building_small1 = load_image(r'resource\map\small1.png')
building_small2 = load_image(r'resource\map\small2.png')
building_medium = load_image(r'resource\map\medium.png')
building_wall_height = load_image(r'resource\map\wall_height.png')
building_wall_width = load_image(r'resource\map\wall_width.png')

def SetEnviroment():
    building_small1.draw(300, 550)
    for i in range(0,10):
        building_wall_width.draw(134*i,400)



#0 = UP 1 = DOWN 2=RIGHT 3= LEFT---------mainloop
while(True):
    clear_canvas()
    handle_events()
    draw_rectangle(mouseInput[0] - 10, mouseInput[1] - 15, mouseInput[0] + 10, mouseInput[1] + 15)
    SetEnviroment()
    SetText()
    ObjectManager.Update()
    update_canvas()

    isClick =False



close_canvas()


