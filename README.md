# Members:

- Frances Calceta
- Miguel Posadas
- Rhea Limkinglam


# Demo Video:
https://drive.google.com/file/d/0B08-BvAcWqPHRHdRTGU1b0VVZkk/view?usp=sharing

# Needs pyglet:

''' pip install pyglet '''

# To run: 
- put three files in same directory
- main.py

# Where are the threads?

- ** Producer-Consumer (Word Generator and Word Display) **
- ''' def spawnWord(dt) and pyglet.clock.schedule_interval(spawnWord, 60.0/wpm) '''
- spawnWord is called per time interval
- spawnWord creates a new Word object
- def on_draw()
- draws all objects on screen (pyglet's event handler deals with this)
- Keyboard Listener
- def on_text(text)
- listens for keyboard input and passes keypress to Words in wordList
- Misc Tasks
- def doChecks(dt) and pyglet.clock.schedule_interval(doChecks, 1/60.0)
- called per time interval
- handles the collisions and the current state of the game (if no more lives, game end, displaying the ending messages when game has ended)
