import cv2 
from tkinter import*
from tkinter import ttk
import os
from tkinter import messagebox
root=Tk()
root.config(bg="skyblue1")
root.geometry("700x600")

label=Label(root,text="Image Extracton Tool",font=("arial",23,"bold","underline"),fg="black",bg="skyblue1")
label.pack()

x=StringVar()
var1=IntVar()
var2=IntVar()
var3=StringVar()
    
def show():
    
    a=x.get()
    v1=var1.get()
    v2=var2.get()
    v3=var3.get()
    imgs=os.listdir(a)
    clf=cv2.CascadeClassifier('f:/opencv/opencv-master/data/haarcascades/haarcascade_frontalface_default.xml')
    
    for img in imgs:
        gray=cv2.imread(a +img,v1)
        faces=clf.detectMultiScale(gray)
        if(len(faces)>=v2):
            cv2.imwrite(f"{v3}{img}",gray)
            
    messagebox.showinfo("Message","Successfully Extract ")
            
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
l1=Label(root,text="From",font=("arial",18,"bold"),fg="black",bg="skyblue1")
l1.place(x=50,y=100)

e1=ttk.Entry(root,textvariable=x,font=("arial",16))
e1.place(x=230,y=100)

l2=Label(root,text="                            0: GrayScale 1: Color Image",font=("arial",15),fg="black",bg="skyblue1")
l2.place(x=50,y=160)

l2=Label(root,text="Color",font=("arial",18,"bold"),fg="black",bg="skyblue1")
l2.place(x=50,y=200)

e2=ttk.Entry(root,textvariable=var1,font=("ariel",16))
e2.place(x=230,y=200)

# checkbtn1=Checkbutton(root,text="Color",variable=var1,font=("ariel",17))
# checkbtn1.place(x=250,y=180)

# checkbtn2=Checkbutton(root,text="GrayScale",variable=var2,font=("ariel",17))
# checkbtn2.place(x=400,y=180)

l3=Label(root,text="No of Faces",font=("ariel",18,"bold"),fg="black",bg="skyblue1")
l3.place(x=50,y=250)

e3=ttk.Entry(root,textvariable=var2,font=("ariel",16))

e3.place(x=230,y=250)

l4=Label(root,text="To",font=("ariel",18,"bold"),fg="black",bg="skyblue1")
l4.place(x=50,y=310)

e4=ttk.Entry(root,textvariable=var3,font=("ariel",16))
e4.place(x=230,y=310)

btn2=Button(root,text="Extract Image",font=("ariel",15),command=show)
btn2.place(x=50,y=400)

root.mainloop()
