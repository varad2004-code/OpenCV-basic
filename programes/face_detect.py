import cv2 as cv

img=cv.imread("images/group.jpg")
cv.imshow("Group image",img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray scale image",gray)

haar_cascade=cv.CascadeClassifier("haar_face.xml")

faces_rect=haar_cascade.detectMultiScale(gray,scaleFactor=1.2,minNeighbors=1)

print(f"Number of faces found in the image:-{len(faces_rect)}")

for (x,y,w,h) in faces_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)

cv.imshow("Detected faces in the image",img)

cv.waitKey(0)