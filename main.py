from tkinter import *
import tkinter
from PIL import Image, ImageTk
import os
from student import Student
from time import strftime
from datetime import datetime
from train import Train
from face_recognition import Face_Recognition
from attendence import Attendence
from developer import Developer
from help import Help
import mysql.connector
import cv2

# Main class 
class FaceRecognitionSystem:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1590x690+0+0")
        self.root.title("Face Recognition System")

        # First image
        img13 = Image.open(r"images/download.png")
        img13 = img13.resize((500, 90), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img13)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=500, y=0, width=500, height=90)

        # Title
        title_lbl = Label(self.root, text="Face Recognition System Software", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=100, width=1530, height=45)

        # ================ Time ================
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000, time)

        lbl=Label(title_lbl, font=('times new roman',18,'bold'),background='white',foreground='blue')
        lbl.place(x=10,y=0,width=120,height=50)
        time()


        # Student button
        img4 = Image.open(r"images/imges.jpg")
        img4 = img4.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img4)

        b1 = Button(self.root, image=self.photoimg1, command=self.student_details, cursor="hand2")
        b1.place(x=200, y=200, width=220, height=220)

        b1_1 = Button(self.root, text="Student Details", command=self.student_details, cursor="hand2", font=("times new roman", 15, "bold"), bg="white", fg="red")
        b1_1.place(x=200, y=400, width=220, height=40)

        # Detect face
        img5 = Image.open(r"images/face.jpeg")
        img5 = img5.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b2 = Button(self.root, image=self.photoimg5, cursor="hand2",command=self.face_data)
        b2.place(x=450, y=200, width=220, height=220)

        b2_1 = Button(self.root, text="Face Detection", cursor="hand2",command=self.face_data, font=("times new roman", 15, "bold"), bg="white", fg="red")
        b2_1.place(x=450, y=400, width=220, height=40)

        # Attendance
        img6 = Image.open(r"images/attendance.jpeg")
        img6 = img6.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b3 = Button(self.root, image=self.photoimg6, cursor="hand2",command=self.attendence_data)
        b3.place(x=750, y=200, width=220, height=220)

        b3_1 = Button(self.root, text="Attendance", cursor="hand2",command=self.attendence_data, font=("times new roman", 15, "bold"), bg="white", fg="red")
        b3_1.place(x=750, y=400, width=220, height=40)

        # Help Desk
        img7 = Image.open(r"images/helping.png")
        img7 = img7.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b4 = Button(self.root, image=self.photoimg7, cursor="hand2",command=self.help_data)
        b4.place(x=1000, y=200, width=220, height=220)

        b4_1 = Button(self.root, text="Help Desk", cursor="hand2",command=self.help_data, font=("times new roman", 15, "bold"), bg="white", fg="red")
        b4_1.place(x=1000, y=400, width=220, height=40)

        # Train Data
        img8 = Image.open(r"images/traindata.png")
        img8 = img8.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b5 = Button(self.root, image=self.photoimg8, cursor="hand2",command=self.train_data)
        b5.place(x=200, y=450, width=220, height=220)

        b5_1 = Button(self.root, text="Train Data", cursor="hand2",command=self.train_data, font=("times new roman", 15, "bold"), bg="white", fg="red")
        b5_1.place(x=200, y=670, width=220, height=40)

        # Photos
        img9 = Image.open(r"images/photo-pile.jpeg")
        img9 = img9.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b6 = Button(self.root, image=self.photoimg9,command=self.open_img, cursor="hand2")
        b6.place(x=450, y=450, width=220, height=220)

        b6_1 = Button(self.root, text="Photos", cursor="hand2",command=self.open_img, font=("times new roman", 15, "bold"), bg="white", fg="red")
        b6_1.place(x=450, y=670, width=220, height=40)

        # Developer
        img10 = Image.open(r"images/developer.jpeg")
        img10 = img10.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b7 = Button(self.root, image=self.photoimg10, cursor="hand2",command=self.developer_data)
        b7.place(x=750, y=450, width=220, height=220)

        b7_1 = Button(self.root, text="Developer", cursor="hand2",command=self.developer_data, font=("times new roman", 15, "bold"), bg="white", fg="red")
        b7_1.place(x=750, y=670, width=220, height=40)

        # Exit
        img11 = Image.open(r"images/exit.jpeg")
        img11 = img11.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b8 = Button(self.root, image=self.photoimg11, cursor="hand2", command=self.iExit)
        b8.place(x=1000, y=450, width=220, height=220)

        b8_1 = Button(self.root, text="Exit", cursor="hand2",command=self.iExit, font=("times new roman", 15, "bold"), bg="white", fg="red")
        b8_1.place(x=1000, y=670, width=220, height=40)

    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognization","Are you sure to exit this project",parent=self.root)
        if self.iExit > 0:
            self.root.destroy()
        else:
            return

# sub class of Student Details
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

# Sub class of  Train data
    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

# Sub class of face data
    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

# sub class of attendance 
    def attendence_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendence(self.new_window)

    def developer_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)
    
    def help_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)

if __name__ == "__main__":
    root = Tk()
    obj = FaceRecognitionSystem(root)
    root.mainloop()



    #access modifies:-private , public, protected , class , class member , how to define classes , how to define clas memeber , insertion operator ,
    #  eperator operator = cascading , array of object to acces multiople object
    # wap  to display the data of 5 student in c++ crating class and object , difference between structure(collection ) and class(collection data member), uding namespace to consrruct multiple class function with same name
    #inheritence :-multilevel , multiple ,