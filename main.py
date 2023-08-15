import sys
from view import CalculateView
from controller import Control
from model import OperateModel
from PySide6.QtWidgets import QApplication


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mod = OperateModel()
    view = CalculateView()
    ctrl = Control(mod, view)
    sys.exit(app.exec())
