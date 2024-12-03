from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self, root):
      self.root = root
      self.root.geometry("1530x790+0+0")
      self.root.title("Face Recognition System")

      # Title
      title_lbl = Label(self.root, text="DEVELOPER", font=("times new roman", 35, "bold"), bg="white", fg="blue")
      title_lbl.place(x=0, y=0, width=1530, height=45)

      img1 = Image.open(r"images/developer.jpeg")
      img1 = img1.resize((1500, 720), Image.Resampling.LANCZOS)
      self.photoimg1 = ImageTk.PhotoImage(img1)

      f_lbl = Label(self.root, image=self.photoimg1 )
      f_lbl.place(x=0, y=55, width=1500, height=720)

       # Main frame
      main_frame = Frame(f_lbl, bd=2, bg="white")
      main_frame.place(x=850, y=0, width=500, height=600)

      #  right image
      img_top = Image.open(r"images/sourav ghosh.jpg")
      img_top = img_top.resize((150,150), Image.Resampling.LANCZOS)
      self.photoimg_top = ImageTk.PhotoImage(img_top)

      f_lbl = Label(main_frame, image=self.photoimg_top )
      f_lbl.place(x=300, y=0, width=150, height=150)

      # Developer info
      dev_label = tk.Label(main_frame, text="Hello my name, Sourav", font=("times new roman", 20, "bold"),bg="white")
      dev_label.place(x=0, y=5)
      
      dev_label = tk.Label(main_frame, text="I am a Developer", font=("times new roman", 18, "bold"),bg="white")
      dev_label.place(x=0, y=40)
      
      dev_label = tk.Label(main_frame, text="Mob-7749031273", font=("times new roman", 18, "bold"),bg="white")
      dev_label.place(x=0, y=70)

      #  right second image
      img_middle = Image.open(r"images/cover pic.jpg")
      img_middle = img_middle.resize((150,150), Image.Resampling.LANCZOS)
      self.photoimg_middle = ImageTk.PhotoImage(img_middle)

      f_lbl2 = Label(main_frame, image=self.photoimg_middle )
      f_lbl2.place(x=300, y=160, width=150, height=150)

      # Developer info
      dev_label2 = tk.Label(main_frame, text="Hello my name, Tabish", font=("times new roman", 20, "bold"),bg="white")
      dev_label2.place(x=0, y=160)
      
      dev_label2 = tk.Label(main_frame, text="I am a Developer", font=("times new roman", 18, "bold"),bg="white")
      dev_label2.place(x=0, y=190)
      
      dev_label2 = tk.Label(main_frame, text="Mob-9870531273", font=("times new roman", 18, "bold"),bg="white")
      dev_label2.place(x=0, y=220)

      #  another image
      img2 = Image.open(r"images/group.jpg")
      img2 = img2.resize((150,150), Image.Resampling.LANCZOS)
      self.photoimg2 = ImageTk.PhotoImage(img2)

      f_lbl = Label(main_frame, image=self.photoimg2 )
      f_lbl.place(x=300, y=330, width=159, height=150)

      # Developer info
      dev_label3 = tk.Label(main_frame, text="Hello my name, another", font=("times new roman", 20, "bold"),bg="white")
      dev_label3.place(x=0, y=330)
      
      dev_label3 = tk.Label(main_frame, text="I am a Developer", font=("times new roman", 18, "bold"),bg="white")
      dev_label3.place(x=0, y=370)
      
      dev_label3 = tk.Label(main_frame, text="Mob-6479031273", font=("times new roman", 18, "bold"),bg="white")
      dev_label3.place(x=0, y=400)


if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()