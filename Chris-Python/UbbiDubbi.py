from Tkinter import *
def insert(original, new, pos):
    return original[:pos] + new + original[pos:] 
def cmd():
    vowels=['a','e','i','o','u','y']
    newsent=''
    sent=txt.get()
    newsent=list(sent)
    if 'a' in sent:
        newsent.insert(sent.find('a',8),'ub')
        newsent.insert(sent.find('a',2),'ub')
        newsent.insert(sent.find('a'),'ub')
    elif 'e' in sent:
        newsent.insert(sent.find('e',8),'ub')
        newsent.insert(sent.find('e',2),'ub')
        newsent.insert(sent.find('e'),'ub')
    print ''.join(newsent)
    
app=Tk()
app.title('Ubbi Dubbi')

btn1= Button(app,text='Go!', command=cmd)
btn1.pack(side=BOTTOM)

txt=Entry(app)
txt.pack()

mainloop()

