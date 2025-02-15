import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget

class MainApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ERP 시스템")
        self.setGeometry(100, 100, 600, 400)
        self.label = QLabel("안녕하세요! ERP 시스템입니다.", self)
        self.label.move(50, 50)

app = QApplication(sys.argv)
window = MainApp()
window.show()
sys.exit(app.exec())
