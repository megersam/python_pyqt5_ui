from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MainWindow (QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("Checkboxes yayy")
        self.resize(1280, 720)

        layout = QVBoxLayout()

        list_ = QListWidget()
        list_.addItems(['Easy', 'hard', 'expert'])
        list_.currentItemChanged.connect(self.show_selected)
        layout.addWidget(list_)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
# we will change this

    def show_selected(self, item):
        print(item.text())


app = QApplication([])
window = MainWindow()
window.show()
app.exec()
