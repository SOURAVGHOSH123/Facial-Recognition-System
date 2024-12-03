from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # Variable
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()
        self.var_radio1 = StringVar()

        # First image
        img = Image.open(r"images/download.png")
        img = img.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=500, y=0, width=500, height=130)

        # Title
        title_lbl = Label(self.root, text="                Student Management System", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=130, width=1530, height=65)

        # Main frame
        main_frame = Frame(self.root, bd=2, bg="white")
        main_frame.place(x=0, y=195, width=1530, height=595)

        # Left side
        left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Detail", font=("times new roman", 20, "bold"), bg="white", fg="red")
        left_frame.place(x=10, y=10, width=750, height=570)
 
        # Current course
        current_course_frame = LabelFrame(left_frame, bd=2, relief=RIDGE, text="Current Course", font=("times new roman", 20, "bold"), bg="white", fg="red")
        current_course_frame.place(x=5, y=10, width=750, height=150)
        
        # Department
        dep_label = tk.Label(current_course_frame, text="Department", font=("times new roman", 20, "bold"))
        dep_label.grid(row=0, column=0, padx=2, pady=10, sticky="W")

        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep, style="TCombobox")
        dep_combo["values"] = ("Select Department", "Computer", "IT", "Civil", "Mechanical")
        dep_combo.current(0)  # Set the default value
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky="W")

        # Course
        course_label = tk.Label(current_course_frame, text="Course", font=("times new roman", 20, "bold"))
        course_label.grid(row=0, column=2, padx=2, pady=10, sticky="W")

        course_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course, style="TCombobox")
        course_combo["values"] = ("Select Course", "FE", "SE", "TE", "BE")
        course_combo.current(0)  # Set the default value
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky="W")

        # Year
        year_label = tk.Label(current_course_frame, text="Year", font=("times new roman", 20, "bold"))
        year_label.grid(row=1, column=0, padx=2, pady=10, sticky="W")

        div_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year, style="TCombobox")
        div_combo["values"] = ("Select Year", "2020-21", "2021-22", "2022-23", "2023-24")
        div_combo.current(0)  # Set the default value
        div_combo.grid(row=1, column=1, padx=2, pady=10, sticky="W")

        # Semester
        semester_label = tk.Label(current_course_frame, text="Semester", font=("times new roman", 20, "bold"))
        semester_label.grid(row=1, column=2, padx=2, pady=10, sticky="W")

        semester_combo = ttk.Combobox(current_course_frame, textvariable=self.var_semester, style="TCombobox")
        semester_combo["values"] = ("Select Semester", "Semester 1", "Semester 2", "Semester 3", "Semester 4")
        semester_combo.current(0)  # Set the default value
        semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky="W")

        # Class Student information
        class_Student_frame = LabelFrame(left_frame, bd=2, relief=RIDGE, text="Class Student Information", font=("times new roman", 20, "bold"), bg="white", fg="red")
        class_Student_frame.place(x=3, y=200, width=720, height=300)
 
        # Student ID
        studentId_label = tk.Label(class_Student_frame, text="Student ID:", font=("times new roman", 10, "bold"))
        studentId_label.grid(row=0, column=0, padx=10, pady=10, sticky="W")

        studentId_entry = ttk.Entry(class_Student_frame, textvariable=self.var_std_id, width=20, font=("times new roman", 10, "bold"))
        studentId_entry.grid(row=0, column=1, padx=10, pady=10, sticky="W")

        # Student Name
        studentName_label = tk.Label(class_Student_frame, text="Student Name:", font=("times new roman", 10, "bold"))
        studentName_label.grid(row=0, column=2, padx=5, pady=5, sticky="W")

        studentName_entry = ttk.Entry(class_Student_frame, textvariable=self.var_std_name, width=20, font=("times new roman", 10, "bold"))
        studentName_entry.grid(row=0, column=3, padx=5, pady=5, sticky="W")

        # Class Division
        class_div_label = tk.Label(class_Student_frame, text="Class Division:", font=("times new roman", 10, "bold"))
        class_div_label.grid(row=1, column=0, padx=10, pady=10, sticky="W")

        div_combo = ttk.Combobox(class_Student_frame, textvariable=self.var_div, style="TCombobox")
        div_combo["values"] = ("A", "B", "C")
        div_combo.current(0)  # Set the default value
        div_combo.grid(row=1, column=1, padx=2, pady=10, sticky="W")

        # Roll Number
        roll_label = tk.Label(class_Student_frame, text="Roll No.:", font=("times new roman", 10, "bold"))
        roll_label.grid(row=1, column=2, padx=10, pady=10, sticky="W")

        roll_entry = ttk.Entry(class_Student_frame, textvariable=self.var_roll, width=20, font=("times new roman", 10, "bold"))
        roll_entry.grid(row=1, column=3, padx=10, pady=10, sticky="W")

        # Gender
        gender_label = tk.Label(class_Student_frame, text="Gender:", font=("times new roman", 10, "bold"))
        gender_label.grid(row=2, column=0, padx=10, pady=10, sticky="W")

        div_combo = ttk.Combobox(class_Student_frame, textvariable=self.var_gender, style="TCombobox")
        div_combo["values"] = ("Male", "Female", "Other")
        div_combo.current(0)  # Set the default value
        div_combo.grid(row=2, column=1, padx=2, pady=10, sticky="W")
        
        # DOB
        dob_label = tk.Label(class_Student_frame, text="DOB:", font=("times new roman", 10, "bold"))
        dob_label.grid(row=2, column=2, padx=10, pady=10, sticky="W")

        dob_entry = ttk.Entry(class_Student_frame, textvariable=self.var_dob, width=20, font=("times new roman", 10, "bold"))
        dob_entry.grid(row=2, column=3, padx=10, pady=10, sticky="W")

        # Email
        email_label = tk.Label(class_Student_frame, text="Email:", font=("times new roman", 10, "bold"))
        email_label.grid(row=3, column=0, padx=10, pady=10, sticky="W")

        email_entry = ttk.Entry(class_Student_frame, textvariable=self.var_email, width=20, font=("times new roman", 10, "bold"))
        email_entry.grid(row=3, column=1, padx=10, pady=10, sticky="W")

        # Phone
        phone_label = tk.Label(class_Student_frame, text="Phone:", font=("times new roman", 10, "bold"))
        phone_label.grid(row=3, column=2, padx=10, pady=10, sticky="W")

        phone_entry = ttk.Entry(class_Student_frame, textvariable=self.var_phone, width=20, font=("times new roman", 10, "bold"))
        phone_entry.grid(row=3, column=3, padx=10, pady=10, sticky="W")

        # Address
        address_label = tk.Label(class_Student_frame, text="Address:", font=("times new roman", 10, "bold"))
        address_label.grid(row=4, column=0, padx=10, pady=10, sticky="W")

        address_entry = ttk.Entry(class_Student_frame, textvariable=self.var_address, width=20, font=("times new roman", 10, "bold"))
        address_entry.grid(row=4, column=1, padx=10, pady=10, sticky="W")

        # Teacher
        teacher_label = tk.Label(class_Student_frame, text="Teacher:", font=("times new roman", 10, "bold"))
        teacher_label.grid(row=4, column=2, padx=10, pady=10, sticky="W")

        teacher_entry = ttk.Entry(class_Student_frame, textvariable=self.var_teacher, width=20, font=("times new roman", 10, "bold"))
        teacher_entry.grid(row=4, column=3, padx=10, pady=10, sticky="W")

        #radio button
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="Take photo sample",value="yes")
        radiobtn1.grid(row=6,column=0)

        radiobtn1=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="No photo sample",value="yes")
        radiobtn1.grid(row=6,column=1)

        #button frame
        btn_frame=Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=715,height=70)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=17,font=("times new roman", 10, "bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="update",command=self.update_data,width=17,font=("times new roman", 10, "bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="delete",command=self.delete_data,width=17,font=("times new roman", 10, "bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="reset",command=self.reset_data,width=17,font=("times new roman", 10, "bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        take_photo_btn=Button(btn_frame,command=self.generate_dataset,text="Take Photo",width=17,font=("times new roman", 10, "bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=1,column=0)

        update_photo_btn=Button(btn_frame,text="update photo",width=17,font=("times new roman", 10, "bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=1,column=1)

        # Right side
        right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Detail", font=("times new roman", 20, "bold"), bg="white", fg="red")
        right_frame.place(x=780, y=10, width=720, height=570)

        # Search System
        search_frame = LabelFrame(right_frame, bd=2, relief=RIDGE, text="Search System", font=("times new roman", 20, "bold"), bg="white", fg="red")
        search_frame.place(x=5, y=10, width=710, height=70)

        search_label = Label(search_frame, text="Search By:", font=("times new roman", 15, "bold"), bg="red", fg="white")
        search_label.grid(row=0, column=0, padx=10, pady=10, sticky="W")

        search_combo = ttk.Combobox(search_frame, font=("times new roman", 13, "bold"), state="readonly", width=15)
        search_combo["values"] = ("Select", "Roll No.", "Phone No.")
        search_combo.current(0)  # Set the default value
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky="W")

        search_entry = ttk.Entry(search_frame, width=15, font=("times new roman", 13, "bold"))
        search_entry.grid(row=0, column=2, padx=10, pady=10, sticky="W")

        search_btn = Button(search_frame, text="Search", width=12, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        search_btn.grid(row=0, column=3, padx=10, pady=10)

        showAll_btn = Button(search_frame, text="Show All", width=12, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        showAll_btn.grid(row=0, column=4, padx=10, pady=10)

        # Table frame
        table_frame = Frame(right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=100, width=710, height=455)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, column=("dep", "course", "year", "sem", "id", "name", "div", "roll", "gender", "dob", "email", "phone", "address", "teacher", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="StudentID")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll", text="Roll")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="PhotoSampleStatus")
        self.student_table["show"] = "headings"

        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=150)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

   #function
    def add_data(self):
        if self.var_dep.get() == "" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="SouravGho@123", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("INSERT INTO student VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_id.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details have been added successfully")
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}")

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="SouravGho@123", database="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM student")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in rows:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_std_id.set(data[4])
        self.var_std_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher.set(data[13])
        self.var_radio1.set(data[14])

    # update data
    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                update = messagebox.askyesno("Update", "Do you want to update this student details?")
                if update > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="SouravGho@123", database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute("""
                        UPDATE student 
                        SET Dep=%s, Course=%s, Year=%s, Semester=%s, Name=%s, `Division`=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s 
                        WHERE Student_id=%s
                    """, (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get()
                    ))
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success", "Student details successfully updated", parent=self.root)
                else:
                    if not update:
                        return
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "Student id must be required")
        else:
            try:
                Delete = messagebox.askyesno("Delete", "Do you want to delete this student")
                if Delete > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="SouravGho@123", database="face_recognizer")
                    my_cursor = conn.cursor()
                    sql = "DELETE FROM student WHERE Student_id=%s"
                    val = (self.var_std_id.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "Successfully deleted student details")
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}")

    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")


# -----------------------------------generate data-------------------------------------
    def generate_dataset(self):
     if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
        messagebox.showerror("Error", "All fields are required", parent=self.root)
     else:
          try:
            conn = mysql.connector.connect(host="localhost", username="root", password="SouravGho@123", database="face_recognizer")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from student")
            myresult = my_cursor.fetchall()
            id = len(myresult)  # Fix to get the correct count of students
            my_cursor.execute("""
                UPDATE student 
                SET Dep=%s, Course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s 
                WHERE Student_id=%s
            """, (
                self.var_dep.get(),
                self.var_course.get(),
                self.var_year.get(),
                self.var_semester.get(),
                self.var_std_name.get(),
                self.var_div.get(),
                self.var_roll.get(),
                self.var_gender.get(),
                self.var_dob.get(),
                self.var_email.get(),
                self.var_phone.get(),
                self.var_address.get(),
                self.var_teacher.get(),
                self.var_radio1.get(),
                self.var_std_id.get()
            ))
            conn.commit()
            self.fetch_data()
            self.reset_data()
            
            conn.close()
            # Load predefined data
            face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

            def face_cropped(img):
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                # scaling factor=1.3
                # minimum neighbor=5
                for (x, y, w, h) in faces:
                    face_cropped = img[y:y + h, x:x + w]
                    return face_cropped
                return None
            cap = cv2.VideoCapture(0)
            img_id = 0
            while True:
                ret, my_frame = cap.read()
                if face_cropped(my_frame) is not None:
                    img_id += 1
                    face = cv2.resize(face_cropped(my_frame), (450, 450))
                    face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                    file_name_path = "data/user." + str(id) + "." + str(img_id) + ".jpg"
                    cv2.imwrite(file_name_path, face)
                    cv2.putText(face, str(img_id),(50,50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                    cv2.imshow("Cropped Face", face)
                if cv2.waitKey(1) == 13 or int(img_id) == 100:
                    break
            cap.release()
            cv2.destroyAllWindows()
            messagebox.showinfo("Result", "Generating Data sets Completed")
          except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}")


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()