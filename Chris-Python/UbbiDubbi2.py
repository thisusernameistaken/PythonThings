from Tkinter import *
def insert(original, new, pos):
    return original[:pos] + new + original[pos:] 
def cmd():
    vowels=['a','e','i','o','u','y']
    newsent=''
    sent=txt.get()
    for letter in sent:
        if letter =='a':
             newsent+='uba'
        elif letter =='e':
             newsent+='ube'
        elif letter =='i':
             newsent+='ubi'
        elif letter =='o':
             newsent+='ubo'
        elif letter =='u':
             newsent+='ubu'
        else:
            newsent+=letter   
    print ''.join(newsent)
    
app=Tk()
app.title('Ubbi Dubbi')

btn1= Button(app,text='Go!', command=cmd)
btn1.pack(side=BOTTOM)

txt=Entry(app)
txt.pack()

mainloop()

