from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QMainWindow, QLabel, QPushButton
from PySide6.QtCore import QFile, QIODevice
import sys


class CalculateView(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui_file_name = 'calculate.ui'
        self.ui_file = QFile(self.ui_file_name)
        if not self.ui_file.open(QIODevice.ReadOnly):
            print(f"{self.ui_file_name}:{self.ui_file.errorString()}")
            sys.exit(-1)

        self.loader = QUiLoader()
        self.ui = self.loader.load(self.ui_file)
        self.ui_file.close()
        if not self.ui:
            print(self.loader.errorString())
            sys.exit(-1)
        self.ui.show()

        self.Label = self.ui.findChild(QLabel, "label")

        self.Buttons = [self.ui.findChild(QPushButton, "Button_0"),
                        self.ui.findChild(QPushButton, "Button_1"),
                        self.ui.findChild(QPushButton, "Button_2"),
                        self.ui.findChild(QPushButton, "Button_3"),
                        self.ui.findChild(QPushButton, "Button_4"),
                        self.ui.findChild(QPushButton, "Button_5"),
                        self.ui.findChild(QPushButton, "Button_6"),
                        self.ui.findChild(QPushButton, "Button_7"),
                        self.ui.findChild(QPushButton, "Button_8"),
                        self.ui.findChild(QPushButton, "Button_9")]

        self.OpButtons = [self.ui.findChild(QPushButton, "Button_add"),
                          self.ui.findChild(QPushButton, "Button_sub"),
                          self.ui.findChild(QPushButton, "Button_mul"),
                          self.ui.findChild(QPushButton, "Button_div"),
                          self.ui.findChild(QPushButton, "Button_eq"),
                          self.ui.findChild(QPushButton, "Button_ac")]

    def UpdateLabel(self, value):
        self.Label.setText(value)
