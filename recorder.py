
import cv2
import numpy as np
import pyautogui
def recordery():
    SCREEN_SIZE = (1920, 1080)
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter("output.avi", fourcc, 20.0, (SCREEN_SIZE))
    while True:
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        out.write(frame)
        # if the user clicks q, it exitsq
        if cv2.waitKey(1) & 0xFF == "q":
            return 'done'
    cv2.destroyAllWindows()
    out.release()

chs = input("Enter any value to start recording")
chs = recordery()
print(chs)
