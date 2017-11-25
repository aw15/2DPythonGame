from pico2d import *

import game_framework
from EffectManager import *
from ObjectManager import *





name = "mainState"

effectManager = None
objectManager = None

def create_world():
    global effectManager, objectManager
    effectManager = Effect()
    pass


def destroy_world():
    global effectManager,objectManager
    del(effectManager)
    pass



def enter():
    open_canvas()
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





def update(frame_time):
    global effectManager,objectManager
    pass


def draw(frame_time):
    clear_canvas()
    global effectManager,objectManager
    effectManager.Draw(frame_time)
    effectManager.Update(frame_time)
    pass

    update_canvas()






