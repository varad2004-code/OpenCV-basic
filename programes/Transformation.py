import cv2 as cv
import numpy as np

img=cv.imread("images/group.jpg")
cv.imshow("Group image",img)

#Translation image
def translate(img,x,y):
    tranMat=np.float32([[1,0,x],[0,1,y]])
    dimensions=(img.shape[1],img.shape[0])
    return cv.warpAffine(img,tranMat,dimensions)

translated=translate(img,-150,-100)
cv.imshow("Translated image",translated)

# Rotation of image
def rotate(img,angle,rotPoint=None):
    (height,width)=img.shape[:2]

    if rotPoint is None:
        rotPoint=(width//2,height//2)
    rotMat=cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimenesions=(width,height)
    return cv.warpAffine(img,rotMat,dimenesions)

rotated=rotate(img,45)
cv.imshow("Rotated image",rotated)

rotated1=rotate(rotated,-45)
cv.imshow("Rotated imagen 1", rotated1)

cv.waitKey(0)