import cv2
cap=cv2.VideoCapture("D:/videos/Kinna_Sona_Full_Video___Marjaavaan___Sidharth_M%2C_Tara_S___Meet_Bros%2CJubin_N%2C_Dhvani_Bhanushali(1080p).mp4")
fgbg=cv2.createBackgroundSubtractorMOG2()
while True:
    ret,frame=cap.read()
    fgmask=fgbg.apply(frame)
    cv2.imshow("original",frame)
    cv2.imshow("fg",fgmask)
    if cv2.waitKey(1)==13:
        break
cap.release()
cv2.destroyAllWindows()
