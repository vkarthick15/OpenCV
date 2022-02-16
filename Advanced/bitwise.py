import cv2 as cv
import numpy as np

#img = cv.imread("img.jpeg")
#cv.imshow("wayne",img)

blank = np.zeros((400,400),dtype = 'uint8')

#Drawing a rectangle

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)

cv.imshow("Rectangle",rectangle)
cv.imshow("Circle",circle)

#Bitwise Operators

#AND - Intersecting Region
 
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow("And Operator",bitwise_and)

#OR - Overlaps one over the other

bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow("OR Operator",bitwise_or)

#XOR - Non Intersecting Region 

bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow("XOR Operator",bitwise_xor)

#NOT - Inverts the binary color

bitwise_not = cv.bitwise_not(rectangle)
cv.imshow("NOT Operator",bitwise_not)

bitwise_not1 = cv.bitwise_not(circle)
cv.imshow("NOT Operator1",bitwise_not1)

cv.waitKey(0)