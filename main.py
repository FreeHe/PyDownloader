"""
    author : FreeHe
"""

# 启动文件

import os.path
import sys
from PyQt5.QtWidgets import QApplication, QPushButton
from QWindow.QMainWin import QMainWin
from threadGet.threadGet import ThreadGet

app = QApplication(sys.argv)
win = QMainWin(ThreadGet(os.path.dirname(os.path.abspath(__file__))))
win.show()
sys.exit(app.exec_())


# TODO // finished_panel