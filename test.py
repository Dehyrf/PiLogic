from Tkinter import * 
from tkMessageBox import askokcancel 

class Quitter(Frame):  
	#Handles window closing                        
    	def __init__(self, parent=None):           
        	Frame.__init__(self, parent)
        	self.pack()
        	widget = Button(self, text='Quit', command=self.quit)
        	widget.pack(expand=YES, fill=BOTH, side=LEFT)
    	def quit(self):
        	ans = askokcancel('Verify exit', "Really quit?")
        	if ans: Frame.quit(self)
        
def run():
	print ('hello',)

def main():
	#Take in logic statement from user
	root = Tk()
	ent = Entry(root)
	ent.insert(0, 'A & (B | C)')               
	ent.pack(side=TOP, fill=X)                     
	ent.focus()                                    
	ent.bind('<Return>', (lambda event: run()))  
	btn = Button(root, text='Compile', command=run) 
	btn.pack(side=LEFT)
	Quitter(root).pack(side=RIGHT)
	root.mainloop()
	
"""********************"""
# execute 
"""********************"""
if __name__ == "__main__":
	main()
