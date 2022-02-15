import cv2 as cv
import numpy as np

img = cv.imread("img.jpeg")
cv.imshow("wayne",img)

#Masking is done using Bitwise Operators 
#for eg :we can mask over people's faces and remove all the unwanted parts of the image using masking 

blank = np.zeros(img.shape[:2], dtype = 'uint8')
#cv.imshow("Blank Image", blank)

mask = cv.circle(blank, (img.shape[1]//2-104,img.shape[0]//2-200), 140, 255, -1)
#cv.imshow("Mask",mask)

masked = cv.bitwise_and(img, img, mask = mask)
#cv.imshow("Masked Circle", masked)


mask1 = cv.rectangle(blank, (img.shape[1]//2,img.shape[0]//2-80), (img.shape[1]//2-200,img.shape[0]//2-320), 255, -1)
#cv.imshow("Mask",mask1)

masked1 = cv.bitwise_and(img, img, mask = mask1)
cv.imshow("Masked Rectangle", masked1)

                   
cv.waitKey(0)