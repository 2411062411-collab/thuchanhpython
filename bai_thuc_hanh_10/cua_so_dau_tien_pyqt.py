import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout


class CuaSoDauTien(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cửa sổ PyQt đầu tiên")
        self.resize(400, 250)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Xin chào PyQt!"))

        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    cua_so = CuaSoDauTien()
    cua_so.show()
    sys.exit(app.exec_())
