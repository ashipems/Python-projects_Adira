import cv2
import numpy as np
import pyautogui
from win32api import GetSystemMetrics
import time

w = GetSystemMetrics(0)
h = GetSystemMetrics(1)
dimension = (w, h)
fourcc = cv2.VideoWriter_fourcc(*"XVID")
output = cv2.VideoWriter("recording.mp4", fourcc, 20.0, dimension)
now = time.time()
duration = int(input('Specify recording duration in seconds: '))
duration += duration
end_time = now + 1.5*duration

while True:
    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output.write(frame)
    current_time = time.time()
    if current_time>end_time:
        break

output.release()
