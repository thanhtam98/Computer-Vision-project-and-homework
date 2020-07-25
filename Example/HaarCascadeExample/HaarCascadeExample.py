#Torres Uriel / Valle Eric
import cv2
import numpy as np
import os

def main():

#WebCam capture
    capWebcam = cv2.VideoCapture(1)

    #OpenCV Classifiers
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

    #WebCam
    if capWebcam.isOpened() == False:
        print "Error: No se pudo acceder a la webcam \n\n"          #English: Error: WebCam is unavailable
        os.system("pause")                                          #Pause until the uses press a Key
        return

    while cv2.waitKey(1) != 27 and capWebcam.isOpened():
        blnFrameReadSuccessfully, imgOriginal = capWebcam.read()    # Se lee el siguiente fotograma

        if not blnFrameReadSuccessfully or imgOriginal is None:     # Englis: Error: We can't read the next frame
            print "Error: No se puede leer desde la webcam\n"
            os.system("pause")
            break


        # Process
        imgGrayscale = cv2.cvtColor(imgOriginal, cv2.COLOR_BGR2GRAY)    # Convert into grayscale

        faces = face_cascade.detectMultiScale(imgGrayscale, 1.3, 5)     # Face classifier in the grayscale image

        for (x,y,w,h) in faces:                                         # Draw the rectangle in the face area
             cv2.rectangle(imgOriginal,(x,y),(x+w,y+h),(0,255,0),2)     # RGB: Green
             # Once we detect the face, we obtain a ROI (Region of Interest) so, we looking for eyes inside the ROI
             roi_imgGrayscale = imgGrayscale[y:y+h, x:x+w]
             roi_color = imgOriginal[y:y+h, x:x+w]
             eyes = eye_cascade.detectMultiScale(roi_imgGrayscale) # eye classifier inside the roi_grayscale image
             for (ex,ey,ew,eh) in eyes:             #CMY: Cyan
                 cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,255,0),2)

        cv2.imshow("Detector de rostro", imgOriginal)


    cv2.destroyAllWindows()

    return

if __name__ == "__main__":
    main()




