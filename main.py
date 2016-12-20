# Common Words Corpora Source: wordfrequency.info

import pyglet
import random
from Word import Word

difficulty = input("difficulty:")
wpm = input("wpm:")
ngrams = input("ngrams:")



window = pyglet.window.Window(800,600, caption = "Typing of the Dead Inside")
fps_display = pyglet.clock.ClockDisplay()
pyglet.gl.glClearColor(0.2, 0.3, 0.5, 0)


killPoint = window.height//4
words = []
spawnableRange = []
numRange = 20

# wpm = 100
# difficulty = 3
# ngrams = 4




print "window width", window.width
for x in range(numRange):
	while True:
		temp = random.randrange(100, window.width-200, 20)
		if temp not in spawnableRange:
			spawnableRange.append(temp)
			break
# print spawnableRange

wordList = []
with open('top5000CommonWords.txt') as fp:
	for line in fp:
		if len(line)>ngrams:
			wordList.append(line[:-1])
def getWord():
	return random.choice(wordList)


label1 = pyglet.text.Label( ("difficulty: "+str(difficulty))     ,font_name="Courier New",font_size=26,x=window.width//2, y=killPoint-60,anchor_x='center', anchor_y='bottom', bold=True)

label2 = pyglet.text.Label(  ("wpm: "+str(wpm))   ,font_name="Courier New",font_size=24,x=window.width//2, y=killPoint-100,anchor_x='center', anchor_y='bottom', bold=True)

label3 = pyglet.text.Label(  ("only words longer than "+str(ngrams)+ " characters")   ,font_name="Courier New",font_size=20,x=window.width//2, y=killPoint-130,anchor_x='center', anchor_y='bottom', bold=True)



fps_display = pyglet.clock.ClockDisplay()
# Display here
@window.event
def on_draw():
	window.clear()
	fps_display.draw()
	for w in words:
		w.draw()
	pyglet.graphics.draw(2, pyglet.gl.GL_LINES,
	    ('v2i', (0, killPoint, window.width, killPoint))
	)
	label1.draw()
	label2.draw()
	label3.draw()



@window.event
def on_text(text):
	print text
	for w in words:
		w.getLetter(text)

# Update here
def doChecks(dt):	
	for x in range(len(words)-1, -1, -1):
		w = words[x]
		if w.end:
			words.pop(x)
			for word in words:
				word.currIndex = 0 #don't carry over letters
			continue
		if w.yPos < killPoint:
			#kill it
			# w.yPos = window.height
			words.pop(x)
			continue

		w.checked = True
		w.updatePos(dt)

def spawnWord(dt):
	print "spawning word"
	velocity = difficulty * -25
	words.append(Word(  getWord() , random.choice(spawnableRange), window.height,velocity))
	print "words list len", len(words)


pyglet.clock.schedule_interval(spawnWord, 60.0/wpm)
pyglet.clock.schedule_interval(doChecks, 1/60.0)
if __name__ == '__main__':
	pyglet.app.run()