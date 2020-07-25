import cv2
import numpy as np
img= cv2.imread('rec.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
edged = cv2.Canny(gray, 30, 200)
contours, hierarchy = cv2.findContours(edged,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 
cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
cv2.imshow('contour',img )
for c in contours:
    M = cv2.moments(c)
    
    print(cv2.contourArea(c))
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    cv2.circle(img, (cX, cY), 5, (255, 255, 255), -1)
    cv2.putText(img, "center", (cX - 25, cY -25),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0, 0), 2)
    cv2.putText(img, str(cv2.contourArea(c)), (cX + 25, cY +25),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255, 0), 2)
    approx = cv2.approxPolyDP(c, 0.01*cv2.arcLength(c, True), True)
    x = approx.ravel()[0]
    y = approx.ravel()[1]
    if len(approx) == 3:
        cv2.putText(img, "Triangle", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0, 255),2)
    elif len(approx) == 4:
        cv2.putText(img, "Rectangle", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0, 255),2)
    else:
        cv2.putText(img, "Circle", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0, 255),2)
    #area = cv2.contourArea(c)
cv2.imshow("Image", img)
cv2.waitKey(0) 
cv2.destroyAllWindows()