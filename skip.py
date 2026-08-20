import pyautogui
import time

# List of all images you want to detect
image_list = ['s2.png' ]  # Add as many as you want

while True:
    try:
        found = False
        
        for img in image_list:
            # Try to locate current image
            location = pyautogui.locateOnScreen(img, confidence=0.7)
            
            if location:
                x, y = pyautogui.center(location)
                pyautogui.moveTo(x, y, duration=0.25)
                pyautogui.click()
                
                print(f"Found & clicked on: {img} at ({x}, {y})")
                found = True
                break  # Stop searching other images this loop
        
        if not found:
            print("None of the images were found.")
    
    except Exception as e:
        print(f"Error: {str(e)}")
    
    time.sleep(1)
