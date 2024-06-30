import cv2 as cv

# img=cv.imread('images/group.jpg')
# cv.imshow('Group',img)
# cv.waitKey(0)

#Reading videos
capture=cv.VideoCapture('video/cat.mp4')

while True:
    isTrue,frame=capture.read()
    cv.imshow("video",frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
capture.destroyAllWindows()