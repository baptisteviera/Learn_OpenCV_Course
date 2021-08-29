import cv2

print("package imported")


# attention il faut mettre le chenmin absolu (linux)
def readImg():
    img = cv2.imread("/home/uruk380/UTC_UBUNTU/Learn_OpenV/Ressources/lena.png")
    cv2.imshow("MyOutput", img)
    cv2.waitKey(0)


def readVideo():
    width = 640
    height = 480
    video = cv2.VideoCapture("/home/uruk380/UTC_UBUNTU/Learn_OpenV/Ressources/v1_Notions d'objet et de classe.mp4")
    while True:
        success, img = video.read()
        img = cv2.resize(img,(width,height))
        cv2.imshow("MyVideoOutput", img)
        if cv2.waitKey(1) and 0xFF == ord('q'):
            break


def readWebcam():
    width = 640
    height = 480
    webcam = cv2.VideoCapture(0)
    webcam.set(3, width)  # width
    webcam.set(4, height)  # height
    webcam.set(10, 100)  # camera brightness
    while True:
        success, img = webcam.read()
        cv2.imshow("MyVideoOutput", img)
        if cv2.waitKey(1) and 0xFF == ord('q'):
            break

# readImg()
# readVideo()
# readWebcam()
