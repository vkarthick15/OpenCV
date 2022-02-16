import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread("img.jpeg")
cv.imshow("wayne",img)

#plt.imshow(img)
#plt.show()

# BGR To Grayscale

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)

# Grayscale to BGR

sh = cv.cvtColor(img, cv.COLOR_GRAY2BGR)
cv.imshow("GS->BGR",sh)

# BGR TO HSV(Huge Saturation value - Based on how humans percieve and conceive colors)
 
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow("HSV",hsv)

# HSV to BGR

hs = cv.cvtColor(img,cv.COLOR_HSV2BGR)
cv.imshow("HSV->BGR",hs)

#BGR to l*a*b

lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow("L*a*b",lab)

# l*a*b to BGR

bal = cv.cvtColor(img,cv.COLOR_LAB2BGR)
cv.imshow("LAB->BGR",bal)

#BGR to RGB

rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("RGB",rgb)

#RGB To BGR

rgg = cv.cvtColor(img,cv.COLOR_RGB2BGR)
cv.imshow("RGB->BGR",rgg)


plt.imshow(rgb)
plt.show()

cv.waitKey(0)