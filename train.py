from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="Train Data Set", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=10, width=1530, height=65)

        b1_1 = Button(self.root, text="Train Data", command=self.train_classifier, cursor="hand2", font=("times new roman", 35, "bold"), bg="white", fg="green")
        b1_1.place(x=0, y=280, width=1530, height=325)

    def train_classifier(self):
        data_dir = "data"
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]
        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L')  # Convert image to grayscale
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("training", imageNp)
            if cv2.waitKey(1) == 13:
                break
        ids = np.array(ids)

        # Train classifier
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training Dataset is completed")

if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()