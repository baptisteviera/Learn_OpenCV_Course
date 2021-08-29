import cv2
import numpy as np

# img = np.zeros((512,512))

# colour functionality (3 chanel)
img = np.zeros((512,512,3),np.uint8)

# img[200:300,100:300] = 255,0,0 # blue form cf same technic as
#img[:] = 255,0,0 # blue window

"""
origine = 0,0
up-to = 300,300
color = green
"""
# width = 300
# height = 300
# cv2.line(img,(0,0),(width,height),(0,255,0),3)
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)
width, height = 250, 300
origine_w, origine_h = 0, 0
color_red = (0,0,255)
thickness = 2
# cv2.rectangle(img,(0,0),(width,height),(0,0,255),thickness)
cv2.rectangle(img,(origine_w,origine_h),(width,height),color_red,cv2.FILLED)
center_point = (400,50)
radius = 30
color_blue = (255,255,0)
thickness2 = 5
cv2.circle(img,center_point,radius,color_blue,thickness2)
position = (300,100)
scale_size = 1
cv2.putText(img," OPEN CV ", position ,cv2.FONT_HERSHEY_SIMPLEX,scale_size,color_red,thickness)

cv2.imshow("Image",img)

print (img.shape)
# result (height,width)

cv2.waitKey(0)