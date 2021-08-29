import cv2
import numpy as np
width = 300
height = 200
img = cv2.imread("/home/uruk380/UTC_UBUNTU/Learn_OpenV/Ressources/lambo.png")
print(img.shape) # (height, width, chanel) with chanel = BGR

imgResize = cv2.resize(img,(width,height)) # (w,h)

imgCropped = img[0:200,200:500]

cv2.imshow("Image original",img)
cv2.imshow("Image Resize",imgResize)
cv2.imshow("Image Cropped",imgCropped)


cv2.waitKey(0)