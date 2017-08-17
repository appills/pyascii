from tkinter import *
from tkinter import filedialog
from pyascii import main
class App:
	def __init__(self, master):
		#initalize myFile instance variable
		self.myFile = None
		self.saveFile = None
		#set window height
		master.minsize(height = 440, width = 680)
		#create frame
		frame = Frame(master)
		frame.pack()
		#first label
		self.labelTop = Label(frame, text="Choose an image file!", font=("Arial", 12))
		self.labelTop.pack()
		#first button
		self.buttonTop = Button(frame, text="Choose file", fg="blue", width = 10, command = self.chooseImageFile)
		self.buttonTop.pack()
		#second label
		self.labelMid = Label(frame, 
			text="The ascii text file will be saved in the same directory as the image.\n"
			"If your image name was foo.jpg, the text file will be foo.txt", 
			font=("Arial", 12))
		self.labelMid.pack()
		#second button
		self.buttonMid = Button(frame, text="Pyascii!", fg="green", width = 10, command=self.pyascii)
		self.buttonMid.pack()
		
	def chooseImageFile(self):
		self.myFile = filedialog.askopenfilename(parent = root,  title='Choose your picture!')	
		while self.verifyFileExtension() is False:
			self.myFile = filedialog.askopenfilename(parent = root,  title='Invalid file!')
				
			
	def pyascii(self):
		main(self.myFile)
		
	def verifyFileExtension(self):
		if self.myFile is None:
			return False
		else:
			validExtensions = ["jpeg", "jpg", "bmp", "png"]
			result = False
			for extension in validExtensions:
				if self.myFile.endswith(extension):
					result = True
			return result


root=Tk()
root.wm_title("Pyascii")
app = App(root)

root.mainloop()