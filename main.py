import curses

def main(stdsrc) -> None:
	MID_X = (curses.COLS - 1) // 2
    MID_Y = (curses.LINE - 1) // 2
	curses.use_default_colors()

	# neowin = curses.newpad()

	stdsrc.clear()

	stdsrc.addstr(MID_Y, MID_X - 6, "Hello World!")

	stdsrc.refresh()
	stdsrc.getch()

if __name__ == "__main__":
	curses.wrapper(main)
