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
