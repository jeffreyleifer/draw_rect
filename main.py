import sys
from PySide2.QtWidgets import QApplication
from rec_creator import RectangleCreator

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    w = RectangleCreator()
    w.resize(640, 480)
    w.show()
    sys.exit(app.exec_())

