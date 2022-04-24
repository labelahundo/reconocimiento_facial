import os
import numpy as np
import cv2 as ocv

ruta = "C:\\Users\\GAME\\Desktop\\imagen"
peoplelist = os.listdir(ruta)
#print(cara)

labels =[]
facesdata= []
label = 0

for namedir in peoplelist:
    personpath = ruta + "\\" + namedir
    #print ("leyendo imagenes" ) 

    for filename in os.listdir(personpath):
        print(namedir + "\\" + filename)
        labels.append(label)
        facesdata.append(ocv.imread(personpath + "\\" + filename,0))
        leer = ocv.imread(personpath + "\\" + filename,0)
        
        ocv.imshow("asd", leer)
        ocv.waitKey(10)
    label = label + 1

print(facesdata)
print(labels)
recognizer=ocv.face.EigenFaceRecognizer_create()

print("entrenando")
recognizer.train(facesdata, np.array(labels))
recognizer.write('cara.xml')
ocv.destroyAllWindows()
