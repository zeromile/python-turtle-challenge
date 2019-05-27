# Using the curses module to read a single key #
## Curses Key 1 ##

Launch IDLE (Windows) and create a new Python file named `curses-key1.py`, save it in your user folder (you'll have to navigate there...C:Drive->Users->YourUserName->)

In that file enter the following code:

~~~~
# this file was originally called curse-key1.py

import curses
 
screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

# loop that listens for keypresses and then reacts to them
while True:
	char = screen.getch()
	if char == ord('q'):
		break
	elif char == curses.KEY_RIGHT:
		screen.addstr(0, 0, 'right')
	elif char == curses.KEY_LEFT:
		screen.addstr(0, 0, 'left ')
	elif char == curses.KEY_UP:
		screen.addstr(0, 0, 'up   ')
	elif char == curses.KEY_DOWN:
		screen.addstr(0, 0, 'down   ')

# shut down cleanly
curses.nocbreak() 
screen.keypad(0) 
curses.echo()
curses.endwin()
~~~~

To run you will have to go back to the Windows command prompt and type:
`python curses-key1.py`

You will get a blank screen and  nothing will happen until you press an arrow key; window should respond with the name of that arrow key.

## Curses Key 2 - This time with turtle ##

Do a "save-as" of the curses-key1.py (or create a new file with the same name) to curses-key2.py

We are going to modify our code to use the arrow keys to control the turtle

Modify your curses-key2.py code to look like the following code:

~~~~
code
~~~~
