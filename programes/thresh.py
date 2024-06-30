import cv2 as cv

img=cv.imread("images/group.jpg")
cv.imshow("Group",img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Grayscale image",gray)

#Simple Thresholding image
threshold,thresh=cv.threshold(gray,130,255,cv.THRESH_BINARY)
cv.imshow("simple thresholding image",thresh)

threshold,thresh_inverse=cv.threshold(gray,130,255,cv.THRESH_BINARY_INV)
cv.imshow("simple Inverse thresholding image",thresh_inverse)

#Adaptive Thresholding
adaptive_thresh=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,2)
cv.imshow("Adaptive Thresholding image",adaptive_thresh)

cv.waitKey(0)