from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import time
import datetime
import random
from main import FaceRecognitionSystem

def main():
    win = Tk()
    app = login_window(win)
    win.mainloop()



class login_window:
   def __init__(self, root):
      self.root = root
      self.root.title('login')
      self.root.geometry('1550x1200+0+0')

      self.bg = ImageTk.PhotoImage(file=r'images2\\bg_image.jpg')

      label_bg = Label(self.root, image=self.bg)
      label_bg.place(x=0, y=0,relwidth=1, relheight=1)

      frame = Frame(self.root, bg='black')
      frame.place(x=560, y=170, width=340, height=450)

      img1 = Image.open(r"images2\\logo1.png")
      img1 = img1.resize((100, 100))
      self.photoImage1 = ImageTk.PhotoImage(img1)

      labelimg1 = Label(image=self.photoImage1, bg='black', borderwidth=0)
      labelimg1.place(x=690, y=175, width=100, height=100)

      get_str = Label(frame, text="Get Started", font=("times new roman", 23, "bold"), fg="white", bg="black")
      get_str.place(x=90, y=100)

      # label
      username_lbl = Label(frame, text="Username", font=("times new roman", 15, "bold"), fg="white", bg="black")
      username_lbl.place(x=70, y=155)

      self.txtuser= ttk.Entry(frame,  font=("times new roman", 15, "bold"))
      self.txtuser.place(x=40, y=180, width=250)

      password1 = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="white", bg="black")
      password1.place(x=70, y=225)

      self.txtpass= ttk.Entry(frame,  font=("times new roman", 15, "bold"))
      self.txtpass.place(x=40, y=250, width=250)

      # ---------- Icon image---------------
      img2 = Image.open(r"images2\\logo1.png")
      img2 = img2.resize((25, 25))
      self.photoImage2 = ImageTk.PhotoImage(img2)

      labelimg2 = Label(image=self.photoImage2, bg='black', borderwidth=0)
      labelimg2.place(x=600, y=325, width=25, height=25)
     
      img3 = Image.open(r"images2\\password_icon.png")
      img3 = img3.resize((25, 25))
      self.photoImage3 = ImageTk.PhotoImage(img3)

      labelimg3 = Label(image=self.photoImage3, bg='black', borderwidth=0)
      labelimg3.place(x=600, y=390, width=25, height=25)

      # ---------- login button-----------
      loginbutton = Button(frame, text='Login',command=self.login, font=("times new roman", 15, "bold"), bd=3, relief=RIDGE, fg='white', bg='red', activebackground='red', activeforeground='white')
      loginbutton.place(x=110, y=300, width=110, height=35)

      # ----------- register button--------
      
      registerbutton = Button(frame, text='New user Register ?', command=self.register_window, font=("times new roman", 10, "bold"),borderwidth=0, fg='white', bg='black', activebackground='black', activeforeground='white')
      registerbutton.place(x=20, y=350, width=160)

      # ------------ forget password button ------------
      forgetbutton = Button(frame, text='Forget Password', command=self.forget_password_window, font=("times new roman", 10, "bold"), borderwidth=0, fg='white', bg='black', activebackground='black', activeforeground='white')
      forgetbutton.place(x=10, y=380, width=160)

   
   # ===================== register ===================
   def register_window(self):
      self.new_window=Toplevel(self.root)
      self.app=Register(self.new_window)


# ================ login =================
   def login(self):
      if self.txtuser.get() == '' or self.txtpass.get() == '':
         messagebox.showerror('Error', "All field required")
      elif self.txtuser.get() == 'admin' and self.txtpass.get() == 'root':
         messagebox.showinfo('Success', 'Welcome to Facial recognition System')
      else:
         conn = mysql.connector.connect(host="localhost", user="root", password="T#90addd", database="myData")
         my_cursor = conn.cursor()
         my_cursor.execute("select * from register where email = %s and password = %s",(
                                                                                       self.txtuser.get(),
                                                                                       self.txtpass.get()
                                                                                    ))

         row = my_cursor.fetchone()
         if row == None:
            messagebox.showerror("Error","Invalid username and password")
         else:
            open_main = messagebox.askyesno("yesNo","Access only admin")
            if open_main>0:
               self.new_window=Toplevel(self.root)
               self.app=FaceRecognitionSystem(self.new_window)
            else:
               if not open_main:
                  return 

         conn.commit()
         conn.close()



