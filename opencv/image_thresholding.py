import cv2
img=cv2.imread("fufa photo.png")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,threshold=cv2.threshold(img,100,255,cv2.THRESH_BINARY)
cv2.imshow("output",threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()
