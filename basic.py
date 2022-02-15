import cv2 as cv

img = cv.imread("img.jpeg")
cv.imshow("wayne",img)

#converting to grayscale = intensity distribution of pixels in the image

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow("b/w wayne",gray)

#Blurring an image (removes noise in an image)
#using gaussian blur

blur = cv.GaussianBlur(img,(3,3), cv.BORDER_DEFAULT) #kernel size must be odd eg:(3,3)
#cv.imshow("Blur",blur)

#Edge Cascading ( to calc to the num of edges an image has)
#using canny edge cascading

canny = cv.Canny(blur,125,175) #the other paramaters are thresholds
#cv.imshow("Edges",canny)
 
#dilating an image using edges

dilated = cv.dilate(canny,(3,3),iterations=4)
#cv.imshow("Dilated",dilated)

#eroding an image

eroded = cv.erode(dilated,(3,3),iterations=4)
#cv.imshow("Eroded",eroded)

#resizing an image

resized = cv.resize(img,(500,500),interpolation =cv.INTER_AREA) 
# original to smaller dimensions INTER_AREA but to Larger dimensions INTER_LINEAR and INTER_CUBIC

#cv.imshow("Resized",resized)

#Cropping an image (array slicing)
cropped = img[50:200,200:400]
cv.imshow("Cropped",cropped)

cv.waitKey(0)