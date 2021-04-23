import tkinter
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

def newFile():
	global file
	root.title("Untitled- BoardPad")
	file = None
	Textarea.delete(1.0, END)

def openFile():
	global file
	file = askopenfilename(defaultextension = ".txt", filetype =[("All Files", "*.*"), 
						   ("Text Documents","*.txt")])
	if file == "":
		file = None
	else:
		root.title(os.path.basename(file) + " -BaordPad ")
		Textarea.delete(1.0, END)
		f = open(file, "r")
		Textarea.insert(1.0, f.read())
		f.close()


def saveFile():
	global file
	if file ==None:
		file = asksaveasfilename(initialfile ='Untitled.txt', defaultextension = ".txt", filetype =[("All Files", "*.*"), 
						   ("Text Documents","*.txt")])
		if file =="":
			file = None

		else:
			# Save as a new file 
			f = open(file, "w")
			f.write(Textarea.get(1.0, END))
			f.close()

			root.title(os.path.basename(file) + " -Notepad")
			print("File Saved")

	else:
		# Save the new file 
		f = open(file, "w")
		f.write(Textarea.get(1.0, END))
		f.close()

def quitApp():
	root.destroy()

def Cut():
    Textarea.event_generate(("<<Cut>>"))


def Copy():
	Textarea.event_generate(("<<Copy>>"))

def Paste():
	Textarea.event_generate(("<<Paste>>"))

def about():
	showinfo("BoardPad","BoardPad by Adderswift Corporation Copyright 2021-2022")

if __name__ == '__main__':
	# Basic tkinter setup..
	root = Tk()
	root.title("Untitled- BoardPad")
	root.wm_iconbitmap("text.ico")
	root.geometry("644x788")

	# Add Textarea

	Textarea = Text(root, font="Rajadhani 18")
	file = None
	Textarea.pack(expand = True, fill = BOTH)

	# Menubar 

	MenuBar = Menu(root)
	FileMenu = Menu(MenuBar, tearoff = 0) 
	# To open new file

	FileMenu.add_command(label="New", command=newFile)

	# To open already existing file
	FileMenu.add_command(label="Open", command=openFile)

	 #To save

	FileMenu.add_command(label="Save", command=saveFile)
	FileMenu.add_command(label="Exit", command=quitApp)
	MenuBar.add_cascade(label ="File", menu= FileMenu)
	 #  FIle Menu starts

	 # Edit Menu starts
	EditMenu = Menu(MenuBar, tearoff = 0)

	EditMenu.add_command(label="Cut", command=Cut)
	EditMenu.add_command(label="Copy", command=Copy)
	EditMenu.add_command(label="Paste", command=Paste)

	MenuBar.add_cascade(label="Edit", menu = EditMenu)
	 # Edit Menu ends

	 # Help Menu startswith
	HelpMenu = Menu(MenuBar, tearoff = 0)
	HelpMenu.add_command(label="About BoardPad", command=about)
	MenuBar.add_cascade(label="Help", menu = HelpMenu)
	 # Help menu ends
	root.config(menu = MenuBar)

	# Adding Scrollbar
	Scroll = Scrollbar(Textarea)
	Scroll.pack(side = RIGHT, fill = Y)
	Scroll.config(command = Textarea.yview)
	Textarea.config(yscrollcommand = Scroll.set)


	
	root.mainloop()
	