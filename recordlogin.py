#!/usr/bin/python3
import curses
import sys
import os

def curses_main(screen):

	name = ""
	while(True):
		new_char = draw_screen(screen,name)
		if new_char=="q":
			break;
		name = name+new_char



def draw_screen(screen, name):

	screen.clear()
	screen.refresh()

	curses.start_color()
	curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLUE)
	curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLUE)

	screen.bkgd(' ',curses.color_pair(1))
	screen.addstr(0,0,"Hello, curses world", curses.color_pair(2) | curses.A_BOLD)

	screen.refresh()

	x = screen.getkey()

	return(x)


def main():
	curses.wrapper(curses_main)

if __name__ == "__main__":
	main()
