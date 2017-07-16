import Tkinter as tk
from time import sleep
from Tkinter import *
class Gui():
	def __init__(self, root):
		self.root=root
		self.entry = tk.Entry(root)
		stvar=tk.StringVar()
		stvar.set("one")
		
		self.canvasWidth = 300
		self.canvasHeight = 300
		self.canvas=tk.Canvas(root, width=self.canvasWidth, height=self.canvasHeight, background='white')
		self.canvas.grid(row=0,column=3)
		
		self.frame=Frame(self.root).grid(column=0,row=4,sticky="n")
		self.button=Button(self.frame,text="simulate",command=self.runSimulation).grid(column=0,row=0,sticky="n")
		self.button=Button(self.frame,text="up",command=lambda: self.runSimulation(0,-10)).grid(column=1,row=1,sticky="n")
		self.button=Button(self.frame,text="down",command=lambda: self.runSimulation(0,10)).grid(column=1,row=2,sticky="n")
		self.button=Button(self.frame,text="left",command=lambda: self.runSimulation(-10,0)).grid(column=0,row=3,sticky="n")
		self.button=Button(self.frame,text="right",command=lambda: self.runSimulation(10,0)).grid(column=2,row=3,sticky="n")
		
	def runSimulation(self,x,y):
		self.canvas.move(self.figure1,x,y)
def runSimulation():
	print "foo"

class mainMap():
	def __init__(self,gui):
		self.columns = 30
		self.rows = 30
		self.mapMatrix = {}
		self.makeMatrixDict()
		# print self.mapMatrix
	
	def makeMatrixDict(self):
		for x in range(self.columns):
			for y in range(self.rows):
				self.mapMatrix[y,x]=[None,None]
				
def movment(gui):
	pass
	
if __name__== '__main__':
	root=tk.Tk()
	gui=Gui(root)
	Map = mainMap(gui)
	for line in range(Map.rows):
		x = line*(gui.canvasWidth/Map.rows)
		gui.canvas.create_line(x,0,x,gui.canvasHeight,fill="black")
	for line in range(Map.columns):
		y = line*(gui.canvasWidth/Map.columns)
		gui.canvas.create_line(0,y,gui.canvasWidth,y,fill="black")
	
	gui.figure1=gui.canvas.create_oval(0, 0, 10, 10, fill="blue")
	# for x in range(10):
		# sleep(1)
		# gui.canvas.move(gui.figure1,10,10)
		# root.update()
	root.mainloop()