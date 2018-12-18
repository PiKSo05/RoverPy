import keyboard

#keyboard.press_and_release('shift+s, space')
#recorded = keyboard.record(until='esc')
#keyboard.play(recorded, speed_factor=3)
#keyboard.wait('esc')
#print 'esc'

def printEvent(event):
	print event.name

#keyboard.hook(printEvent)
keyboard.on_press(printEvent)

keyboard.wait('esc')
