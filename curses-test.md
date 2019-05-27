# Installing and using the curses module #
## Curses Test 1 ##

At the Windows command prompt type the following 2 lines, follow each with the Enter key:
~~~~
python -m pip install --user --upgrade pip
pip3 install --user windows-curses
~~~~

Now launch IDLE (Windows) and create a new Python file named `curses-test1.py`, save it in your user folder (you'll have to navigate there...C:Drive->Users->YourUserName->)

In that file enter the following code:

~~~~
import time
import curses

# get the curses screen window
stdscr = curses.initscr()

# turn off input echoing
curses.noecho()

# respond to keys immediately (don't wait for enter)
curses.cbreak()

# map arrow keys to special values
stdscr.keypad(True)

# print doesn't work with curses, use addstr instead
stdscr.addstr(5, 5, "Hello")

# screen must be refreshed when changes are made
stdscr.refresh()

# wait 3 seconds
time.sleep(3)

# return normal control of terminal functions
curses.echo()
curses.nocbreak()
stdscr.keypad(False)

# bye bye
curses.endwin()
~~~~

To run you will have to go back to the Windows command prompt and type:
`python curses-test1.py`

You should get an empty terminal window that says "Hellow World"

## Curses Test 2 - this time with a wrapper ##

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
