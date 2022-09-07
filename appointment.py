from tkinter import *
import sqlite3
import tkinter.messagebox

#connect to the databse.
conn = sqlite3.connect('database.db')
# cursor to move around the databse
c = conn.cursor()
# empty list to later append the ids from the database
ids = []

# tkinter window
class Application:
    def __init__(self, master):
        self.master = master
        self.master.title('القائمة الاساسية')
        # creating the frames in the master
        self.left = Frame(master, width=900, height=720, bg='#002db3')
        self.left.pack(side=LEFT)

        self.right = Frame(master, width=300, height=500, bg='steelblue')
        self.right.pack(side=RIGHT)

        # labels for the window
        self.heading = Label(self.left, text="مواعيد مشفى السلامة", font=('arial 40 bold'), fg='black', bg='#ffff1a')
        self.heading.place(x=160, y=0)
        # patients name
        self.name = Label(self.left, text="اسم المريض", font=('arial 18 bold'), fg='black', bg='lightgreen')
        self.name.place(x=20, y=100)

        # age
        self.age = Label(self.left, text="العمر", font=('arial 18 bold'), fg='black', bg='lightgreen')
        self.age.place(x=20, y=140)

        # gender
        self.gender = Label(self.left, text="الجنس", font=('arial 18 bold'), fg='black', bg='lightgreen')
        self.gender.place(x=20, y=180)

        # location
        self.location = Label(self.left, text="المنطقة", font=('arial 18 bold'), fg='black', bg='lightgreen')
        self.location.place(x=20, y=220)

        # appointment time
        self.time = Label(self.left, text="وقت الموعد", font=('arial 18 bold'), fg='black', bg='lightgreen')
        self.time.place(x=20, y=260)

        # phone
        self.phone = Label(self.left, text="رقم الهاتف", font=('arial 18 bold'), fg='black', bg='lightgreen')
        self.phone.place(x=20, y=300)
        # Entries for all labels=============
        self.name_ent = Entry(self.left, width=30)
        self.name_ent.place(x=150, y=100)

        self.age_ent = Entry(self.left, width=30)
        self.age_ent.place(x=150, y=140)
    
        self.gender_ent = Entry(self.left, width=30)
        self.gender_ent.place(x=150, y=180)

        self.location_ent = Entry(self.left, width=30)
        self.location_ent.place(x=150, y=220)

        self.time_ent = Entry(self.left, width=30)
        self.time_ent.place(x=150, y=260)

        self.phone_ent = Entry(self.left, width=30)
        self.phone_ent.place(x=150, y=300)

        # button to perform a command
        self.submit = Button(self.left, text="حجز موعد",font=('arial 10 bold'), width=20, height=2, bg='#ffff1a', command=self.add_appointment)
        self.submit.place(x=380, y=200)
    
        # getting the number of appointments fixed to view in the log
        sql2 = "SELECT ID FROM appointments "

        self.result = c.execute(sql2)

        for self.row in self.result:
            self.id = self.row[0]
            ids.append(self.id)
        
        # ordering the ids
        self.new = sorted(ids)

        self.final_id = self.new[len(ids)-1]

        # displaying the logs in our right frame
        self.logs = Label(self.right, text="السجل", font=('arial 28 bold'), fg='white', bg='steelblue')
        self.logs.place(x=0, y=0)

        self.box = Text(self.right, width=24, height=10)
        self.box.place(x=0, y=60)
        self.box.insert(END,"the total number:  " + str(self.final_id))
    # funtion to call when the submit button is clicked
    def add_appointment(self):
        # getting the user inputs
        self.val1 = self.name_ent.get()
        self.val2 = self.age_ent.get()
        self.val3 = self.gender_ent.get()
        self.val4 = self.location_ent.get()
        self.val5 = self.time_ent.get()
        self.val6 = self.phone_ent.get()

        # checking if the user input is empty
        if self.val1 == '' or self.val2 == '' or self.val3 == '' or self.val4 == '' or self.val5 == '':
            tkinter.messagebox.showinfo("Warning", "Please Fill Up All Boxes")
        else:
            # now we add to the database
            sql = "INSERT INTO 'appointments' (name, age, gender, location, scheduled_time, phone) VALUES(?, ?, ?, ?, ?, ?)"
            c.execute(sql, (self.val1, self.val2, self.val3, self.val4, self.val5, self.val6))
            conn.commit()
            tkinter.messagebox.showinfo("Success", "Appointment for " +str(self.val1) + " has been created" )
            

            self.box.insert(END, 'Appointment fixed for ' + str(self.val1) + ' at ' + str(self.val5))

 # creating the object
master= Tk()
b = Application(master)
img=PhotoImage(file='C:\\Users\mohammad\Desktop\Hospital-Management-System-f393dd892a538d26932278960cd83f8830f8ba2d\image.png')
lab=Label(master,image=img ,bg='green')
lab.place(x=-20,y=330 ,width=1200,height=300)
img2=PhotoImage(file='C:\\Users\mohammad\Desktop\Hospital-Management-System-f393dd892a538d26932278960cd83f8830f8ba2d\imag2.png')
lab1=Label(master,image=img2 ,bg='green')
lab1.place(x=550,y=3 ,width=350,height=325)
# resolution of the window
master.geometry("1100x620+0+0")

master.resizable(False, False)

# end the loop
master.mainloop()