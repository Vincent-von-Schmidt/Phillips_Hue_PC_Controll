from mainApp import MainWidget
from PyQt5.QtWidgets import QApplication
import sys


def program() -> None:
    app = QApplication([sys.argv])
    ex = MainWidget()

    with open("style.css", "r") as file:
        app.setStyleSheet(file.read())

    sys.exit(app.exec_())


def main() -> None:
    import cProfile
    import pstats

    with cProfile.Profile() as pr:
        program()

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats()
    stats.dump_stats("debug.prof")


if __name__ == '__main__':
    main()
