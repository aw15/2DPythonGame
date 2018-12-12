from pico2d import *

import game_framework
from ObjectManager import *
from World import *
from EffectManager import *
import start_state
import winState

name = "mainState"

objectManager = None
effectManager = None
world = None

loseImage = None
loseMusic = None
index =0
totalTime =0
effectPosition=[]

def create_world():
    global world, objectManager,effectManager,winImage,loseImage, loseMusic
    world = World()
    objectManager = ObjectManager()
    effectManager = Effect()
    loseImage = load_image('resource/titleImage/lose.png')
    loseMusic = load_wav('resource/music/lose.wav')
    loseMusic.set_volume(100)

    for i in range(0,20):
        effectPosition.append((random.randint(100,700),random.randint(100,500)))
    pass


def destroy_world():
    global world ,objectManager,effectManager,loseMusic,totalTime,index
    del(objectManager)
    del(world)
    del(effectManager)
    del(loseMusic)
    totalTime =0
    index=0
    effectPosition.clear()
    pass



def enter():
    game_framework.reset_time()
    create_world()


def exit():
    destroy_world()



def pause():
    pass


def resume():
    pass


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            else:
                objectManager.handle_events(event)
                pass





def update(frame_time):
    global world,objectManager
    objectManager.Update(frame_time)
    if(objectManager.win):
        game_framework.change_state(winState)
    pass



def draw(frame_time):
    global world, objectManager, totalTime, effectManager, effectPosition,loseMusic,loseImage
    clear_canvas()
    world.Draw(objectManager.stage)
    objectManager.Draw(frame_time)

    if (objectManager.lose):
        for pos in effectPosition:
            effectManager.Draw(pos[0], pos[1], 3)
            effectManager.Update(frame_time * 0.05)
        totalTime+=frame_time
        loseMusic.repeat_play()
        loseImage.draw(400, 300)
        if(totalTime>5):
            game_framework.change_state(start_state)


    update_canvas()






