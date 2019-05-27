# this file was originally called curse-key2.py

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
