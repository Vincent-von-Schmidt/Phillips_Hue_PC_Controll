import curses

def main(stdsrc) -> None:
	MID = (curses.COLS - 1) // 2
	curses.use_default_colors()

	neowin = curses.newpad()

	stdsrc.clear()

	stdsrc.addstr(0, MID - 6, "Hello World!")

	stdsrc.refresh()
	stdsrc.getch()

if __name__ == "__main__":
	curses.wrapper(main)
