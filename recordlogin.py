#!/usr/bin/python3
import curses
import os
from datetime import datetime

def curses_main(screen):

	name = ""
	while(True):
		new_char = draw_screen(screen,name)
		if new_char=="\n":
			if len(name)>0:
				break;

		elif new_char=="KEY_BACKSPACE" and len(name)>0:
			name=name[:-1]

		elif new_char.startswith("KEY"):
			continue

		else:
			name = name+new_char

	print_final_screen(screen)
	save_name(name)
	logout(screen)


def save_name(name):
	# We can't use ~ in a n open statement directly.  We have
	# to manually expand it.
	with open(os.path.expanduser("~")+"/.recorded_logins.txt","a") as file:
		file.write(name)
		file.write("\t")
		file.write(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
		file.write("\n")

def logout(screen):
	screen.clear()
	screen.refresh()

	curses.start_color()
	curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_BLACK)

	screen.bkgd(' ',curses.color_pair(1))

	screen.refresh()

	# Logging out is tricky.  We can't actually call logout or exit
	# as those are shell builtins and not commands.  The hack we use
	# is simply to kill the parent of this process which will always be
	# the shell which launched it, and this will then log us out.

	os.kill(os.getppid(),9)


def print_final_screen (screen):

	screen.clear()
	screen.refresh()

	height, width = screen.getmaxyx()

	curses.start_color()
	curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLUE)
	curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLUE)
	curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_RED)

	screen.bkgd(' ',curses.color_pair(1))

	main_title = "BABRAHAM BIOINFORMATICS TEST SERVER"
	screen.addstr(1,get_centre_offset(main_title, width),main_title, curses.color_pair(2) | curses.A_BOLD)

	congrats_text = "Thankyou, you're all done"
	screen.addstr(int(height/2)-1,get_centre_offset(congrats_text, width),congrats_text, curses.color_pair(2))

	congrats_text = " <Press any key to log out> "
	screen.addstr(int(height/2)+1,get_centre_offset(congrats_text, width),congrats_text, curses.color_pair(3))

	screen.move(0,0)

	screen.refresh()

	x = screen.getkey()



def draw_screen(screen, name):

	screen.clear()
	screen.refresh()

	height, width = screen.getmaxyx()

	curses.start_color()
	curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLUE)
	curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLUE)
	curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_RED)

	screen.bkgd(' ',curses.color_pair(1))

	main_title = "BABRAHAM BIOINFORMATICS TEST SERVER"
	screen.addstr(1,get_centre_offset(main_title, width),main_title, curses.color_pair(2) | curses.A_BOLD)

	congrats_text = "Congratulations, you logged in successfully"
	screen.addstr(4,get_centre_offset(congrats_text, width),congrats_text, curses.color_pair(2))

	name_please_text = "Please type your name so we know who you are"
	screen.addstr(5,get_centre_offset(name_please_text, width),name_please_text, curses.color_pair(2))

	user_name = name.ljust(50,".")
	screen.addstr(10,get_centre_offset(user_name, width),user_name, curses.color_pair(3))

	# Put the cursor where they're going to have to type
	cursor_pos = get_centre_offset(user_name, width)+len(name)
	screen.move(10,cursor_pos)


	screen.refresh()

	x = screen.getkey()

	return x


def get_centre_offset(text,width):
	return int(width/2 - len(text)/2)


def main():
	curses.wrapper(curses_main)

if __name__ == "__main__":
	main()
