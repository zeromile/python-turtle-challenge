import time
import curses

# define a function called main
def main(stdscr):
	curses.curs_set(0)
	stdscr.addstr(5,5, "Hello")
	stdscr.refresh()
	time.sleep(3)

# Call the function named main from the “wrapper”…
# A wrapper is a class built into curses that 
# 	takes care of setup at the beginning and 
#	cleanup once code is finished

curses.wrapper(main)
