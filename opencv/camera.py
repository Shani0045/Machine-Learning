import cv2
cap=cv2.VideoCapture(0)
while True:
    ret, frame=cap.read()
    img=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("live video", img)
    if cv2.waitKey(1)==13:
        break
cap.release()
cv2.destroyAllWindows()

