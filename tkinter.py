from Tkinter import *

app = Tk()
app.title('alarm')
app.geometry('800x500+200+200')

label = Label(app,text="Enter Your Current Hour").pack()
textbox = Entry().pack()

label1 = Label(app,text="Enter Your Current Minute").pack()
textbox1 = Entry().pack()

labe2 = Label(app,text="Enter Your Alarm Hour").pack()
textbox2 = Entry().pack()

label3 = Label(app,text="Enter Your Alarm Minute").pack()
textbox3 = Entry().pack()

button = Button(app,text="Click here to Run").pack()

app.mainloop()
