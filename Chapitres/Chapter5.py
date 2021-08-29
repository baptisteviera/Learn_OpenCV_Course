import cv2
import numpy as np
img = cv2.imread("/home/uruk380/UTC_UBUNTU/Learn_OpenCV/Ressources/cards.jpg")
width, height = 250, 350
# points of the part of the image we want to select (obtained with gimp)
points1 = np.float32([[110,218],[286,187],[153,481],[351,439]])
# points of the final image output which correspond with the points of the old image
points2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(points1,points2)
imgResult = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("ImgResult",imgResult)
cv2.waitKey(0)