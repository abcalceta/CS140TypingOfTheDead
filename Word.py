import pyglet
# import time
# from threading import Thread

class Word:
	#class variables are shared with everyone
	fontSize = 20
	font = "Courier New"
	def __init__(self, name, xpos, ypos=0, velocity = -60):
		self.name = name#"name"
		self.xPos = xpos
		self.yPos = ypos
		self.velocity = velocity

		self.checked = False
		self.currIndex = 0
		self.end = False
		self.underlineLen = self.fontSize*len(name)



	def draw(self):
		pyglet.graphics.draw(2, pyglet.gl.GL_LINES,('v2i', (int(self.xPos), int(self.yPos), int(self.xPos+self.underlineLen), int(self.yPos))))

		# self.label = pyglet.text.Label(self.name,font_name='Times New Roman',font_size=36,x=self.xPos, y=self.yPos,anchor_x='center', anchor_y='bottom')
		# self.label.draw()

		for x in range(len(self.name)):
			offset = x*self.fontSize
			if x<self.currIndex:
				pyglet.text.Label(self.name[x],font_name=self.font,font_size=self.fontSize+5,x=self.xPos+offset, y=self.yPos,anchor_x='center', anchor_y='bottom', bold=True).draw()
			else:
				pyglet.text.Label(self.name[x],font_name=self.font,font_size=self.fontSize,x=self.xPos+offset, y=self.yPos,anchor_x='center', anchor_y='bottom', bold=False).draw()

	def updatePos(self, dt):
		self.yPos += self.velocity*dt

	def getLetter(self, letter):
		if not self.currIndex>=len(self.name):
			if self.name[self.currIndex] == letter:
				self.currIndex += 1
				if self.currIndex>=len(self.name):
					print "GOT IT"
					self.end = True
			else:
				self.currIndex = 0
