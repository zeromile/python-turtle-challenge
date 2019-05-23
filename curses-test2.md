# Curses Test 2 - this time with a wrapper #

Do a "save-as" of the curses-test1.py (or create a new file with the same name) to curses-test2.py

We are going to simplify our code by using Curses' built-in "wrapper". A wrapper is code that handles a lot of the monotonous interstitial stuff. Instead of having to put everything back to normal with the terminal a wrapper can do that automatically once our code is done.

Modify your curses-test2.py code to look like the following code:

~~~~
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
~~~~

See? Way simpler!
