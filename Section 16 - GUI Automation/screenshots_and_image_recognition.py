import pyautogui

print('\n1------------------------------------------\n')
# pyautogui.screenshot()

print(pyautogui.screenshot()) # <PIL.Image.Image image mode=RGB size=1920x1080 at 0x3432C90>

pyautogui.screenshot('screenshot_example.jpg') # the screenshot image had saved

print('\n2------------------------------------------\n')
# pyautogui.locateOnScreen()  

a = pyautogui.locateOnScreen('chrome_icon.png')
print(a) # print the location of the screen that the chrome icon located

print('\n3------------------------------------------\n')
# pyautogui.locateCenterOnScreen()

pyautogui.locateCenterOnScreen('chrome_icon.png') # set the chrome icon location as center
#pyautogui.click(location of the chrome icon location)


# To Recap:
# A screenshot is an image of the screen's content.
# The pyautogui.screenshot() will return an Image object of the screen, or you can pass it a filename to save it to a file
# locateOnScreen() is passed a sample image file, and returns the coordinates of where it is on the screen.
# locateCenterOnScreen() will return an (x, y) tuple of where the image is on the screen.
# Combining the keyboard/mouse/screenshot functions lets you make awesome stuff!





