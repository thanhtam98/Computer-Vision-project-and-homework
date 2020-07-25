import cv2
import numpy as np 


def nothing(x):
    pass
def countX(lst, x):     # find num of element x in lst
    count = 0
    for ele in lst: 
        if (ele == x): 
            count = count + 1
    return count 

img = cv2.imread('bt7.jpg')
# create trackbar to tune value of some functions
cv2.namedWindow('Trackbar')  
cv2.createTrackbar('Low','Trackbar',1,255,nothing)
cv2.createTrackbar('High','Trackbar',1,255,nothing)
cv2.createTrackbar('AreaFilter','Trackbar',1,1000,nothing)
cv2.createTrackbar('MinSizeOfContour','Trackbar',1,25,nothing)
cv2.setTrackbarPos('Low','Trackbar',37)
cv2.setTrackbarPos('High','Trackbar',172)
cv2.setTrackbarPos('MinSizeOfContour','Trackbar',4)
# Conver  RGB to Gray 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
while True:
    # Get value of Trackbar
    Low = cv2.getTrackbarPos('Low','Trackbar')
    High = cv2.getTrackbarPos('High','Trackbar')
    edges = cv2.Canny(gray,Low,High) 
    edgesNonMor = edges 
    # Change the image to get the best mask
    edges = cv2.dilate(edges, None, iterations=1)
    edges = cv2.erode(edges, None, iterations=1)
    contours, hierarchy = cv2.findContours(edges,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    numContour = 0
    grayNonBounding = gray
    #find bounding box by eject small contours
    for contour in contours:
        if cv2.contourArea(contour) < cv2.getTrackbarPos('AreaFilter','Trackbar'):  
            continue
        cv2.drawContours(edgesNonMor, [contour], -1, (0,0,0), 2)
        cv2.drawContours(img, [contour], -1, (255,0,0), 3)
        numContour +=1

    mask = np.zeros(edgesNonMor.shape )
    maskToKmean =np.zeros(edgesNonMor.shape ) 
    contours, hierarchy = cv2.findContours(edgesNonMor,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    maskToKmean = []
    imgToKmean = np.zeros(edgesNonMor.shape ) 
    num = 0
    #find points by eject big contours
    for contour in contours:
        if cv2.contourArea(contour) < cv2.getTrackbarPos('MinSizeOfContour','Trackbar'):
            continue
        cv2.drawContours(mask, [contour], -1, (255,0,0), 2)
        M = cv2.moments(contour)
        #Put situation of point into array for input of Kmean 
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        imgToKmean[cY,cX] = 255
        maskToKmean.append([cY,cX])
        num +=1
  
    maskToKmean = np.float32(maskToKmean)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    #Inplement Kmean to find group of points
    ret,label,center=cv2.kmeans(maskToKmean,numContour,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
    center = center.astype(int)
    elementCounter  = 0
    elementNum = 0
    #Compute sum of element for each region.
    for cen in center:
        print(cen)
        elementCounter = countX(label,elementNum )
        elementNum += 1
        print(elementCounter)
        mask[cen[0],cen[1]]= 255
        cv2.putText(img, str(elementCounter), (cen[1], cen[0]),cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0, 255), 4)
        cv2.circle(mask, (cen[1],cen[0]), 5, (255), -1)
    cv2.putText(img, "Sum of point: "+ str(len(maskToKmean)), (10, 30),cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255, 0), 2)
    cv2.imshow('img',img)
    if cv2.waitKey(30) == ord('q'):
        break
cv2.destroyAllWindows()
