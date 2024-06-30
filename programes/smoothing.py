import cv2 as cv
import numpy as np

img=cv.imread("images/group.jpg")
cv.imshow("Group image",img)

#Averaging blur image
average=cv.blur(img,(3,3))
cv.imshow("Average image blur image",average)

#Gaussian blur image
gals=cv.GaussianBlur(img,(7,7),3)
cv.imshow("Gaussian blur image",gals)

#Median blur image
median=cv.medianBlur(img,3)
cv.imshow("Median blur image",median)

#Bilateral blur image
bilateral=cv.bilateralFilter(img,10,34,35)
cv.imshow("Bilateral blur image",bilateral)

cv.waitKey(0)