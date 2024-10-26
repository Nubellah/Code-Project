from PyQt5.QtWidgets import QApplication, QWidget, QLabel
import sys
class NaijaApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set the title of the window
        self.setWindowTitle('NAIJA 4 LIFE Application')

        # Set the dimensions of the window
        self.setGeometry(100, 100, 400, 200)

        # Create a QLabel to display "NAIJA 4 LIFE"
        label = QLabel('NAIJA 4 LIFE', self)
        label.move(150, 80)  # Position the label in the window

        # Set the label font size and make it bold
        label.setStyleSheet("font-size: 24px; font-weight: bold; color: green;")

#In this step, create an instance of `QApplication` to manage the application, create an instance of your custom `NaijaApp` window, and then execute the main application loop.

#```python
if __name__ == '__main__':
    app = QApplication(sys.argv)
    naija_window = NaijaApp()
    naija_window.show()  # Show the main window
    sys.exit(app.exec_())
