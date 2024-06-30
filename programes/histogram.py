import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img=cv.imread("images/group.jpg")
cv.imshow("Group image",img)

blank=np.zeros(img.shape[:2],dtype="uint8")

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray scale image",gray)

circle=cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)
mask=cv.bitwise_and(gray,gray,mask=circle)
cv.imshow("Masked image",mask)

#Grayscale histogram
gray_hist=cv.calcHist([gray],[0],mask,[256],[0,256])
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("x")
plt.ylabel("y")
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

#Color histogram
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("x")
plt.ylabel("y")
colors=("b","g","r")
for i,col in enumerate(colors):
    hist=cv.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist,color=col)
plt.show()

cv.waitKey(0)