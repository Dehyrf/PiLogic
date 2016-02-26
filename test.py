from Tkinter import * 
from tkMessageBox import showinfo
from sympy import * 
from tkMessageBox import askokcancel 

def simp(r):
	return to_cnf(r, True)

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
        chars = set('ABCD&|~() ,')
        if any((c in chars) for c in raw):
                legal = True
        else:
                print('Illegal characters!')
                legal = False
                exit()
        logic = simp(raw)
        showinfo(str(raw), str(logic))
        
def main():
	#Take in logic statement from user
	def fetch():
		global raw
		raw = ent.get()
		run()
	
	root = Tk()
	ent = Entry(root)
	ent.insert(0, 'A & (B | C)')               
	ent.pack(side=TOP, fill=X)                     
	ent.focus()
	btn = Button(root, text='Compile', command=fetch) 
	btn.pack(side=LEFT)
	Quitter(root).pack(side=RIGHT)
	root.mainloop()

"""********************"""
# execute 
"""********************"""
if __name__ == "__main__":
	main()
