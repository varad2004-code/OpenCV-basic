import cv2 as cv
import numpy as np

blank=np.zeros((500,500),dtype="uint8")

rectangle=cv.rectangle(blank.copy(),(30,30),(250,250),255,-1)
circle=cv.circle(blank.copy(),(250,250),100,255,-1)

cv.imshow("rectnagle image",rectangle)
cv.imshow("circle image",circle)

#bitwise and --->intersecting regions
bitwise_and=cv.bitwise_and(rectangle,circle)
cv.imshow("Bitwise and image",bitwise_and)

#Bitwise or --->non intersecting  and intersecting regions
bitwise_or=cv.bitwise_or(rectangle,circle)
cv.imshow("Bitwise or image",bitwise_or)

#bitwise xor --->non intersecting regions
bitwise_xor=cv.bitwise_xor(rectangle,circle)
cv.imshow("Bitwise xor image",bitwise_xor)

#bitwise not
bitwise_not=cv.bitwise_not(circle)
cv.imshow("Bitwise not image",bitwise_not)

cv.waitKey(0)