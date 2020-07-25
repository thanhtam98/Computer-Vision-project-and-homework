import numpy as np
import cv2
kernel = np.ones((5,5),np.uint8)

def nothing(x):
    pass
countX =0
countY =0
averX = 0
averY = 0
cap = cv2.VideoCapture('videoplayback.mp4')
BK = cv2.imread('E:\ilovebk.jpg')
cv2.namedWindow('sadasdsa')
cv2.imshow('sadasdsa',BK)
cv2.namedWindow('trackbar')
cv2.createTrackbar('H_low','trackbar',0,255,nothing)
cv2.createTrackbar('H_high','trackbar',0,255,nothing)
cv2.createTrackbar('S_low','trackbar',0,255,nothing)
cv2.createTrackbar('S_high','trackbar',0,255,nothing)
cv2.createTrackbar('V_low','trackbar',0,255,nothing)
cv2.createTrackbar('V_high','trackbar',0,255,nothing)
cv2.setTrackbarPos('H_low','trackbar',0)
cv2.setTrackbarPos('H_high','trackbar',84)
cv2.setTrackbarPos('S_low','trackbar',46)
cv2.setTrackbarPos('S_high','trackbar',185)
cv2.setTrackbarPos('V_low','trackbar',35)
cv2.setTrackbarPos('V_high','trackbar',255)
while(cap.isOpened()):
    HL = cv2.getTrackbarPos('H_low', 'trackbar')
    HH = cv2.getTrackbarPos('H_high', 'trackbar')
    SL = cv2.getTrackbarPos('S_low', 'trackbar')
    SH = cv2.getTrackbarPos('S_high', 'trackbar')
    VL = cv2.getTrackbarPos('V_low', 'trackbar')
    VH = cv2.getTrackbarPos('V_high', 'trackbar')
    ret, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv_frame, (HL, SL, VL), (HH, SH, VH))
    # mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    # median = np.median(mask)
    
    cv2.imshow("mask",mask)
    print(mask.shape)
    # edgeX=0
    # edgeY=0
    # averX = 0
    # countX = 0
    # averY = 0
    # countY = 0
    # Xmax= 0
    # Xmin = mask.shape[0]
    # Ymax= 0
    # Ymin = mask.shape[1]
    # for x in range (mask.shape[0]):
    #     for y in range (mask.shape[1]):
    #         # if mask[x][y] !=0:
    #         #     print (mask[x][y])
    #         if mask[x][y] == 255 :
    #             if(Xmin > x):
    #                 Xmin = x
    #             if (Xmax < x):
    #                 Xmax = x
    #             if(Ymin > y):
    #                 Ymin = y
    #             if (Ymax < y):
    #                 Ymax = y
    #             averX = averX + x
    #             countX = countX + 1

    #             averY = averY + y
    #             countY = countY +1 
   
    # if ((countX != 0)&(countY != 0)):        
    #     averX = averX/countX
    #     averY = averY/countY 
    #     if (averX - Xmin > Xmax - averX):
    #         edgeX = Xmax - averX
    #     else:
    #         edgeX = averX - Xmin

    #     if (averY - Ymin > Ymax - averY):
    #         edgeY = Ymax - averY
    #     else:
    #         edgeY = averY - Ymin
        
    # print (averX,averY)
    # if (edgeX != 0 )&(edgeY != 0) :
    #     edgeX = round(edgeX)
    #     edgeY = round(edgeY)
    #     BK1= cv2.resize(BK,(2*edgeY,2*edgeX),interpolation = cv2.INTER_AREA)
    #     print(BK1.shape)
    #     res = cv2.bitwise_and(frame, frame, mask=mask)

    #     frame[round(averX)-edgeX:round(averX)+edgeX,round(averY)-edgeY:round(averY)+edgeY]=BK1[:,:]
    # # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    cv2.imshow('frame',frame)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()