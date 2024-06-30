import numpy as np
import cv2 as cv

haar_cascade = cv.CascadeClassifier("haar_face.xml")
people = ["Ben afflek","elton john"]

# features=np.load("features.npy")
# labels=np.load("labels.npy")

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read("face_trained.yml")

img=cv.imread(r"D:\Python\Computer vision\faces\train\Ben affleck\2.jpg")

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Person image",gray)

#Detect the face in the image
faces_rect=haar_cascade.detectMultiScale(gray,1.1,4)

for (x,y,w,h) in faces_rect:
    faces_roi=gray[y:y+h,x:x+w]

    label,confidence=face_recognizer.predict(faces_roi)

    cv.putText(img,str(people[label]),(20,20),cv.FONT_HERSHEY_COMPLEX,1.4,(0,255,0,),thickness=2)
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)

cv.imshow("Detected face",img)

cv.waitKey(0)