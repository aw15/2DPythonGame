from pico2d import *
from Object import *

open_canvas()

image = load_image('resource\grass.png')
wall_image = load_image('resource\wall.png')
charator_image = load_image('resource\charactor\MainGuy.png')

Object:Object

while(True):
    clear_canvas()
    for i in range(0,8):
        for j in range(0,6):
            image.draw(50+i*100,50+j*100)
    for i in range(0,6):
        wall_image.draw(500,50+i*100)


    charator_image.clip_draw(g_index*41,36,41,36,100,100)

    delay(0.2)
    update_canvas()
close_canvas()
