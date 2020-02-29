Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 


>>> 

>>> 

>>> 
>>> #'C:\Users\amit\AppData\Local\Programs\Python\Python37-32\Lib\site-packages\cv2\data'
>>> import cv2
>>> 
>>> img=cv2.imread('f:/data/python/minion.png')
>>> img.shape
(545, 638, 3)
>>> cv2.imshow('window',img)
>>> rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
>>> cv2.imshow('window',rgb)
>>> cv2.waitKey(0)
113
q
>>> 
>>> rgb=cv2.cvtColor(img,cv2.COLOR_BGR2HLS)
>>> cv2.imshow('window',rgb)
>>> rgb=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
>>> cv2.imshow('window',rgb)
>>> cv2.imshow('window',img)
>>> 
>>> x=cv2.rectangle(img,(10,10),(100,100),(255,0,0),2)
>>> cv2.imshow('window',img)
>>> x=cv2.circle(img,(150,200),100,(0,255,0),-1)
>>> cv2.imshow('window',img)
>>> x=cv2.circle(img,(150,200),100,(0,0,255),-1)
>>> cv2.imshow('window',img)
>>> x=cv2.circle(img,(150,200),100,(0,255,0),2)
>>> cv2.imshow('window',img)
>>> 
>>> 
>>> 
>>> #thresholding is to get selected colors from a image
>>> img=cv2.imread("f:/data/python/thresh.png")
>>> cv2.imshow('orginal blur image',img)
>>> 
>>> limit,threshimage=cv2.threshold(img,115,255,cv2.THRESH_BINARY)
>>> limit
115.0
>>> cv2.imshow('thresh image',threshimage)
>>> 
>>> grimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
>>> cv2.imshow('gray scaled image because adptthreshlod supports only gray',grimage)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    cv2.imshow('gray scaled image because adptthreshlod supports only gray',grimage)
NameError: name 'grimage' is not defined
>>> cv2.imshow('gray scaled image because adptthreshlod supports only gray',grimg)
>>> #syntax cv2.imshow('title any name',image)
>>> 
>>> newimg=cv2.adaptiveThreshold(grimg,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,0)
>>> cv2.imshow("clean image part 1",newimg)
>>> newimg=cv2.adaptiveThreshold(grimg,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,5)
>>> cv2.imshow("clean image part 1",newimg)
>>> newimg=cv2.adaptiveThreshold(grimg,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,3)
>>> cv2.imshow("clean image part 1",newimg)
>>> newimg=cv2.equalizeHist(newimg)
>>> cv2.imshow("clean image part 1",newimg)
>>> 
>>> 
>>> cam=cv2.VideoCapture("f:/data/python/Footage of walking people on the street ,jeepneys CCTV style Philippines.mp4")
>>> while 1:
	reslt,img=cam.read()
	cv2.imshow("movie",img)
	if cv2.waitKey(1)!=-1:
		break

	
>>> while 1:
	reslt,img=cam.read()
	img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	nimg=cv2.Canny(img,115,255)
	cv2.imshow("movie",img)
	if cv2.waitKey(1)!=-1:
		break

	
>>> while 1:
	reslt,img=cam.read()
	img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	nimg=cv2.Canny(img,115,255)
	cv2.imshow("movie",nimg)
	if cv2.waitKey(1)!=-1:
		break

	
>>> img=cv2.imread("f:/data/python/thresh.png")
>>> grimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
>>> nimg=cv2.Canny(img,115,255)
>>> cv2.imshow("movie",nimg)
>>> newimg=cv2.adaptiveThreshold(grimg,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,3)
>>> nimg=cv2.Canny(newimg,115,255)
>>> cv2.imshow("movie",nimg)
>>> while 1:
	reslt,img=cam.read()
	img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	nimg=cv2.Canny(img,115,255)
	cv2.imshow("amit",nimg)
	if cv2.waitKey(100)!=-1:
		break

	
>>> while 1:
	reslt,img=cam.read()
	img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	nimg=cv2.Canny(img,115,255)
	cv2.imshow("amit",nimg)
	if cv2.waitKey(0.5)!=-1:
		break

	
Traceback (most recent call last):
  File "<pyshell#76>", line 6, in <module>
    if cv2.waitKey(0.5)!=-1:
