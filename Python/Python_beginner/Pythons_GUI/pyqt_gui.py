from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.label = QLabel('Enter your name:')
        self.entry = QLineEdit()
        self.button = QPushButton('Click me!')

        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.entry)
        layout.addWidget(self.button)

        self.button.clicked.connect(self.on_button_click)

    ############## important set for show text on same page ##############
    def on_button_click(self):
        name = self.entry.text()
        self.label.setText(f'Hello, {name}!')



if __name__ == '__main__':
    app = QApplication([]) #-1
    window = MyWindow() #-2
    window.show() #-3
    app.exec_() #-4
	
	
"""
##############################################################################################################
########################## to show the window just thats enough ##############################################
##############################################################################################################

from PyQt5.QtWidgets import QApplication, QWidget
class MyWindow(QWidget):
	pass

	
if __name__=="__main__" :
	app = QApplication([])
	window = MyWindow()
	window.show()
	app.exec_()
"""