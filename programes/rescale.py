import cv2 as cv

img=cv.imread("images/group.jpg")

cv.imshow("Group",img)

def rescaleframe(frame,scale=0.75):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

resized_image=rescaleframe(img)
cv.imshow("image",resized_image)

# capture=cv.VideoCapture('video/cat.mp4')

# while True:
#     isTrue,frame=capture.read()
#     frame_resized=rescaleframe(frame,scale=0.5)

#     cv.imshow("video",frame)
#     cv.imshow("video resized",frame_resized)

#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break
# capture.release()
# capture.destroyAllWindows()

cv.waitKey(0)