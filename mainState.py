from pico2d import *

import game_framework


from boy import Boy # import Boy class from boy.py
from ball import Ball, BigBall
from grass import Grass
from Brick import  Brick


name = "collision"

boy = None
balls = None
big_balls = None
grass = None
brick = None

def create_world():
    global boy, grass, balls, big_balls
    global boy,grass,balls,brick
    boy = Boy()
    big_balls = [BigBall() for i in range(10)]
    balls = [Ball()for i in range(10)]
    balls = big_balls+balls
    grass = Grass()
    brick = Brick()
    pass


def destroy_world():
    global boy, grass, balls, big_balls,brick

    del(boy)
    del(balls)
    del(grass)
    del(big_balls)
    del(brick)



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
            else:
                boy.handle_event(event)



def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b : return False
    if right_a<left_b:return False
    if top_a<bottom_b:return False
    if bottom_a > top_b:return False

    return True
    pass

stopBall = set()
def update(frame_time):
    boy.update(frame_time)
    brickPos =brick.update(frame_time)
    if collide(brick,boy):
        boy.Stop()
    else:
        boy.falling()
    for ball in balls:
        ball.update(frame_time)
    for ball in balls:
        if collide(brick,ball):
            ball.stop()
    for ball in big_balls:
        if collide(grass,ball):
            ball.stop()
        if collide(brick,ball):
            ball.stop()
            stopBall.add(ball)

    for ball in stopBall:
        ball.Move(brickPos)

    print(stopBall)
    print()


def draw(frame_time):
    clear_canvas()
    grass.draw()
    boy.draw()
    for ball in balls:
        ball.draw()
    brick.draw()
    # fill here
    pass

    update_canvas()






