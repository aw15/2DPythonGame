import game_framework
from pico2d import *
import start_state

name = "TitleState"
winImage = None
winMusic = None

def enter():
    global winImage,winMusic
    winImage = load_image('resource/titleImage/trophy.png')
    winMusic = load_music('resource/music/win.mp3')
    winMusic.set_volume(100)
    winMusic.repeat_play()

def exit():
    global winImage,winMusic
    del(winImage)
    del(winMusic)

def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.push_state(start_state)

def draw(frame_time):
    clear_canvas()
    winImage.draw(400,300)
    update_canvas()







def update(frame_time):
    pass


def pause():
    pass


def resume():
    pass
