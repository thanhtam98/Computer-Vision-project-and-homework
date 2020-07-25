import numpy as np
import cv2
import matplotlib.pyplot as plt
def countX(lst, x):     # find num of element x in lst
    count = 0
    for ele in lst: 
        if (ele == x): 
            count = count + 1
    return count 

image = cv2.imread("bt7b.jpg")
cv2.imshow("Raw", image)
blur  = cv2.medianBlur(image, 5)
gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)

# Setup SimpleBlobDetector parameters.
params = cv2.SimpleBlobDetector_Params() 

# Filter by Inertia
params.filterByInertia = True 
params.minInertiaRatio = 0.7  
# Create a detector with the parameters
detector = cv2.SimpleBlobDetector_create(params)
# Binary Picture For Detect Black Pips Of Dice
binary = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 131, 15)
# Detect black blobs.
keypoints = detector.detect(binary)
SumOfPoint = len(keypoints)  
#find center of points
Center = np.zeros(shape=(len(keypoints), 2))  
for i in range(len(keypoints)):
    Center[i][0] = keypoints[i].pt[0]  
for i in range(len(keypoints)):
    Center[i][1] = keypoints[i].pt[1] 
#Convert Center to float 
Center = np.float32(Center)  
#Perform Kmean to find regions
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
ret, label, center = cv2.kmeans(Center,7, None, criteria, 10, cv2.KMEANS_PP_CENTERS)

count = np.zeros((7, 1), dtype=int)  

elementCounter = 0
elementNum = 0
for cen in center:
    elementCounter = countX(label,elementNum )    
    cv2.putText(image, str(elementCounter), (center[elementNum][0], center[elementNum][1]),  cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255,0 ), 2)
    elementNum += 1

# 
binary = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 255, 7)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
erode = cv2.erode(binary, kernel, iterations=1)
kernel2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (4, 4))
dilate = cv2.dilate(erode, kernel2, iterations=1)
dilate = cv2.dilate(dilate, kernel2, iterations=1)
binary = ~dilate


keypoints = detector.detect(binary)
SumOfPoint += len(keypoints)

Center = np.zeros(shape=(len(keypoints), 2))
for i in range(len(keypoints)):
    Center[i][0] = keypoints[i].pt[0]
for i in range(len(keypoints)):
    Center[i][1] = keypoints[i].pt[1]

Center = np.float32(Center)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
Center = np.float32(Center)
ret, label, center = cv2.kmeans(Center,4, None, criteria, 10, cv2.KMEANS_PP_CENTERS)
count = np.zeros((4, 1), dtype=int)

elementCounter = 0
elementNum = 0
for cen in center:
    elementCounter = countX(label,elementNum )
    
    cv2.putText(image, str(elementCounter), (center[elementNum][0], center[elementNum][1]),  cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255,0 ), 2)
    elementNum += 1


cv2.putText(image, 'Sum Of Point:' + str(SumOfPoint), (300, 50),  cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
cv2.imshow("Result", image)
cv2.waitKey(0)
cv2.destroyAllWindows()