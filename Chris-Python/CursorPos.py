import Tkinter

class App:
    def __init__(self, root):
        f = Tkinter.Frame(width=110, height=100, background="white")
        f.pack(padx=0, pady=0)
        f.bind("<1>", self.OnMouseDown)

    def OnMouseDown(self, event):
        print "root coordinates: (%s,%s)" % (event.x_root, event.y_root)

root=Tkinter.Tk()
app = App(root)
root.mainloop()


