import cv2 as ocv
import os

cara = ocv.face.EigenFaceRecognizer_create()
#guardado = ocv.VideoWriter("C:\\Users\\GAME\\Desktop\\neg\\" + "reconocimiento.avi", ocv.VideoWriter_fourcc(*'XVID'), 20.0,(640,480))

cara.read('cara.xml')
#camara = ocv.VideoCapture("C:\\Users\\GAME\\Desktop\\intar\\vid_1.avi")
camara = ocv.VideoCapture(0)
detect = ocv.CascadeClassifier(ocv.data.haarcascades + 'haarcascade_frontalface_default.xml')
while True:
    so,img =camara.read()
    gris = ocv.cvtColor(img,ocv.COLOR_BGR2GRAY)
    aux = gris.copy()

    clasificador = detect.detectMultiScale(gris,
                    scaleFactor = 1.1,
                    minNeighbors = 5, 
                    minSize = (95,95),
                    maxSize = (400,400))
    for (x,y,w,h) in clasificador:
        rostro = aux[y:y+h, x:x+w]
        rostro = ocv.resize(rostro,(150,150), interpolation = ocv.INTER_CUBIC)
        resultado = cara.predict(rostro)
        if resultado[1]<5600 :
            ocv.putText(img, "esteban", (x,y-25),2,1.1,(0,225,0),1,ocv.LINE_AA)
            ocv.rectangle(img,(x,y), (x+w, y+h), (0,250,0),3)
            #if not os.path.exists ("C:\\Users\\GAME\\Desktop\\neg"):
                #os.makedirs("C:\\Users\\GAME\\Desktop\\neg")
        else:
            ocv.putText(img, "desconocido", (x,y-25),2,1.1,(0,0,250),1,ocv.LINE_AA)
            ocv.rectangle(img,(x,y), (x+w, y+h), (0,0,250),3)
        #print("asdasdasdasdasd")
        ocv.putText(img,"{}".format(resultado), (x,y-5),1,1.3,(225,225,0),1,ocv.LINE_AA)
    ocv.imshow("img", img)
    #guardado.write(img)
    if ocv.waitKey(1) & 0xFF == ord('q'):
        break

camara.release()
ocv.destroyAllWindows()


