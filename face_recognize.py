import numpy as np
import cv2 as cv

haar_cascade = cv.CascadeClassifier('haar_face.xml')

people = ['dicaprio', 'eisaya', 'mads', 'mark wahlberg', 'matt damon', 'phoenix', 'robbie']

# features = np.load('features.npy')
# labels = np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

# Validating the model by trying to recognize a particular person

img = cv.imread(r"C:\Users\vkkn2\Margot-Robbie-GettyImages-1332065473-H-2021.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Person", gray)


# Detect the face in the image

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+w]
    
    label, confidence = face_recognizer.predict(faces_roi)
    print(f'Label = {people[label]} with a Confidence of {confidence}')
    
    cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), 2)
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
    
    
cv.imshow('Detected Face', img)
cv.waitKey(0)