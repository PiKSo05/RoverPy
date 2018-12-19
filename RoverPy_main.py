import keyboard

from RoverPy_KeyBoardControl import KeyBoardControl

keyBoardControl = KeyBoardControl()

keyboard.on_press(keyBoardControl.keyInput)
keyboard.wait('esc')
