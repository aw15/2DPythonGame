
import platform
import os

os.environ["PYSDL2_DLL_PATH"] = "./dll/x64"


import game_framework
import start_state
import mainState

game_framework.run(mainState)
