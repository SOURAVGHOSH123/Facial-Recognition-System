from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata = []
class Attendence:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # ============= Variables ================
        self.var_atten_id = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendence = StringVar()

        # first image
        img = Image.open(r"images\smart_attendence.jpg")
        img = img.resize((700, 200), Image.LANCZOS)  # Corrected here
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=700, height=200)

        # second image
        img1 = Image.open(r"images//clg.jpg")
        img1 = img1.resize((700, 200), Image.LANCZOS)  # Corrected here
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=700, y=0, width=700, height=200)

        # background image
        img3 = Image.open(r"images//clg.jpg")
        img3 = img3.resize((1520, 710), Image.LANCZOS)  # Corrected here
        self.bg_photoimg = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.bg_photoimg)
        bg_img.place(x=0, y=200, width=1520, height=710)

        # Title
        title_lbl = Label(self.root, text="Attendence Management System", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=200, width=1530, height=45)

        # Main frame
        main_frame = Frame(self.root, bd=2, bg="white")
        main_frame.place(x=15, y=250, width=1400, height=560)

        # Left side
        left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Attendence Detail", font=("times new roman", 20, "bold"), bg="white", fg="red")
        left_frame.place(x=10, y=10, width=700, height=570)

        left_inside_frame = Frame(left_frame, bd=2, bg="white", relief=RIDGE)
        left_inside_frame.place(x=0, y=20, width=680, height=370)

        # Label and entry fields
        attendenceId_label = tk.Label(left_inside_frame, text="Attendence ID:", font=("times new roman", 12, "bold"), bg="white")
        attendenceId_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        attendenceId_entry = tk.Entry(left_inside_frame, textvariable=self.var_atten_id, width=20, font=("times new roman", 10, "bold"))
        attendenceId_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Roll
        roll_label = tk.Label(left_inside_frame, text="Roll:", font=("times new roman", 12, "bold"), bg="white")
        roll_label.grid(row=0, column=2, padx=4, pady=8)

        atten_roll = tk.Entry(left_inside_frame, textvariable=self.var_atten_roll, width=20, font=("times new roman", 10, "bold"))
        atten_roll.grid(row=0, column=3, pady=8)

        # Name
        nameLabel = tk.Label(left_inside_frame, text="Name:", font=("times new roman", 12, "bold"), bg="white")
        nameLabel.grid(row=1, column=0)

        atten_name = tk.Entry(left_inside_frame, textvariable=self.var_atten_name, width=20, font=("times new roman", 10, "bold"))
        atten_name.grid(row=1, column=1, pady=8)

        # Department
        depLabel = tk.Label(left_inside_frame, text="Department:", font=("times new roman", 12, "bold"), bg="white")
        depLabel.grid(row=1, column=2)

        atten_dep = tk.Entry(left_inside_frame, textvariable=self.var_atten_dep, width=20, font=("times new roman", 10, "bold"))
        atten_dep.grid(row=1, column=3, pady=8)

        # Time
        timeLabel = tk.Label(left_inside_frame, text="Time:", font=("times new roman", 12, "bold"), bg="white")
        timeLabel.grid(row=2, column=0)

        atten_time = tk.Entry(left_inside_frame, textvariable=self.var_atten_time, width=20, font=("times new roman", 10, "bold"))
        atten_time.grid(row=2, column=1, pady=8)

        # Date
        dateLabel = tk.Label(left_inside_frame, text="Date:", font=("times new roman", 12, "bold"), bg="white")
        dateLabel.grid(row=2, column=2)

        atten_date = tk.Entry(left_inside_frame, textvariable=self.var_atten_date, width=15, font=("times new roman", 10, "bold"))
        atten_date.grid(row=2, column=3, pady=8)

        # Attendence
        attendenceLabel = tk.Label(left_inside_frame, text="Attendence label", font=("times new roman", 12, "bold"), bg="white")
        attendenceLabel.grid(row=3, column=0)

        self.atten_status = ttk.Combobox(left_inside_frame, textvariable=self.var_atten_attendence, width=20, font=("times new roman", 10, "bold"), state="readonly")
        self.atten_status["values"] = ("Status", "Present", "Absent")
        self.atten_status.grid(row=3, column=1, pady=8)
        self.atten_status.current(0)

        # Button frame
        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=310, width=715, height=70)

        save_btn = Button(btn_frame, text="Import csv", command=self.importCsv, width=17, font=("times new roman", 10, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text="Export csv", command=self.exportCsv, width=17, font=("times new roman", 10, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="Update", width=17,font=("times new roman", 10, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, width=17, font=("times new roman", 10, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)

        # Right side
        right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Attendence Detail", font=("times new roman", 20, "bold"), bg="white", fg="red")
        right_frame.place(x=720, y=10, width=615, height=450)

        # Table frame
        table_frame = Frame(right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=5, width=600, height=380)

        # Scroll bar table
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendenceReportTable = ttk.Treeview(table_frame, column=("id", "roll", "name", "department", "time", "date", "attendence"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.AttendenceReportTable.xview)
        scroll_y.config(command=self.AttendenceReportTable.yview)

        self.AttendenceReportTable.heading("id", text="Attendence ID")
        self.AttendenceReportTable.heading("roll", text="Roll")
        self.AttendenceReportTable.heading("name", text="Name")
        self.AttendenceReportTable.heading("department", text="Department")
        self.AttendenceReportTable.heading("time", text="Time")
        self.AttendenceReportTable.heading("date", text="Date")
        self.AttendenceReportTable.heading("attendence", text="Attendence")

        self.AttendenceReportTable["show"] = "headings"
        self.AttendenceReportTable.column("id", width=100)
        self.AttendenceReportTable.column("roll", width=100)
        self.AttendenceReportTable.column("name", width=100)
        self.AttendenceReportTable.column("department", width=100)
        self.AttendenceReportTable.column("time", width=100)
        self.AttendenceReportTable.column("date", width=100)
        self.AttendenceReportTable.column("attendence", width=100)

        self.AttendenceReportTable.pack(fill=BOTH, expand=1)

        self.AttendenceReportTable.bind("<ButtonRelease>", self.get_cursor)

    # ===================Fetch data=====================
    def fetchData(self, rows):
        self.AttendenceReportTable.delete(*self.AttendenceReportTable.get_children())
        for i in rows:
            self.AttendenceReportTable.insert("", END, values=i)

    # Import CSV
    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    # Export CSV
    def exportCsv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("No Data", "No data found to export", parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
            with open(fln, mode="w", newline="") as myfile:
                export_write = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    export_write.writerow(i)
                messagebox.showinfo("Data Export", f"Your data exported to {os.path.basename(fln)} successfully")
        except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    def get_cursor(self, event=""):
        cursor_row = self.AttendenceReportTable.focus()
        content = self.AttendenceReportTable.item(cursor_row)
        data = content["values"]
        self.var_atten_id.set(data[0])
        self.var_atten_roll.set(data[1])
        self.var_atten_name.set(data[2])
        self.var_atten_dep.set(data[3])
        self.var_atten_time.set(data[4])
        self.var_atten_date.set(data[5])
        self.var_atten_attendence.set(data[6])

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendence.set("Status")


if __name__ == "__main__":
    root = Tk()
    obj = Attendence(root)
    root.mainloop()