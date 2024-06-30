import cv2 as cv
import numpy as np

img=cv.imread("images/group.jpg")
cv.imshow("Group image",img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray image",gray)

#laplacian
lap=cv.Laplacian(gray,cv.CV_64F)
lap=np.uint8(np.absolute(lap))
cv.imshow("Laplacian image",lap)

#Sobel
sobelx=cv.Sobel(gray,cv.CV_64F,1,0)
sobely=cv.Sobel(gray,cv.CV_64F,0,1)
combine_sobel=cv.bitwise_and(sobelx,sobely)

cv.imshow("Sobel X image",sobelx)
cv.imshow("Sobel Y image",sobely)
cv.imshow("Combine sobel image",combine_sobel)

cv.waitKey(0)