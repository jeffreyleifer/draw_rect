import sys
import signal
from PySide2.QtWidgets import QApplication
from rect_creator import RectangleCreator

"""
Main Driver
* Creates Rectangle Creator Widget
"""
if __name__ == '__main__':
    import sys
    print('Launching draw_rec...')
    app = QApplication(sys.argv)
    w = RectangleCreator()
    w.resize(640, 480)
    w.show()
    print('Ready')
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    sys.exit(app.exec_())
y