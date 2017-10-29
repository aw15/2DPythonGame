from pico2d import *
import Object

open_canvas()

image = load_image('resource\grass.png')
wall_image = load_image('resource\wall.png')
charator_image = load_image('resource\character\MainGuy.png')

#boy
boy1 = Object.Object('resource\character\MainGuy.png')
boy1.SetDirection([41,36],[41,108],[41,0],[43,72],[38,36])
boy1.SetPosition(100,100)
boy1.SetMaxIndex(2)
#2단계---------------------------------------------------
boy2 = Object.Object('resource\character\george.png')
boy2.SetDirection([96,48],[0,48],[144,48],[48,48],[48,48])
boy2.SetPosition(100,100)
boy2.SetMaxIndex(3,False)
#Unit Initailize, SetDirection(up,down,right, left, increase)
# Albert = Object.Object(r'resource\character\unit\Albert.png')
# Albert.SetDirection([16,48],[16,16],[16,32],[16,0],[16,16])
# Albert.SetPosition(100,100)
# Albert.SetMaxIndex(1)
#---------------------------------------------------------
unitList = []
for i in range(1,42):
    filename = '\c' + str(i)+'.png'
    newObject = Object.Object(r'resource\character\unit' + filename)
    newObject.SetDirection([16,48],[16,16],[16,32],[16,0],[16,16])
    newObject.SetPosition(100,100)
    newObject.SetMaxIndex(1)
    unitList.append(newObject)


g_index=0
#0 = UP 1 = DOWN 2=RIGHT 3= LEFT
while(True):
    clear_canvas()
    for i in range(0,8):
        for j in range(0,6):
            image.draw(50+i*100,50+j*100)
    for i in range(0,6):
        wall_image.draw(500,50+i*100)
    # Albert.SetPosition(100+g_index, 100)
    unitList[35].update(2)

    # charator_image.clip_draw(g_index*41,108,41,36,100,100)
    g_index = g_index+3
    # if g_index>2:
    #     g_index=0
    delay(0.08)
    update_canvas()
close_canvas()
