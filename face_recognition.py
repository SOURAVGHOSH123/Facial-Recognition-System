# Import necessary libraries
from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from datetime import datetime
import cv2
import os
import numpy as np

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition App")
        self.root.geometry("1530x790+0+0")  # Window size

        title_lbl = Label(self.root, text="Face Recognition", font=("times new roman", 35, "bold"),
         bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # 1st image
        img_top = Image.open(r"images/face_detector.jpg")
        img_top = img_top.resize((650, 700), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=650, height=700)

        # 2nd image
        img_bottom = Image.open(r"images/face_recognization.png")
        img_bottom = img_bottom.resize((950, 670), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lb1 = Label(self.root, image=self.photoimg_bottom)
        f_lb1.place(x=650, y=55, width=950, height=670)

        # Button
        b1_1 = Button(f_lb1, text="Face Recognition", cursor="hand2", font=("times new roman", 15, "bold"),
                      bg="darkgreen", fg="white", command=self.face_recog)
        b1_1.place(x=360, y=590, width=200, height=40)

    # ============ Attendance ==============
    def mark_attendance(self, i, r, n, d):
        with open("Student_data.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.strip().split(",")
                name_list.append(entry[0])
            if ((i not in name_list) and (r not in name_list)and (n not in name_list)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")

    # ============ Face Recognition ==========
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)
                id, confidence = clf.predict(gray_image[y:y + h, x:x + w])
        
                print(id)

                # if id == 2:
                #     id = 154

                confidence = int(100 * (1 - confidence / 300))

                conn = mysql.connector.connect(host="localhost", username="root", password="T#90addd", database="face_recognizer")
                my_cursor = conn.cursor()

                try:
                    # import pdb; pdb.set_trace()
                    my_cursor.execute("SELECT Name, Roll, Dep, Student_id FROM student WHERE Student_id=%s", (str(id),))
                    result = my_cursor.fetchone()

                    if result:
                        n, r, d, i = result

                        if confidence > 70:
                            cv2.putText(img, f"Id: {i}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 200), 3)
                            cv2.putText(img, f"Roll: {r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 200), 3)
                            cv2.putText(img, f"Name: {n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 200), 3)
                            cv2.putText(img, f"Department: {d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 224), 3)
                            self.mark_attendance(i, r, n, d)
                        else:
                            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                            cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 25, 255), 3)
                    else:
                        cv2.putText(img, "Error Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 25, 255), 3)

                    coord = [x, y, w, h]
                except mysql.connector.Error as err:
                    print(f"Error: {err}")
                finally:
                    conn.close()
            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        # Correct the path to the Haar Cascade file
        faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

        # Check if the classifier file exists
        if not os.path.exists("classifier.xml"):
            messagebox.showerror("Error", "Classifier XML file not found. Please ensure it exists and is properly trained.")
            return

        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        if not video_cap.isOpened():
            messagebox.showerror("Error", "Could not open video stream.")
            return

        while True:
            ret, img = video_cap.read()
            if not ret:
                print("Failed to grab frame")
                break

            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to Face Recognition", img)

            if cv2.waitKey(1) == 13:  # Press 'Enter' to exit
                break

        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()