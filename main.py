# Common Words Corpora Source: wordfrequency.info

import pyglet
import random
from Word import Word

# difficulty = input("difficulty:")
# wpm = input("wpm:")
# ngrams = input("ngrams:")
difficulty = 5
wpm = 50
ngrams = 2


window = pyglet.window.Window(800,600, caption = "Typing of the Dead Inside")
fps_display = pyglet.clock.ClockDisplay()
pyglet.gl.glClearColor(0.2, 0.3, 0.5, 0)


killPoint = window.height//4
words = []
spawnableRange = []
numRange = 20
lives = 3
score = 0

# wpm = 100
# difficulty = 3
# ngrams = 4
gameEnd = False
poppingDone = False



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

label4 = pyglet.text.Label(  ("lives: "+" "+ " left")   ,font_name="Courier New",font_size=18,x=window.width//2+300, y=killPoint,anchor_x='center', anchor_y='top', bold=False)
label5 = pyglet.text.Label(  ("score: "+" "+ " points")   ,font_name="Courier New",font_size=18,x=window.width//2+280, y=killPoint-30,anchor_x='center', anchor_y='top', bold=False)

livesLabel = pyglet.text.Label(  ("      "+str(lives)+ "     ")   ,font_name="Courier New",font_size=18,x=window.width//2+300, y=killPoint,anchor_x='center', anchor_y='top', bold=True)
scoreLabel = pyglet.text.Label(  ("       "+str(score)+ "       ")   ,font_name="Courier New",font_size=18,x=window.width//2+280, y=killPoint-30,anchor_x='center', anchor_y='top', bold=True)


gameEndLabel = pyglet.text.Label(  ("Game end, press any key to exit")   ,font_name="Courier New",font_size=28,x=window.width//2, y=window.height//2,anchor_x='center', anchor_y='center', bold=True)


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
	label4.draw()
	label5.draw()
	livesLabel.draw()
	scoreLabel.draw()
	global gameEnd
	global poppingDone
	if gameEnd:
		pyglet.gl.glClearColor(0.5, 0.3, 0.3, 0)
		if poppingDone:
			gameEndLabel.draw()
			global score
			pyglet.text.Label(  ("Final Score: "+str(score))   ,font_name="Courier New",font_size=34,x=window.width//2, y=window.height//2+70,anchor_x='center', anchor_y='center', bold=True).draw()
	



@window.event
def on_text(text):
	global gameEnd
	if not gameEnd:
		print text
		for w in words:
			w.getLetter(text)
	else:
		exit()
		pass

# Update here
def doChecks(dt):	
	global gameEnd
	if not gameEnd:
		for x in range(len(words)-1, -1, -1):
			w = words[x]
			if w.end:
				words.pop(x)
				global score
				global scoreLabel
				score += 1
				for word in words:
					word.currIndex = 0 #don't carry over letters
				scoreLabel = pyglet.text.Label(  ("       "+str(score)+ "       ")   ,font_name="Courier New",font_size=18,x=window.width//2+280, y=killPoint-30,anchor_x='center', anchor_y='top', bold=True)	
				continue
			if w.yPos < killPoint:
				#kill it
				# w.yPos = window.height
				global lives
				global livesLabel
				lives -= 1
				livesLabel = pyglet.text.Label(  ("      "+str(lives)+ "     ")   ,font_name="Courier New",font_size=18,x=window.width//2+300, y=killPoint,anchor_x='center', anchor_y='top', bold=True)
				if lives<=0:
					gameEnd = True
				words.pop(x)
				global gameEnd
				continue

			w.checked = True
			w.updatePos(dt)
	else:
		# gameEndLabel.draw()
		pass


def spawnWord(dt):
	global gameEnd
	# print gameEnd
	if not gameEnd:
		print "spawning word"
		velocity = difficulty * -25
		words.append(Word(  getWord() , random.choice(spawnableRange), window.height,velocity))
		print "words list len", len(words)
	else:
		for x in range(len(words)-1, -1, -1):
			words.pop(x)
		global poppingDone
		poppingDone = True

pyglet.clock.schedule_interval(spawnWord, 60.0/wpm)
pyglet.clock.schedule_interval(doChecks, 1/60.0)
if __name__ == '__main__':
	pyglet.app.run()