import cv2 as cv

img=cv.imread("images/group.jpg")

cv.imshow("Group image",img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray scale image",gray)

cv.waitKey(0)