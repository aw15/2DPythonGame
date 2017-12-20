
import platform
import os

os.environ["PYSDL2_DLL_PATH"] = "./dll/x64"


import game_framework
import mainState

game_framework.run(mainState)
