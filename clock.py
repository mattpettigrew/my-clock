from Tkinter import *
import time, datetime

from sys import stdout
# if you are working under Python 3, comment the previous line and comment out the following line
#from tkinter import *
#while True:


root = Tk()
thetime = time.time()
taco = datetime.datetime.fromtimestamp(thetime).strftime(" %H:%M:%S   %m-%d-%Y")
w = Label(root, font=('times', 40, 'bold'), bg='green', text = taco)
w.pack()
def my_mainloop():
	
	thetime = time.time()
	taco = datetime.datetime.fromtimestamp(thetime).strftime(" %H:%M:%S   %m-%d-%Y")
	#
	#w["bg"] = 'blue'
	w['text'] = taco
	
	

	
	root.after(1000, my_mainloop)

my_mainloop()

root.mainloop()