# =============== reset password ============
   def reset_password(self):
      if self.combo_security_Q.get()=='Select':
         messagebox.showerror('Error',"Select security Question", parent=self.root2)
      elif self.txt_security.get() == "":
         messagebox.showerror('Error',"Please enter the number", parent=self.root2)
      elif self.txt_newpass.get()=='':
         messagebox.showerror('Error',"Please enter the new password", parent=self.root2)
      else:
         conn = mysql.connector.connect(host="localhost", user="root", password="T#90addd", database="myData")
         my_cursor = conn.cursor()
         query = ("select * from register where email = %s and securityQ=%s and securityA=%s")
         value = (self.txtuser.get(),self.combo_security_Q.get(), self.txt_security.get(),)
         my_cursor.execute(query, value)
         row=my_cursor.fetchone()
         if row == None:
            messagebox.showerror("Error", "Please enter the correct answer", parent=self.root2)
         else:
            query = ("update register set password=%s where email=%s") 
            value=(self.txt_newpass.get(), self.txtuser.get())
            my_cursor.execute(query, value)

            conn.commit()
            conn.close()
            messagebox.showinfo("Info", "Your password has been reset, please login with new password", parent=self.root2)
            self.root2.destroy()


   # ============ forget Password window =============
   def forget_password_window(self):
      if self.txtuser.get() == "":
         messagebox.showerror("Error","Please enter the email address to reset the password")
      else:
         conn = mysql.connector.connect(host="localhost", user="root", password="T#90addd", database="myData")
         my_cursor = conn.cursor()
         query = ("select * from register where email = %s")
         value = (self.txtuser.get(),)
         my_cursor.execute(query, value)
         row = my_cursor.fetchone()
         # print(row)

         if row== None:
            messagebox.showerror("My Error", "Please enter the valid username")
         else:
            conn.close()
            self.root2=Toplevel()
            self.root2.title('Forget Password')
            self.root2.geometry("340x450+610+170")

            l = Label(self.root2, text="Forget Password", font=("times new roman", 20, "bold"), bg="white", fg='red')
            l.place(x=0, y=10, relwidth=1)

            security_Q = Label(self.root2, text="Select Scurity Questions", font=("times new roman", 15, "bold"), bg="white", fg='black')
            security_Q.place(x=50, y=80)

            self.combo_security_Q= ttk.Combobox(self.root2, font=("times new roman", 15, 'bold'), state='readonly')
            self.combo_security_Q['values'] = ('Select', 'What is your birth place', 'Your gender')
            self.combo_security_Q.place(x=50, y=110, width=250)
            self.combo_security_Q.current(0)

            Security_A = Label(self.root2, text="Security Answer", font=("times new roman", 15, "bold"), bg="white", fg='black')
            Security_A.place(x=50, y=150)

            self.txt_security= ttk.Entry(self.root2, font=("times new roman", 15))
            self.txt_security.place(x=50, y=180, width=250)

            new_password = Label(self.root2, text="New Passwod", font=("times new roman", 15, "bold"), bg="white", fg="black")
            new_password.place(x=50, y=220)

            self.txt_newpass= ttk.Entry(self.root2, font=("times new roman", 15))
            self.txt_newpass.place(x=50, y=250, width=250)

            bt = Button(self.root2, text='reset', command=self.reset_password, font=("times new roman", 15, "bold"), bg='green', fg='white')
            bt.place(x=130, y=290)






