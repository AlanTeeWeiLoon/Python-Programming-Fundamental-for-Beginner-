import pyautogui

print('\n1----------------------------------------\n')
# pyautosize.size() - the size of screen

print(pyautogui.size()) # Size(width=1920, height=1080)

width, height = pyautogui.size()
print(width) # 1920
print(height) # 1080

print('\n2----------------------------------------\n')
# pyautogui.position()

print(pyautogui.position()) # the position of the current mouse

print('\n3----------------------------------------\n')
# pyautogui.moveTo() - move your mouse with Python

#pyautogui.moveTo(10, 10) # mouse will move to the top left of the screen
#pyautogui.moveTo(10, 1000, duration = 1.5) # mouse will move to the bottom left of the screen in 1.5 second

print('\n4----------------------------------------\n')
# pyautogui.moveRel() - (xOffset = 0, yOffset = 0, duration = 0.0)

#pyautogui.moveRel(200, 0) # mouse will move to the right 200 pixels
#pyautogui.moveRel(200, 0, duration =  2) # mouse will move to the right 200 pixels in 2 seconds
#pyautogui.moveRel(0, -100, duration =  2) # mouse will move up 100 pixels in 2 seconds

print('\n5----------------------------------------\n')
# pyautogui.click() - mouse will click according to the position
# pyautogui.doubleclick() - mouse will doubleclick according to the position
# pyautogui.rightclick() - mouse will right click according to the position
# pyautogui.middleclick() - mouse will middle click according to the position

print(pyautogui.position()) # Point(x=1343, y=57) - position of the 'Help'
#pyautogui.click(1343, 57) # mouse will move to the position and click the 'Help'

print('\n6----------------------------------------\n')
# move the mouse to the top left corner to terminate every pyautogui


print('\n7----------------------------------------\n')
# pyautogui.dragTo()
# pyautogui.dragRel()

#pyautogui.dragTo(10,10) # drag the mouse to the position
#pyautogui.dragRel(10,10)
































