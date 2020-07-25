import cv2
import numpy as np 


img = cv2.imread('blob.png')
cv2.imshow('ogrinal',img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,40,150)
contours, hierarchy = cv2.findContours(edges,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
nb_components, output, stats, centroids = cv2.connectedComponentsWithStats(gray, connectivity=8)
sizes = stats[1:, -1]; nb_components = nb_components - 1
min_size = 600  

#your answer image
img2 = np.zeros((output.shape))
#for every component in the image, you keep it only if it's above min_size
for i in range(0, nb_components):
    if sizes[i] >= min_size:
        img2[output == i + 1] = 255   
cv2.imshow('final',img2)

cv2.waitKey(0)
