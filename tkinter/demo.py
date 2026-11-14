# from tkinter import *

# win = Tk()

# # win.config(bg="red")
# # photo = PhotoImage(file="C:/Users/ssaty/Downloads/dog.png")

# # lb = Label(win, image=photo,bg="red", text="dog",compound="top", font=(30))
# # lb.place(x=50 ,y=50,height=100,width=50)

# menu = Menu(win)

# file = Menu(menu, tearoff=0)
# file.add_command(label = "New")
# file.add_checkbutton(label = "open")
# file.add_command(label = "save")
# file.add_separator()
# menu.add_cascade(label = "file", menu = file)
# win.config(menu=menu)
# win.mainloop()



from tkinter import *

def gmail():
    lb1.config(text=var.get())


win = Tk()

lb = Label(win, text="Email",font=("Times New Roman",30))
lb.place(x=100,y=100,height=50,width=100)

var = StringVar()
entry = Entry(win,font=80,cursor="plus",bd=8,textvariable=var)
entry.place(x=100,y=170,height=40,width=250)

button = Button(win, text="Ok",font=(60),command=gmail)
button.place(x=200,y=220)


lb1 = Label(win, text="",font=(100))
lb1.place(x=100,y=310,height=70,width=250)

win.mainloop()