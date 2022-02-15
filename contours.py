#contours are boundaries of objects (not edges in a mathematical pov)
#contours can be mainly used in shape analaysis and object detection
import cv2 as cv
import numpy as np


img = cv.imread("img.jpeg")
cv.imshow("wayne",img)

blank = np.zeros(img.shape, dtype ='uint8')
cv.imshow("Blank",blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)

blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
cv.imshow("Blur",blur)

canny = cv.Canny(blur, 150, 175)
cv.imshow("Canny",canny)

# The method returns two outputs. The first is the threshold that was used and the second output is the thresholded image.
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow("Thresh",thresh)

contours,hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
#cv.findCountours returns a list of coordinates of countours in an image and returns the hierarchial representation of contours
# RETR_LIST Finds all the contours, RETR_EXTERNAL Finds all the external contours, RETR_TREE Returns all the contours in the hirarchial system
# CHAIN_APPROX_NONE it returns all of the contours, CHAIN_APPROX_SIMPLE returns all contours compressed

cv.drawContours(blank, contours, -1, (0,0,255), 2)
cv.imshow("Contours Drawn",blank)

print(len(contours))




cv.waitKey(0)