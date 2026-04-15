import pyautogui
import time


n = int(input("Enter a number : "))

time.sleep(5)


for i in range(1, n + 1):
    
    
    ch = "#" * (2 * i - 1)
    
    
    pyautogui.typewrite(ch)
    
    
    pyautogui.press('enter')




