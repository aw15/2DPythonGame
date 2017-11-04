from pico2d import *
import Spawner

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

alliesList = []
enemyList = []

building_big = load_image(r'resource\map\big.png')
building_small1 = load_image(r'resource\map\small1.png')
building_small2 = load_image(r'resource\map\small2.png')
building_medium = load_image(r'resource\map\medium.png')
building_wall_height = load_image(r'resource\map\wall_height.png')
building_wall_width = load_image(r'resource\map\wall_width.png')
for i in range(1,11):
    filename = '\c'+str(i)+'-'
    temp1 = load_image(r'resource\character\allies'+filename+'1.gif')
    temp2 = load_image(r'resource\character\allies'+filename+'2.gif')
    temp3 = load_image(r'resource\character\allies'+filename+'3.gif')
    temp4 = load_image(r'resource\character\allies'+filename+'4.gif')
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
    # for i in range(0,8):
    #     for j in range(0,6):
    #         image.draw(50+i*100,50+j*100)
    # for i in range(0,6):
    #     wall_image.draw(500,50+i*100)
    handle_events()
    building_small1.draw(200,200)
    building_big.draw(300, 300)
    Spawner.SpawnEnemy()
    delay(0.1)
    update_canvas()
close_canvas()


