import cv2 as cv
import numpy as np

img = cv.imread("img.jpeg")
cv.imshow("wayne",img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Grayscale",gray)

#Thresholding - It is binarisation of an image i.e, we convert the image into binary where the pixelds are black(zero or 0) or White(255)

# Simple Thresholding
# The method returns two outputs. The first is the threshold that was used and the second output is the thresholded image.
threshold, thresh = cv.threshold(gray, 50, 255, cv.THRESH_BINARY)
cv.imshow("Threshold",thresh)

threshold, thresh_inv = cv.threshold(gray, 30, 255, cv.THRESH_BINARY_INV)
cv.imshow("Threshold Inverse",thresh_inv)

# Adaptive Thresholding - Optimal Threshold value is set by the method itself (uses mean,gaussian to find the optimal threshold value)

adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 15, 10)
cv.imshow("Adaptive Thresholding", adaptive_thresh)

cv.waitKey(0)