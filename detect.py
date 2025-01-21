import cv2
import pyautogui
import numpy as np
import time

def capture_screen_region(x, y, width=100, height=100):
    screenshot = pyautogui.screenshot(region=(x - width // 2, y - height // 2, width, height))
    frame = np.array(screenshot)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)  
    return frame

def detect_green(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_green = np.array([35, 50, 50])  
    upper_green = np.array([85, 255, 255]) 

    mask = cv2.inRange(hsv, lower_green, upper_green)
    green_pixels = cv2.countNonZero(mask)
    
    return green_pixels > 50 

def left_click():
    pyautogui.click()

print("Move cursor near green objects...")

detected = False  

try:
    while True:
        x, y = pyautogui.position()  
        frame = capture_screen_region(x, y)
        
        if detect_green(frame):
            if not detected:  
                print("Green detected! Clicking...")
                left_click()
                detected = True  
        else:
            detected = False 

        time.sleep(0.1) 

except KeyboardInterrupt:
    print("\nProgram exited.")
