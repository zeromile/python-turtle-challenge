# Using the curses module to read keys without hitting enter #
## Curses Key 1 ##

Launch IDLE (Windows) and create a new Python file named `curses-key1.py`, save it in your user folder (you'll have to navigate there...C:Drive->Users->YourUserName->)

In that file enter the following code:

~~~~
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

## Curses Key 2 - This time with Turtle ##

Do a "save-as" of the curses-key1.py (or create a new file with the same name) to curses-key2.py

We are going to modify our code to use the arrow keys to control the turtle

Modify your curses-key2.py code to look like the following code; we are simply adding the turtle import and turtle control commands in the conditionals

~~~~
import curses
import turtle

# get the curses screen window
screen = curses.initscr()
 
# turn off input echoing
curses.noecho()
 
# respond to keys immediately (don't wait for enter)
curses.cbreak()
 
# map arrow keys to special values
screen.keypad(True)

while True:
  char = screen.getch()
	if char == ord('q'):
		break
	elif char == curses.KEY_RIGHT:
		screen.addstr(0, 0, 'right')
		turtle.right(15)
	elif char == curses.KEY_LEFT:
		screen.addstr(0, 0, 'left ')
	 	turtle.left(15)
	elif char == curses.KEY_UP:
		screen.addstr(0, 0, 'up   ')
		turtle.forward(20)       
	elif char == curses.KEY_DOWN:
		screen.addstr(0, 0, 'down ')

# shut down cleanly
curses.nocbreak() 
screen.keypad(0) 
curses.echo()
curses.endwin()
~~~~


## Curses Key 3 Challenge - This time with wrapper() ##

Do a "save-as" of the curses-key2.py (or create a new file with the same name) to curses-key3.py

We are going to modify our curses-key2.py code to use the python built-in wrapper, in a similar way that we did in the curses-test2.py file.
