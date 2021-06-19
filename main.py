from PIL import ImageGrab #python image library
import numpy as np
import cv2
from win32api import GetSystemMetrics
width=GetSystemMetrics(0)
height=GetSystemMetrics(1)

fourcc=cv2.VideoWriter.fourcc('1','2','3','4')
captures=cv2.VideoWriter('code',fourcc,20.0,(width,height))
while True:
    image = ImageGrab.grab(bbox=(0, 0, width,height))
    image_n = np.array(image)
    image_c=cv2.cvtColor(image_n,cv2.COLOR_BGR2RGB)
    captures.write(image_c)
    cv2.imshow('capture',image_c)

    if cv2.waitKey(10)==ord('s'):
        break


