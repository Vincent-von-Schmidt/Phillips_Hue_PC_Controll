import curses
from curses import wrapper

class Tab:
    def __init__(self, name: str) -> None:
        print(
            f"  ##################################################\n"
            f" # {name} # \n"
            f"##################################################  \n"
        )


if __name__ == "__main__":
    test_tab = Tab("Test")
