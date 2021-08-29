import cv2
import numpy as np

def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

def getContours(img):
    # attention importance de mettre une image de type Canny
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area>500:
            # on travaille ici sur imgContour imgContour !!!!
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3) # -1 car nous voulons tout le contour de l'image
            # (255,0,0) correspond à la couleur de l'image (bleue)
            # thickness = 3
            # on récupère la longueur de tous les contours de l'arc
            # True car les contours sont pleins
            peri = cv2.arcLength(cnt,True)
            #print(peri)
            resolution = 0.02 * peri
            approx = cv2.approxPolyDP(cnt,resolution,True)
            print(len(approx)) # approx contient les cordonnées des points de la forme en question
            # le nombre de point nous renseigne sur le type de forme (triangle, carré, rectangle...)
            # au dessus de 4 on considère qu'il s'agit d'un cercle.
            objCor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)

            # on catégorise nos objets
            if objCor ==3:
                objectType ="Tri"
            elif objCor == 4:
                aspRatio = w/float(h)
                # deviation de 2 / 3 %
                if aspRatio >0.98 and aspRatio <1.03: objectType= "Square"
                else:objectType="Rectangle"
            elif objCor>4: objectType= "Circles"
            else:objectType="None"


            # point 1 = x,y
            # point 2 = x+w,y+h
            # couleur : (0,255,0)
            # epaisseur : 2
            center_objet1 = x+(w//2)
            center_objet2 = y+(h//2)
            deviation = 10
            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,0,0),2)
            cv2.putText(imgContour,objectType,
                        (center_objet1-deviation,center_objet2-deviation),cv2.FONT_HERSHEY_COMPLEX,0.7,
                        (0,0,0),2)




path = '/home/uruk380/UTC_UBUNTU/My_Own_Project/Learn_OpenCV/Ressources/shapes.png'
img = cv2.imread(path)
imgContour = img.copy()
# pour pas travailler sur l'image de base

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
imgCanny = cv2.Canny(imgBlur,50,50)
getContours(imgCanny)

imgBlank = np.zeros_like(img)
imgStack = stackImages(0.8,([img,imgGray,imgBlur],
                            [imgCanny,imgContour,imgBlank]))

cv2.imshow("Stack", imgStack)

cv2.waitKey(0)