TypeError: integer argument expected, got float
>>> cam=cv2.VideoCapture(0)
>>> while 1:
	reslt,img=cam.read()
	img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	nimg=cv2.Canny(img,115,255)
	cv2.imshow("amit",nimg)
	if cv2.waitKey(0.5)!=-1:
		break

	
Traceback (most recent call last):
  File "<pyshell#79>", line 6, in <module>
    if cv2.waitKey(0.5)!=-1:
TypeError: integer argument expected, got float
>>> while 1:
	reslt,img=cam.read()
	img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	nimg=cv2.Canny(img,115,255)
	cv2.imshow("amit",nimg)
	if cv2.waitKey(1)!=-1:
		break

	
>>> while 1:
	reslt,img=cam.read()
	cv2.imshow("amit",nimg)
	if cv2.waitKey(1)!=-1:
		break

	
>>> while 1:
	reslt,img=cam.read()
	cv2.imshow("amit",img)
	if cv2.waitKey(1)!=-1:
		break

	
>>> while 1:
	reslt,img=cam.read()
	img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	cv2.imshow("amit",img)
	if cv2.waitKey(1)!=-1:
		break

	
>>> while 1:
	reslt,img=cam.read()
	img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	nimg=cv2.equalizeHist(img)
	cv2.imshow("amit",img)
	if cv2.waitKey(1)!=-1:
		break

	
>>> while 1:
	reslt,img=cam.read()
	img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	cv2.imshow('org',img)
	nimg=cv2.equalizeHist(img)
	cv2.imshow("amit",img)
	if cv2.waitKey(1)!=-1:
		break

	
>>> cam=cv2.VideoCapture(0)
>>> while 1:
	reslt,img=cam.read()
	img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	cv2.imshow('org',img)
	nimg=cv2.equalizeHist(img)
	cv2.imshow("amit",img)
	if cv2.waitKey(1)!=-1:
		break

	
>>> face=cv2.CascadeClassifier('C:\Users\amit\AppData\Local\Programs\Python\Python37-32\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> face=cv2.CascadeClassifier(r'C:\Users\amit\AppData\Local\Programs\Python\Python37-32\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')
>>> while 1:
	reslt,img=cam.read()
	img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	rest=face.detectMultiScale(img,1.5,5)
	if rest:
		print("face detected")
	cv2.imshow("amit",img)
	if cv2.waitKey(1)!=-1:
		break

	
>>> while 1:
	reslt,img=cam.read()
	img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	rest=face.detectMultiScale(img,1.5,5)
	if rest:
		print("face detected")
	cv2.imshow("amit",img)
	if cv2.waitKey(1)!=-1:
		break

	
Traceback (most recent call last):
  File "<pyshell#100>", line 5, in <module>
    if rest:
ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()
>>> while 1:
	reslt,img=cam.read()
	img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	rest=face.detectMultiScale(img,1.5,5)
	if type(rest):
		print("face detected")
	cv2.imshow("amit",img)
	if cv2.waitKey(1)!=-1:
		break

	

>>> while 1:
	reslt,img=cam.read()
	img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	rest=face.detectMultiScale(img,1.5,5)
	for x,y,h,w in rest:
		l=cv2.rectangle(img,(x,y),(x+h,y+w),(255,0,0),3)
	cv2.imshow("amit",img)
	if cv2.waitKey(1)!=-1:
		break

	
>>> while 1:
	reslt,img=cam.read()
	img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	rest=face.detectMultiScale(img,1.5,5)
	for x,y,h,w in rest:
		l=cv2.rectangle(img,(x,y),(x+h,y+w),(255,0,0),3)
	cv2.imshow("amit",img)
	if cv2.waitKey(1)!=-1:
		break

	
>>> while 1:
	reslt,img=cam.read()
	img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	rest=face.detectMultiScale(img,1.3,5)
	for x,y,h,w in rest:
		l=cv2.rectangle(img,(x,y),(x+h,y+w),(255,0,0),3)
	cv2.imshow("amit",img)
	if cv2.waitKey(1)!=-1:
		break

	
>>> 
=============================== RESTART: Shell ===============================
>>> 
