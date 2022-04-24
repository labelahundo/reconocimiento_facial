import cv2 as ocv
import imutils as muti
import os

nombre = input("nombre de carpeta a crear y/o llenar")
imagen = input("numero de imagen")
#path = "C:\\Users\\GAME\\Desktop\\captura de caras\\asd\\"
camera = ocv.VideoCapture(0)
detect = ocv.CascadeClassifier(ocv.data.haarcascades + 'haarcascade_frontalface_default.xml')
contador = int(imagen)
path = "C:\\Users\\GAME\\Desktop\\imagen\\" + nombre + "\\"
texto ="C:\\Users\\GAME\\Desktop\\imagen\\"

while True:
    so,img= camera.read()
    if so == False:
        break
    img = muti.resize(img, width = 640)
    gris = ocv.cvtColor(img, ocv.COLOR_BGR2GRAY)
    aux = img.copy()

    cara = detect.detectMultiScale(gris,
                    scaleFactor = 1.3,
                    minNeighbors = 6,
                    minSize = (30,30),
                    maxSize = (200,200))
    for (x,y,w,h) in cara :
        if not os.path.exists(path):
            os.makedirs(path)
        ocv.rectangle(img, (x,y), (x+w ,y+h), (0,250,0), 2)
        rostro = aux[y:y+h, x:x+w]
        rostro = ocv.resize(rostro, (150, 150), interpolation = ocv.INTER_CUBIC)
        ocv.imwrite(path + "CAR_%04d.jpg" % contador, rostro)
        listo = ocv.waitKey(1) & 0xFF == ord('q')
        if listo == True or contador >= 350 :
            break
        print (contador)
        contador += 1
    ocv.imshow("asd",img)
    #ocv.imshow("magia", rostro)
    if ocv.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
ocv.destroyAllWindows()