import cv2 as cv
import numpy as np

img = cv.imread("img.jpeg")
cv.imshow("wayne",img)

#Computing Edges (note: Edges and Gradients aren't the same but with having a programming perspective we can escape the difference)
#Already used Canny method to detect edges

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Grayscaled",gray)

# Laplacian 

lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap)) 
#Images should not have negative pixel values which often happens while grayscaling that's the reason why we use absolute value of the image, so that all the values in the image are absolute
cv.imshow("Laplacian",lap)

# Sobel Gradient Magnitude representation
# This Algorithm that computes the gradients computes the gradients in two directions X and Y axes

sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
cv.imshow("Sobel X", sobelx)
cv.imshow("Sobel Y", sobely)

combined = cv.bitwise_or(sobelx, sobely, None)
cv.imshow("Sobel (Combined Axes)",combined)

# Canny
# Canny does use two thresholds (upper and lower): If a pixel gradient is higher than the upper threshold, the pixel is accepted as an edge. If a pixel gradient value is below the lower threshold, then it is rejected.

canny = cv.Canny(gray, 150, 175)
cv.imshow("Canny",canny)


cv.waitKey(0)