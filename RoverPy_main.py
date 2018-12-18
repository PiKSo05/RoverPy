import keyboard
from RoverPy_command import RoverPyCommand

rover = RoverPyCommand()

keyboard.on_press(rover.keyInput)
keyboard.wait('esc')
