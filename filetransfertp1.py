import tkinter as tk
from tkinter import *
import tkinter.filedialog
import os
import shutil
import datetime
import timedelta

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        #Sets title of GUI window
        self.master.title("File Transfer")

        #create button to select files from source dir
        self.sourceDir_btn = Button(text="Select Source", width=20, command=self.sourceDir)
        
        #positions source button in GUI using tkinter grid()
        self.sourceDir_btn.grid(row=0, column=0, padx=(20, 10), pady=(30,0))

        #creates entry for source dir slection
        self.source_dir = Entry(self, width=75)
        #positions entry in GUI using tkinter grid()padx and pady are teh same as
        #the button to ensure they will line up
        self.source_dir.grid(row=0, column=1, columnspan=2, padx=(20, 10), pady=(30,0))

        #create button to select destination of files from destination dir
        self.destDir_btn = Button(text="Select Destination", width=20, command=self.destDir)
        #positions source button in GUI using tkinter grid()
        self.destDir_bin.grid(row=1, column=0, padx=(20, 10), pady=(15,10))

        #creates entry for destiantion dir selection
        self.destination_dir = Entry(width=75)
        #positions entry in GUI using tkinter grid()padx and pady are teh same as
        #the button to ensure they will line up
        self.destination_dir.grid(row=1, column=1, columnspan=2, padx=(20, 10), pady=(15,10))

        #create btn to transfer files
        self.transfer_btn = Button(self, text="Transfer Files", width=20, command=self.transferFiles)
        #positions transfer files btn
        self.transfer_btn.grid(row=2, column=1, padx=(200, 0), pady=(0,15))
        #creates an Exit button
        self.exit_btn = Button(self, text="Exit", width=20, command=self.exit_program)
        #positions the Exit button
        self.exit_btn.grid(row=2, column=2, padx=(10, 40), pady=(0, 15))
    
    #create function to select source dir
    def sourceDir(self):
        selectSourceDir = tkinter.filedialog.askdirectory()
        #the .delete(0, END) will clear the content that is inserted in the Entry widget, 
        #this allows the path to be inserted into the Entry widget properly
        self.source_dir.delete(0, END)
        #the .insert method will insert the user selection to the source_dir Entry
        self.source_dir.insert(0, selectSourceDir)


    #creates fucntion to select dest dir 
    def destDir(self):
        selectDestDir= tkinter.filedialog.askdirectory()
        #the .delete(0, END) will clear the content that is inserted in the Entry widget
        #this allows the path to be inserted into the Entry widget properly
        self.destination_dir.delete(0, END)
        #the .insert method will insert the user selection to the destionation_dir Entry widget
        self.destination_dir.insert(0, selectDestDir)

    #create function to transfer files from one dir to another
    def transferFiles(self):
        #gets source dir
        source = self.source_dir.get()
        #get destination dir
        destination = self.destination_dir.get()
        #gets a list of files in the source dir
        source_files = os.listdir(source)

        current_time = datetime.now()

    #runs through each file in source dir
    for i in source_files:
        source_file_path = os.path.join(source, i)

        #check if file chnaged in last 24h
        mod_time = datetime.fromtimestamp(os.path.getmtime(source_file_path))
        time_diff = current_time - mod_time 
        if time_diff < timedelta(hours=24):
            #move file to desDir
            shutil.mov(source_file_path, destination)
            print("{i} was transferred.")

            #move each file from the source to the destination
            #shutil.move(source + '/' + i, destination)
            #print(i + ' was successfully transferred.')
        



    #creates function to exit program
    def exit_program(self):
        #root is the main GUI window, the Tkinter destroy method
        #tells python to terminate root.mainloop and all widgets inside the GUI window
        self.master.destroy()





if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

