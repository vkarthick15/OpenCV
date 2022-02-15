import cv2 as cv

img = cv.imread("grppic.jpg")
cv.imshow("wayne",img)

# Face detection does not involve face color tone or in general the color of the image
# haar cascade uses the edges and tries to determine whether it is a face or not

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("GrayScaled",gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')
# haar_cascade is very much influenced by noises in the image

face_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
#The less the values for the above parameters the more sensitive the Classifier will become
print(f"Faces found = {len(face_rect)}")

for (x,y,w,h) in face_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
    
cv.imshow("Faces Detected",img)

cv.waitKey(0)

#TRY FOR VIDEOS