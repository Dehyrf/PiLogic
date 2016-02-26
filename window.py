from Tkinter import Tk, Frame, BOTH


class Window(Frame):
	def __init__(self, parent):
        	Frame.__init__(self, parent, background="white")   
        	self.parent = parent
        	self.parent.title("Centered window")
        	self.pack(fill=BOTH, expand=1)
        	self.centerWindow()
    	def centerWindow(self):
        	w = 512
        	h = 256
        	x = (self.parent.winfo_screenwidth() - w)/2
        	y = (self.parent.winfo_screenheight() - h)/2
        	self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))
        

def main():
	root = Tk()
	root.geometry("250x150+300+300")
	app = Window(root)
	root.mainloop()  

if __name__ == '__main__':
    main()
