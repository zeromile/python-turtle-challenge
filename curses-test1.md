# Curses Test 1 #

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