class Register:
   def __init__(self, root):
      self.root = root
      self.root.title('Register')
      self.root.geometry("1700x800+0+0")

      # ================= variables ==============
      self.var_fname = StringVar()
      self.var_lname = StringVar()
      self.var_contact = StringVar()
      self.var_email = StringVar()
      self.var_securityQ = StringVar()
      self.var_securityA= StringVar()
      self.var_pass = StringVar()
      self.var_confpass = StringVar()
      self.var_check = IntVar()

      # ---------- Background Image-----------
      self.bg = ImageTk.PhotoImage(file=r'images2\\bg_image2.png')
      label_bg1 = Label(self.root, image=self.bg)
      label_bg1.place(x=0, y=0,relwidth=1, relheight=1)

      # ============m left image ===============
      self.bg1 = ImageTk.PhotoImage(file=r'images2\\image3.png')
      label_bg2 = Label(self.root, image=self.bg1)
      label_bg2.place(x=50, y=100,width=460, height=550)

      # --------------- main frame ---------------
      frame = Frame(self.root, bg='white')
      frame.place(x=510, y=100, width=780, height=550)

       # label
      register_lbl = Label(frame, text="REGISTER HERE", font=("times new roman", 20, "bold"), fg="darkgreen", bg="white")
      register_lbl.place(x=20, y=10)

      # ======================= label entry =====================

      # ---------------------- row1
      fname = Label(frame, text="First Name", font=("times new roman", 15, "bold"), bg="white")
      fname.place(x=50, y=100)

      self.fname_entry = ttk.Entry(frame, textvariable= self.var_fname, font=("times new roman", 15))
      self.fname_entry.place(x=50, y=130, width=250)

      lname = Label(frame, text="Last Name", font=("times new roman", 15, "bold"), bg="white")
      lname.place(x=370, y=100)

      self.txt_lname= ttk.Entry(frame,textvariable=self.var_lname, font=("times new roman", 15))
      self.txt_lname.place(x=370, y=130, width=250)

      # ---------------------- row2
      contact = Label(frame, text="Contact Me", font=("times new roman", 15, "bold"), bg="white", fg='black')
      contact.place(x=50, y=170)

      self.txt_contact= ttk.Entry(frame,textvariable=self.var_contact,  font=("times new roman", 15))
      self.txt_contact.place(x=50, y=200, width=250)

      email = Label(frame, text="Email", font=("times new roman", 15, "bold"), bg="white")
      email.place(x=370, y=170)

      self.txt_email= ttk.Entry(frame,textvariable=self.var_email,  font=("times new roman", 15))
      self.txt_email.place(x=370, y=200, width=250)

      # ---------------------- row3
      security_Q = Label(frame, text="Select Scurity Questions", font=("times new roman", 15, "bold"), bg="white", fg='black')
      security_Q.place(x=50, y=240)

      self.combo_security_Q= ttk.Combobox(frame,textvariable=self.var_securityQ,  font=("times new roman", 15, 'bold'), state='readonly')
      self.combo_security_Q['values'] = ('Select', 'What is your birth place', 'Your gender')
      self.combo_security_Q.place(x=50, y=270, width=250)
      self.combo_security_Q.current(0)

      Security_A = Label(frame, text="Security Answer", font=("times new roman", 15, "bold"), bg="white", fg='black')
      Security_A.place(x=370, y=270)

      self.txt_scurity= ttk.Entry(frame, textvariable=self.var_securityA, font=("times new roman", 15))
      self.txt_scurity.place(x=370, y=270, width=250)

      # ---------------------- row4
      pswd = Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white", fg='black')
      pswd.place(x=50, y=310)

      self.txt_pswd= ttk.Entry(frame, textvariable=self.var_pass, font=("times new roman", 15, "bold"))
      self.txt_pswd.place(x=50, y=340, width=250)

      confirm_pswd = Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white", fg='black')
      confirm_pswd.place(x=370, y=310)

      self.txt_lname= ttk.Entry(frame, textvariable=self.var_confpass, font=("times new roman", 15, "bold"))
      self.txt_lname.place(x=370, y=340, width=250)

      # --------------- ROW5  WITH Check button
      checkbtn = Checkbutton(frame, variable=self.var_check, text='I agree the terms & condition', font=("times new roman", 12, "bold"), fg='black', onvalue=1, offvalue=0)
      checkbtn.place(x=50, y= 380)

      # ================ Butttons============================
      img1 = Image.open(r"images2\\register.png")
      img1 = img1.resize((200, 70))
      self.photoImage1 = ImageTk.PhotoImage(img1)
      b1 = Button(frame, image=self.photoImage1,command=self.registerData, borderwidth=0, cursor='hand2', font=("times new roman", 15, "bold"))
      b1.place(x=50, y=420, width=200)


      img2 = Image.open(r"images2\\login.png")
      img2 = img2.resize((200, 70))
      self.photoImage2 = ImageTk.PhotoImage(img2)
      b2 = Button(frame, image=self.photoImage2,command=self.return_login, borderwidth=0, cursor='hand2', font=("times new roman", 15, "bold"))
      b2.place(x=370, y=420, width=200)


   # ============== function declaration ==============
   def registerData(self):
      if self.var_fname.get() == '' or self.var_email.get() == '' or self.var_securityQ.get() == 'Select':
         messagebox.showerror('Error', 'All fields are required', parent=self.root)
      elif self.var_pass.get() != self.var_confpass.get():
         messagebox.showerror('Error', 'Password and confirm password must be same', parent=self.root)
      elif self.var_pass.get() == '' or len(self.var_pass.get()) < 6:
         messagebox.showerror('Error', "Password must be given & not less then 6 character", parent=self.root)
      elif self.var_check.get() == 0:
         messagebox.showerror('Error', 'Please agree the terms and conditions', parent=self.root)
      else:
         conn = mysql.connector.connect(host="localhost", user="root", password="T#90addd", database="myData")
         my_cursor = conn.cursor()
         query=("select * from register where email=%s")
         value =(self.var_email.get(),)
         my_cursor.execute(query, value)
         row = my_cursor.fetchone()
         if row!= None:
            messagebox.showerror("Error", "User alredy exist, Please try with another email", parent=self.root)
         else:
            my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                       self.var_fname.get(),
                                                                                       self.var_lname.get(),
                                                                                       self.var_contact.get(),
                                                                                       self.var_email.get(),
                                                                                       self.var_securityQ.get(),
                                                                                       self.var_securityA.get(),
                                                                                       self.var_pass.get()
                                                                                    ))
         conn.commit()
         conn.close()
         messagebox.showinfo("Success", "Register Successfully", parent=self.root)
         self.root.destroy()


   def return_login(self):
      self.root.destroy()



# ============================= Add any project class here ===================
class Example:
   def __init__(self, root):
      self.root = root
      self.root.title('Example')
      self.root.geometry('1550x1200+0+0')

      self.bg4 = ImageTk.PhotoImage(file=r'images2\\bg_image.jpg')

      label_bg4 = Label(self.root, image=self.bg4)
      label_bg4.place(x=0, y=0,relwidth=1, relheight=1)



if __name__ == '__main__':
   main()