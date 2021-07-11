from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MainWindow (QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("Checkboxes ")
        self.resize(1280, 720)
        layout = QVBoxLayout()

        check1 = QCheckBox("python ")
        check1.toggled.connect(lambda: self.something_checked(check1))

        check2 = QCheckBox("java")
        check2.toggled.connect(lambda: self.something_checked(check2))
       
        check3 = QCheckBox("C++")
        check3.toggled.connect(lambda: self.something_checked(check3))
        
        check4 = QCheckBox("C#")
        check4.toggled.connect(lambda: self.something_checked(check4))
        
        check5 = QCheckBox("PHP")
        check5.toggled.connect(lambda: self.something_checked(check5))

        self.label = QLabel("You have not selected anything")

        self.checked_stuff = []

        layout.addWidget(check1)
        layout.addWidget(check2)
        layout.addWidget(check3)
        layout.addWidget(check4)
        layout.addWidget(check5)
        layout.addWidget(self.label)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def something_checked(self, check):

        if check.isChecked() == False:
            self.checked_stuff = list(filter(lambda stuff: (
                stuff != check.text()), self.checked_stuff))
        else:
            # when its true
            self.checked_stuff.append(check.text())
        task_string = ""
        for task in self.checked_stuff:
            task_string += (task+"\n")

        self.label.setText(task_string)


app = QApplication([])
window = MainWindow()
window.show()
app.exec()
