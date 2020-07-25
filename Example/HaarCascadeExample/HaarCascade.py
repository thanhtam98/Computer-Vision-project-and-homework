#Iniciando Python
import cv2
import numpy as np
import os

def main():     #Se inicia el Main

    # capWebcam = cv2.VideoCapture(0)
    img = cv2.imread('images.jpg')
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')  #Se cargan los entrenadores de OpenCV para el rostro
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml') #Se Cargan los entrenadores para los ojos
    smile_cascade =  cv2.CascadeClassifier('haarcascade_smile.xml')
    cv2.imshow('saas',img)
    # if capWebcam.isOpened() == False:
    #     print ("Error: No se pudo acceder a la webcam \n\n"  )        #Si no se manda error
    #     os.system("pause")                                          #Se detiene hasta que el usuario pulse una tecla
    #     return                                                      # Se sale del main

    while True:            # El programa funciona hasta que se presione la tecla de salida
        # blnFrameReadSuccessfully, imgOriginal = capWebcam.read()    # Se lee el siguiente fotograma
        imgOriginal = img
        # if not blnFrameReadSuccessfully or imgOriginal is None:     # Si no se puede leer el fotograma manda un mensaje de error
        #     print( "Error: No se puede leer desde la webcam\n")
        #     os.system("pause")                                      # Se detiene hasta que el usuario pulse una tecla
        #     break                                                   # Se sale del ciclo terminado el programa

        ## En esta secci+on convertimos a escala de grises el video
        imgGrayscale = cv2.cvtColor(imgOriginal, cv2.COLOR_BGR2GRAY)    # Convierte a Escala de grises

        faces = face_cascade.detectMultiScale(imgGrayscale, 1.3, 5)     # Se aplica el entrenador a la imagen en escala de grises

        for (x,y,w,h) in faces:                                         # Se agregan los rectangulos limitadores
             cv2.rectangle(imgOriginal,(x,y),(x+w,y+h),(0,255,0),2)     # Se elige el color en este caso verde
             # Cuando se detecta la cara obtenemos la posicion x y w h donde esta el rostro, entonces tendremos una region de interes (ROI)  para buscar los ojos
             roi_imgGrayscale = imgGrayscale[y:y+h, x:x+w]   #Region de interes para los ojos en escala de grises para el analisis de los ojos
             roi_color = imgOriginal[y:y+h, x:x+w]           #Region de interes donde esta la cara
             eyes = eye_cascade.detectMultiScale(roi_imgGrayscale)  #Se detectan los ojos de la region de interes en escala de grises
             for (ex,ey,ew,eh) in eyes:             #Se crea el rectangulo que indique donde se encuentran los ojos en este caso de color amarillo
                 cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,255,0),2)
            
             smiles = smile_cascade.detectMultiScale(roi_imgGrayscale) 
             for (ex,ey,ew,eh) in smiles:             #Se crea el rectangulo que indique donde se encuentran los ojos en este caso de color amarillo
                 cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,0,0),2)
        cv2.imshow("Detector de", imgOriginal)         # Se grafica
        if cv2.waitKey(200000) == ord('q'):
            break
    # Fin del while

    cv2.destroyAllWindows()                 # Se remueven las ventanas de la memoria

    return

#Estructura del programa
if __name__ == "__main__":
    main()

