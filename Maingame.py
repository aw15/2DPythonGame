﻿from pico2d import *
import Spawner

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
            Spawner.SetInput(mouseInput, isClick)
        elif event.type ==SDL_KEYDOWN and event.key ==SDLK_SPACE:
            pass
gold = 0
stage =1
font = load_font('resource\HMKMMAG.ttf',20)
def SetText():
    global  stage,gold
    font.draw(550, 580, '스테이지: %d' %stage, (1, 1, 1))
    font.draw(700, 580, '골드: %d G' %gold, (255, 255, 0))




fireEffect = load_image(r'resource\effect\fire.png')
explosion = load_image(r'resource\effect\e3.png')
def FireEffect():
    global effectIndex,fireEffect
    fireEffect.clip_draw(0, 128*effectIndex, 128, 128, 300, 300)
    effectIndex= (effectIndex+1)%8
def Explosion():
    global explosion
    explosion.clip_draw(0,92,90,92,300,300)
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

for i in range(1,11):
    filename = '\c'+str(i)+'-'
    temp1 = load_image(r'resource\character\allies'+filename+'1.png')
    temp2 = load_image(r'resource\character\allies'+filename+'2.png')
    temp3 = load_image(r'resource\character\allies'+filename+'3.png')
    temp4 = load_image(r'resource\character\allies'+filename+'4.png')
    alliesList.append([temp1,temp2,temp3,temp4])

for i in range(1,9):
    filename = '\e'+str(i)+'-'
    temp1 = load_image(r'resource\character\enemy'+filename+'1.png')
    temp2 = load_image(r'resource\character\enemy'+filename+'2.png')
    temp3 = load_image(r'resource\character\enemy'+filename+'3.png')
    temp4 = load_image(r'resource\character\enemy'+filename+'4.png')
    enemyList.append([temp1,temp2,temp3,temp4])

Spawner.SetUnitList(alliesList, enemyList)#유닛 리스트 설정

#0 = UP 1 = DOWN 2=RIGHT 3= LEFT---------mainloop
while(True):
    clear_canvas()
    handle_events()
    draw_rectangle(mouseInput[0] - 10, mouseInput[1] - 15, mouseInput[0] + 10, mouseInput[1] + 15)
    SetEnviroment()
    SetText()
    Spawner.Update()
    update_canvas()

    isClick =False
close_canvas()

