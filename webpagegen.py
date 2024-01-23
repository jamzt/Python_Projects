import tkinter as Tk
from tkinter import *
import webbrowser

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")
    
        self.btn = Button(text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.btn.grid(padx=(10,10), pady=(10,10))

        #entry widget
        self.cstm_entry = Entry(width=40)
        self.cstm_entry.grid(row=1, column=0, columnspan=2, padx=(10,10), pady=(0, 10)) 

        self.btn_cstm = Button(text="Custom HTML Page", width=30, height=2, command=self.customHTML)
        self.btn_cstm.grid(row=2, column=0, columnspan=2, padx=(10, 10), pady=(10, 10))

    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

    def customHTML(self):
        user_input = self.cstm_entry.get()
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + user_input + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()

#input field in the GUI 45
    