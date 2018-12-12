import game_framework
from pico2d import *
import mainState

name = "TitleState"
image = None
directionImage = None
select = 1
howTo = False
howToImage = None
music = None

def enter():
    global image,directionImage,howToImage, music
    image = load_image('resource/titleImage/title.png')
    directionImage = load_image('resource/titleImage/direction.png')
    howToImage = load_image('resource/titleImage/howTo.png')
    music = load_music('resource/music/open.mp3')
    music.set_volume(100)
    music.repeat_play()
def exit():
    global image, music
    del(image)
    del(music)
def handle_events(frame_time):
    global select, howTo
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN):
                howTo = False
                if(select==1):
                    select =2
                else:
                    select=1
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
                howTo = False
                if(select==1):
                    select = 2
                else:
                    select = 1
            elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                if(select == 1):
                    game_framework.change_state(mainState)
                else:
                    if(howTo):
                        howTo = False
                    else:
                        howTo = True

def draw(frame_time):
    global select
    clear_canvas()
    if(howTo):
        howToImage.draw(400,300)
    else:
        image.draw(400,300)
        if(select==2):
            directionImage.draw(220,290)
        else:
            directionImage.draw(220, 360)
    update_canvas()







def update(frame_time):
    pass


def pause():
    pass


def resume():
    pass






