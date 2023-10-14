from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import randint

app = QApplication([])

win = QWidget()
win.setWindowTitle("Генератор")
win.resize(400,200)
win.move(100,100)

def rand():
    txt2.setText(str(randint(0,9)))
    txt3.setText(str(randint(0,9)))

    if txt2.text() == txt3.text():
        txt.setText("Ви виграли! Зіграйте знову")
    else:
        txt.setText("Ви програли! Зіграйте знову")
 
txt = QLabel()
txt.setText("Натисни, щоб взяти участь")

txt2 = QLabel()
txt2.setText("?")

txt3 = QLabel()
txt3.setText("?")

but = QPushButton()
but.setText("Випробувати удачу")
linev = QVBoxLayout()
linev.addWidget(txt, alignment=Qt.AlignCenter)

linev.addWidget(txt2, alignment=Qt.AlignCenter)

linev.addWidget(txt3, alignment=Qt.AlignCenter)
linev.addWidget(but, alignment=Qt.AlignCenter)

but.clicked.connect(rand)

win.setLayout(linev)
win.show()
app.exec_()