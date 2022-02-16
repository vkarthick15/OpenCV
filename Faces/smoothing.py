import cv2 as cv

img = cv.imread("img.jpeg")
cv.imshow("wayne",img)

# Smoothing is generally done when there is a lot of noise in an image
# Kernel is a window like portion of an image which is defined with a size which is bascically rows and columns (Kernel size is must always be odd)

# Averaging Blur- A process where the pixel intesity of the middle pixel of the center as the average intensities of the surrounding pixels

average = cv.blur(img,(3,3))
cv.imshow("Average Blur",average)
 
# The Difference Between Normal and Gaussian Blur?
#The central difference, depending on algorithm, is that Gaussian blur takes a weighted average around the pixel, while “normal” blur just averages all the pixels in the radius of the single pixel together (I believe). I think this latter “normal” blur is called box blur.

# Gaussian Blur is more natural than Blur

gauss = cv.GaussianBlur(img,(3,3),0)
cv.imshow("Gaussian Blur",gauss)

# Median Blur - Same as averaging but uses median of the surrounding pixels

median = cv.medianBlur(img,3)
cv.imshow("Median Blur",median)

# Bilateral Blur - this is an advanced blurring where it blurs the image but retains the edges in the image

bilateral = cv.bilateralFilter(img, 5, 15, 15)
cv.imshow("Bilateral Blur",bilateral)

cv.waitKey(0)