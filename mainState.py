from pico2d import *

import game_framework
from ObjectManager import *
from World import *




name = "mainState"

objectManager = None
world = None

def create_world():
    global world, objectManager
    world = World()
    objectManager = ObjectManager()

    pass


def destroy_world():
    global world ,objectManager
    del(objectManager)
    del(world)
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


def draw(frame_time):
    global world, objectManager
    clear_canvas()
    world.Draw(objectManager.stage)
    objectManager.Draw(frame_time)


    update_canvas()






