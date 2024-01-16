
import tkinter
from tkinter import*


class ParentWindow(Frame):
    def __init__ (self, master, *args, **kwargs):
        Frame.__init__ (self)

        self.master = master.self.master.resizable(width=False, height =False)
        self.master.geometry('()x()').format(700, 400)
        self.master.title("Learning Tkinter!")

        self.varFName = StringVar()
        self.varLName = StringVar()
        self.varFName.set("Bob")
        self.varLName.set("Smith")

        print(self.varFName.get())
        print(self.varLName.get())

        self.lblFName = Label(self.master,text=self.varFName, font=("Hevletica", 16), fg="black", bg="lightblue" )
        self.lblFName.grid(row=0, column=0)

        self.lblLName = Label(self.master,text=self.varLName, font=("Hevletica", 16), fg="black", bg="lightblue" )
        self.lblLName.grid(row=0, column=0)

        self.txtFName = Entry(self.master,text=self.varFName, font=("Hevletica", 16), fg="black", bg="lightblue" )
        self.txtFName.grid(row="", column="")

        self.txtLName = Entry(self.master,text=self.varLName, font=("Hevletica", 16), fg="black", bg="lightblue" )
        self.txtLName.grid(row="", column="")












if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
