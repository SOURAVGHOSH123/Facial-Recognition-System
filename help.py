from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import cv2


class Help:
   def __init__(self, root):
      self.root = root
      self.root.geometry("1530x790+0+0")
      self.root.title("Face Recognition System")

      # Title
      title_lbl = Label(self.root, text="HELP DESK", font=("times new roman", 35, "bold"), bg="white", fg="blue")
      title_lbl.place(x=0, y=0, width=1500, height=45)

      img1 = Image.open(r"images\helping.png")
      img1 = img1.resize((1500, 720), Image.Resampling.LANCZOS)
      self.photoimg1 = ImageTk.PhotoImage(img1)

      f_lbl = Label(self.root, image=self.photoimg1 )
      f_lbl.place(x=0, y=55, width=1500, height=720)

      # email info
      dev_label = tk.Label(f_lbl, text="Email:sg608251@gmail.com", font=("times new roman", 20, "bold"),bg="white")
      dev_label.place(x=500, y=260)
      dev_label2 = tk.Label(f_lbl, text="Email:sg608251@gmail.com", font=("times new roman", 20, "bold"),bg="white")
      dev_label2.place(x=500, y=300)
      dev_label3 = tk.Label(f_lbl, text="Email:sg608251@gmail.com", font=("times new roman", 20, "bold"),bg="white")
      dev_label3.place(x=500, y=340)




if __name__ == "__main__":
   root = Tk()
   obj = Help(root)
   root.mainloop()