#AutoText Bot
#After clicking the run button immediately switch to the prom
# where you want to sent the txt   
import pyautogui
import time

while True:
    time.sleep(5)
    pyautogui.typewrite("Hello Love! I Love you")
    time.sleep(2)
    pyautogui.press("Enter")