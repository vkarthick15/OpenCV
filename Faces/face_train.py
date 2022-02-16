import os
import cv2 as cv
import numpy as np

people = []
DIR = r'D:\Programming\OpenCV\train'
haar_cascade = cv.CascadeClassifier('haar_face.xml')

for i in os.listdir(r'D:\Programming\OpenCV\train'):
    people.append(i)

features = []
labels = []
def create_train():
    for person in people:
        path = os.path.join(DIR,person)
        label = people.index(person)
        
        for img in os.listdir(path):
            img_path = os.path.join(path,img)
            
            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
            
            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
            
            for (x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)
                
create_train()
print("---------------------------------Training Done--------------------------------")


# print(f'Length of the Features = {len(features)}')
# print(f'Length of the Labels = {len(labels)}')

features = np.array(features, dtype = 'object')
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create() #instatiating the face recognizer

# Training the features and labels of our images

face_recognizer.train(features,labels)

#face_recognizer allows you to save the trained model so that we can use this model in any code

face_recognizer.save('face_trained.yml')

np.save('features.npy',features)
np.save('labels.npy',labels)

            