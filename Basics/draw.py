import cv2 as cv
import numpy as np

#img = cv.imread("img.jpeg")
#cv.imshow("wayne",img)

#creating a blank image to draw on it

blank = np.zeros((500,500,3),dtype="uint8")#"uint8" datatype of an image
#cv.imshow("Blank",blank)

# 1.paint the image with a certain color
#Green
#blank[250:300, 300:350] = 0,255,0
#cv.imshow("Green",blank)

#Red
#blank[:] = 0,0,255
#cv.imshow("Red",blank)
#blue
#blank[:] = 255,0,0
#cv.imshow("Blue",blank)

#2.Drawing a Rectangle

cv.rectangle(blank,(0,0),(blank.shape[0]//2,blank.shape[1]//2),(0,255,0),thickness=cv.FILLED ) #thickness = -1 or cv.FILLED results the same
#cv.imshow("Rectangle",blank)

#3. Drawing a circle

cv.circle(blank,(blank.shape[0]//2,blank.shape[1]//2),40,(0,0,255),thickness = 3)
#cv.imshow("Circle",blank)

#4. Drawing a line

cv.line(blank,(0,0),(blank.shape[0]//2,blank.shape[1]//2),(255,255,255),thickness= 5)
#cv.imshow("Line",blank)

#write text on image

cv.putText(blank,"ViShNu",(225,225),cv.FONT_HERSHEY_TRIPLEX,1.0,(255,255,200),thickness = 5)
cv.imshow("Text",blank)


cv.waitKey(0)

#next: % essential functions