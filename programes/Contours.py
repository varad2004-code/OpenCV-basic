import cv2 as cv
import numpy as np

img=cv.imread("images/group.jpg")

cv.imshow("cat image",img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray image",gray)

blank=np.zeros(img.shape,dtype="uint8")
cv.imshow("Blank image",blank)


# blur=cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)
# cv.imshow("Blur image",blur)

# canny=cv.Canny(blur,125,150)
# cv.imshow("Canny image",canny)

ret,thresh=cv.threshold(gray,125,255,cv.THRESH_BINARY)
cv.imshow("thresh image",thresh)

contours, hierarchies = cv.findContours(thresh,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
print(len(contours))

cv.drawContours(blank,contours,-1,(0,255,0),2)
cv.imshow("drawn contours image",blank)

cv.waitKey(0)