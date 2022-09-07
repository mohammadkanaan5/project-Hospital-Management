from tkinter import *
import tkinter.messagebox 
import sqlite3
conn = sqlite3.connect('database.db')
c = conn.cursor()

class Application:
    def __init__(self, master):
        self.master = master
        self.master.title('التعديل والحذف')
        self.left = Frame(master, width=900, height=720, bg='#f2f2f2')
        self.left.pack(side=LEFT)
        # heading label
        self.h1 = Label(master, text="تعديل",  fg='steelblue', font=('arial 45 bold'))
        self.h1.place(x=300, y=0)

        # search  -->name
        self.name = Label(master, text="أدخل اسم المريض ", font=('arial 22 bold'))
        self.name.place(x=0, y=60)

        # entry for  the name
        self.namenet = Entry(master, width=40)
        self.namenet.place(x=250, y=80)

        # search button
        self.search = Button(master, text="بحث", width=12, height=1, bg='steelblue', command=self.search_db)
        self.search.place(x=250, y=102)
    # function to search
    def search_db(self):
        self.input = self.namenet.get()
        # execute sql 

        sql = "SELECT * FROM appointments WHERE name LIKE ?"
        self.res = c.execute(sql, (self.input,))
        for self.row in self.res:
            self.name1 = self.row[1]
            self.age = self.row[2]
            self.gender = self.row[3]
            self.location = self.row[4]
            self.time = self.row[6]
            self.phone = self.row[5]
        # creating the update form
        self.uname = Label(self.master, text="اسم المريض", font=('arial 18 bold'))
        self.uname.place(x=0, y=140)

        self.uage = Label(self.master, text="العمر", font=('arial 18 bold'))
        self.uage.place(x=0, y=180)

        self.ugender = Label(self.master, text="الجنس", font=('arial 18 bold'))
        self.ugender.place(x=0, y=220)

        self.ulocation = Label(self.master, text="المنطقة", font=('arial 18 bold'))
        self.ulocation.place(x=0, y=260)

        self.utime = Label(self.master, text="وقت الموعد", font=('arial 18 bold'))
        self.utime.place(x=0, y=300)

        self.uphone = Label(self.master, text=" رقم الهاتف", font=('arial 18 bold'))
        self.uphone.place(x=0, y=340)

        # entries for each labels
        # filling the search result in the entry box to update
        self.ent1 = Entry(self.master, width=30)
        self.ent1.place(x=150, y=140)
        self.ent1.insert(END, str(self.name1))

        self.ent2 = Entry(self.master, width=30)
        self.ent2.place(x=150, y=180)
        self.ent2.insert(END, str(self.age))

        self.ent3 = Entry(self.master, width=30)
        self.ent3.place(x=150, y=220)
        self.ent3.insert(END, str(self.gender))

        self.ent4 = Entry(self.master, width=30)
        self.ent4.place(x=150, y=260)
        self.ent4.insert(END, str(self.location))

        self.ent5 = Entry(self.master, width=30)
        self.ent5.place(x=150, y=300)
        self.ent5.insert(END, str(self.time))

        self.ent6 = Entry(self.master, width=30)
        self.ent6.place(x=150, y=340)
        self.ent6.insert(END, str(self.phone))

        # button to execute update
        self.update = Button(self.master, text="تعديل بيانات المريض", width=20, height=2, bg='lightblue', command=self.update_db)
        self.update.place(x=0, y=380)

        # button to delete
        self.delete = Button(self.master, text="حذف المريض", width=20, height=2, bg='red', command=self.delete_db)
        self.delete.place(x=170, y=380)
    def update_db(self):
        # declaring the variables to update
        self.var1 = self.ent1.get() #updated name
        self.var2 = self.ent2.get() #updated age
        self.var3 = self.ent3.get() #updated gender
        self.var4 = self.ent4.get() #updated location
        self.var5 = self.ent5.get() #updated phone
        self.var6 = self.ent6.get() #updated time

        query = "UPDATE appointments SET name=?, age=?, gender=?, location=?, phone=?, scheduled_time=? WHERE name LIKE ?"
        c.execute(query, (self.var1, self.var2, self.var3, self.var4, self.var5, self.var6, self.namenet.get(),))
        conn.commit()
        tkinter.messagebox.showinfo("Updated", "Successfully Updated.")
    def delete_db(self):
        # delete the appointment
        sql2 = "DELETE FROM appointments WHERE name LIKE ?"
        c.execute(sql2, (self.namenet.get(),))
        conn.commit()
        tkinter.messagebox.showinfo("Success", "Deleted Successfully")
        self.ent1.destroy()
        self.ent2.destroy()
        self.ent3.destroy()
        self.ent4.destroy()
        self.ent5.destroy()
        self.ent6.destroy()
# creating the object
root = Tk()
b = Application(root)
img4=PhotoImage(file='C:\\Users\mohammad\Desktop\Hospital-Management-System-f393dd892a538d26932278960cd83f8830f8ba2d\image7.png')
lab4=Label(root,image=img4 ,bg='green')
lab4.place(x=350,y=110 ,width=350,height=325)

root.geometry("700x500+200+200")
root.resizable(True, False)
root.mainloop()