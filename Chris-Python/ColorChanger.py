from Tkinter import *

app=Tk()
app.title('Color Changer')
app.geometry('220x150')
def cmd():
    red=txtR.get()
    green=txtG.get()
    blue=txtB.get()
    mycolor='#%02x%02x%02x' % (int(red),int(green),int(blue))
    cFrame=Frame(width=80,height=80,bg=mycolor)
    cFrame.place(x=12,y=30)

lblTitle=Label(app,text="Color Changer")
lblTitle.pack(side=TOP)
    
mycolor = '#%02x%02x%02x' % (0, 0, 0)
cFrame=Frame(app,width=80,height=80,bg=mycolor)
cFrame.place(x=12,y=30)

btnGo = Button(app,text="GO!", command=cmd)
btnGo.place(x=150,y=115)

txtR = Entry(app, text='', width=5)
txtR.place(x=150,y=35)
red=txtR.get()

lblR = Label(app,text="Red")
lblR.place(x=110,y=35)

txtG = Entry(app, text='', width=5)
txtG.place(x=150,y=60)
green=txtG.get()

lblG = Label(app,text="Green")
lblG.place(x=110,y=60)

txtB = Entry(app, text='', width=5)
txtB.place(x=150,y=85)
blue=txtB.get()

lblB = Label(app,text="Blue")
lblB.place(x=110,y=85)

mainloop()
