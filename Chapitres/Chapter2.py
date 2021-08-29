import cv2
import numpy as np
img = cv2.imread("/home/uruk380/UTC_UBUNTU/Learn_OpenV/Ressources/lena.png")

kernel = np.ones((5,5),np.uint8)

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0) # ksize only odd number
imgCanny = cv2.Canny(img,150,200)
imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)
# work with a dialation img
imgErode = cv2.erode(imgDialation,kernel,iterations=1)

cv2.imshow("Gray img",imgGray)
cv2.imshow("Blur img",imgBlur)
cv2.imshow("Canny img",imgCanny)
cv2.imshow("Dialation img",imgDialation)
cv2.imshow("Erode img",imgErode)


cv2.waitKey(0)

