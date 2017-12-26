
import platform
import os

os.environ["PYSDL2_DLL_PATH"] = "./dll/x64"


import game_framework
import start_state
import mainState
from pico2d import *

open_canvas(800,600)
game_framework.run(start_state)
close_canvas()
