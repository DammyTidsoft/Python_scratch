from tkinter import *
root = Tk()
#using label in python
'''
thelable1 = Label(root, text="You are Welcome")
thelable1.pack()
'''
#using button in oython
topForm = Frame(root)
topForm.pack()
buttonFrame = Frame(root)
buttonFrame.pack(side=BOTTOM)

button1 = Button(topForm, text="Button 1", fg="blue")
button2 = Button(topForm, text="Button 2", fg="red")
button3 = Button(topForm, text="Button 3", fg="yellow")
button4 = Button(topForm, text="Button 4", fg="pink")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)

root.mainloop()
