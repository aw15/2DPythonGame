from pico2d import *

import game_framework
from ObjectManager import *
from World import *
from EffectManager import *


name = "mainState"

objectManager = None
effectManager = None
world = None
effectPosition=[]
loseImage = None
winImage = None

winMusic = None
loseMusic = None

def create_world():
    global world, objectManager,effectManager,winImage,loseImage, winMusic, loseMusic
    world = World()
    objectManager = ObjectManager()
    effectManager = Effect()
    winImage = load_image('resource/titleImage/trophy.png')
    loseImage = load_image('resource/titleImage/trophy.png')
    winMusic = load_wav('resource/music/win.wav')
    winMusic.set_volume(100)
    loseMusic = load_wav('resource/music/lose.wav')
    loseMusic.set_volume(100)
    for i in range(0,20):
        effectPosition.append((random.randint(100,700),random.randint(100,500)))
    pass


def destroy_world():
    global world ,objectManager,effectManager, winMusic, loseMusic
    del(objectManager)
    del(world)
    del(effectManager)
    del(winMusic)
    del(loseMusic)
    pass



def enter():
    open_canvas(800,600)
    game_framework.reset_time()
    create_world()


def exit():
    destroy_world()
    close_canvas()


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

    pass

index =0
totalTime =0

def draw(frame_time):
    global world, objectManager, totalTime, effectManager, effectPosition
    clear_canvas()
    world.Draw(objectManager.stage)
    objectManager.Draw(frame_time)

    if (objectManager.lose):
        for pos in effectPosition:
            effectManager.Draw(pos[0], pos[1], 3)
            effectManager.Update(frame_time * 0.05)
        totalTime+=frame_time
        if(totalTime>3):
            game_framework.pop_state()

    update_canvas()






