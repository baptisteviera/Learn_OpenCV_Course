import cv2


faceCascade = cv2.CascadeClassifier("/home/uruk380/UTC_UBUNTU/My_Own_Project/Learn_OpenCV/haarcascades/haarcascade_frontalface_default.xml")
img = cv2.imread("/home/uruk380/UTC_UBUNTU/My_Own_Project/Learn_OpenCV/Ressources/lena.png")
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray,1.1,4)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow("img",img)
cv2.waitKey(0)