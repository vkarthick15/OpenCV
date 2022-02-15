import cv2 as cv
#reading images
img = cv.imread("img.jpeg")
cv.imshow("Wayne",img)

#reading videos
capture = cv.VideoCapture("hi.mp4")
while True:
    isTrue,frame = capture.read()
    
    cv.imshow("hi",frame)
    
    if cv.waitKey(20) & 0xFF==ord("d"):
        break
        
    capture.release()
    cv.destroyAllWindows
    cv.waitKey(0)


#rescaling and resizing
def rescaleFrame(frame,scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)
    
    return cv.resize(frame,dimensions, interpolation = cv.INTER_AREA)

imgrs = rescaleFrame(img)

cv.imshow("rescaled",imgrs)
cv.waitKey(0)

#changing resolution while capturing a video 
def changeres(width,height):
    capture.set(3,width)
    capture.set(4,height)
