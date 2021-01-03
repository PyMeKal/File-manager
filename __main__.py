import sys
from __class__ import *

if __name__ == '__main__':
    app = QApplication([])
    ex = Main()
    ex.show()
    sys.exit(app.exec_())