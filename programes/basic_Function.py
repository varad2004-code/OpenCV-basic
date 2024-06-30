import cv2 as cv

img=cv.imread("images/group.jpg")
cv.imshow("Group image",img)

#1. Converting the image into gray scale image
# gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow("Gray image",gray)

#2. Blur the image
blur=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow("Blur image",blur)

#3. Edge cascade
canny=cv.Canny(blur,125,175)
cv.imshow("Canny image",canny)

#4 Dilating the image
dilated=cv.dilate(canny,(7,7),iterations=7)
cv.imshow("Dilated image",dilated)

#5 Eroding
eroded=cv.erode(dilated,(5,5),iterations=3)
cv.imshow("Eroded image",eroded)

#6. resize
resized=cv.resize(img,(700,500))
cv.imshow("Resized image",resized)

cv.waitKey(0)