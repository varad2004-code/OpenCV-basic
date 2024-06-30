import cv2 as cv
import matplotlib.pyplot as plt

img=cv.imread("images/group.jpg")

cv.imshow("group image",img)

plt.imshow(img)
plt.show()

# #BGR TO GRAYSCALE
# gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow("Gray image",gray)

# #BGR TO HSV
# hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
# cv.imshow("Hsv image",hsv)

# #BGR TO LAB
# lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)
# cv.imshow("Lab image",lab)



# cv.waitKey(0)