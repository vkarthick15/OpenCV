import cv2 as cv
import numpy as np

img = cv.imread("img.jpeg")
cv.imshow("wayne",img)

#Translating Shifting image along X and Y axis
def Translate(img, x, y):
    TransMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img, TransMat, dimensions)

# -x left
# x right
# -y up
# y down

shifty = Translate(img, -100, 200)
#cv.imshow("shifty wayne",shifty)

#Rotating an image 

def rotate(img, angle, rotpoint = None):
    (height,width) = img.shape[:2]
    
    if rotpoint == None:
        rotpoint = (width//2,height//2)
        
    rotmat = cv.getRotationMatrix2D(rotpoint, angle, 1.0)   
    dimensions = (width,height)
    
    return cv.warpAffine(img, rotmat, dimensions)

rotated = rotate(img, 45)
#cv.imshow("Rotated",rotated)

#Flipping an image
# flipcode -> 0 - flipping vertically, 1- flipping horizontally, -1 both vertical and horizontal

flip = cv.flip(img,-1)
cv.imshow("Flip",flip)

    
cv.waitKey(0)
