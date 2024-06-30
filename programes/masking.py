import cv2 as cv
import numpy as np

img=cv.imread("images/group.jpg")
cv.imshow("Group",img)
blank=np.zeros(img.shape[:2],dtype="uint8")
cv.imshow("Blank image",blank)

mask=cv.rectangle(blank,(img.shape[1]//2,img.shape[0]//2),(img.shape[1]//2+100,img.shape[0]//2+100),255,-1)
cv.imshow("Masking image",mask)

masked=cv.bitwise_and(img,img,mask=mask)
cv.imshow("Masked image",masked)


cv.waitKey(0)