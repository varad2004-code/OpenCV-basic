import cv2 as cv

img=cv.imread("images/taj.jpg")

cv.imshow("Taj image",img)

b,g,r=cv.split(img)
cv.imshow("Blue",b)
cv.imshow("Green",g)
cv.imshow("red",r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

cv.waitKey(0)