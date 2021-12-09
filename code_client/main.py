from PyQt5.QtWidgets import QApplication
from sys import argv, exit
from LotteryTicketSystem import LotteryTicketSystem
from pre import get_qss


def main():
    qss = get_qss()
    app = QApplication(argv)
    app.setStyleSheet(qss)
    gui = LotteryTicketSystem()
    gui.show()
    exit(app.exec_())


if __name__ == '__main__':
    main()

