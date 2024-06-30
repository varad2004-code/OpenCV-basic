import cv2 as cv
import numpy as np

blank=np.zeros((500,500,3),dtype="uint8")
cv.imshow("blank image",blank)

#1. paint an image
# blank[100:200, 200:300]=0,0,255
# cv.imshow("painted image",blank)

#2. draw a rectangle
# cv.rectangle(blank,(0,0),(500,500),(0,255,0),thickness=cv.FILLED)
# cv.imshow("Rectangle image",blank)

#3. Draw a circle
# cv.circle(blank,(250,250),40,(0,0,255),thickness=3)
# cv.imshow("Circle image",blank)

#4. Draw a Line
# cv.line(blank,(0,0),(250,250),(255,0,0),thickness=3)
# cv.imshow("Line image",blank)

#Put a text
cv.putText(blank,"Hello world varad here",(0,250),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),thickness=2)
cv.imshow("Text image",blank)

cv.waitKey(0)