from tkinter import *
import sqlite3
import pyttsx3
# connection to database
conn = sqlite3.connect('database.db')
c = conn.cursor()
# empty lists to append later
number = []
patients = []
sql = "SELECT * FROM appointments"
res = c.execute(sql)
for r in res:
    ids = r[0]
    name = r[1]
    number.append(ids)
    patients.append(name)
# window
class Application:
    def __init__(self, master):
        self.master = master
        self.master.title('القائمة')
        self.x = 0
        # heading
        self.left = Frame(master, width=800, height=650, bg='#ff3399')
        self.left.pack(side=LEFT)
        self.heading = Label(master, text="المرضى", font=('arial 60 bold'), fg='#660000')
        self.heading.place(x=100, y=0)
        # self.title('')

        # button to change patients
        self.change = Button(master, text="المريض التالي", width=25, height=2, bg='#ffff00', command=self.func)
        self.change.place(x=325, y=120)

        # empty text labels to later config
        self.n = Label(master, text="الرقم",bg='#ff0000', font=('arial 30 bold'))
        self.n.place(x=0, y=100)

        self.pname = Label(master, text="الاسم", font=('arial 30 bold'), bg='#ff0000')

        self.pname.place(x=100, y=100)

    # function to speak the text and update the text

    def func(self):
        self.n.config(text=str(number[self.x]))
        self.pname.config(text=str(patients[self.x]))
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        rate = engine.getProperty('rate')
        engine.setProperty('rate', rate-100)
        engine.say('Patient number ' + str(number[self.x]) + str(patients[self.x]))
        engine.runAndWait()
        self.x += 1
root = Tk()

b = Application(root)
img3=PhotoImage(file='C:\\Users\mohammad\Desktop\Hospital-Management-System-f393dd892a538d26932278960cd83f8830f8ba2d\image5.png')
lab2=Label(root,image=img3 ,bg='red')
lab2.place(x=0,y=160 ,width=550,height=330)
root.geometry("550x500+0+0")
root.resizable(False, False)
root.mainloop()
