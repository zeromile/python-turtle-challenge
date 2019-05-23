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
