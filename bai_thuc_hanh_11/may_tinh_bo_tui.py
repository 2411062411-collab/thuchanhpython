import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QGridLayout,
    QLabel, QLineEdit, QComboBox, QPushButton, QMessageBox
)
from PyQt5.QtCore import Qt


class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hoạt động 6 - Máy tính bỏ túi")
        self.resize(420, 300)

        layout = QVBoxLayout(self)

        title = QLabel("MÁY TÍNH BỎ TÚI")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 20px; font-weight: bold;")
        layout.addWidget(title)

        grid = QGridLayout()

        self.a = QLineEdit()
        self.a.setPlaceholderText("Nhập số thứ nhất")

        self.b = QLineEdit()
        self.b.setPlaceholderText("Nhập số thứ hai")

        self.op = QComboBox()
        self.op.addItems(["+", "-", "*", "/"])

        grid.addWidget(QLabel("Số a:"), 0, 0)
        grid.addWidget(self.a, 0, 1)
        grid.addWidget(QLabel("Phép tính:"), 1, 0)
        grid.addWidget(self.op, 1, 1)
        grid.addWidget(QLabel("Số b:"), 2, 0)
        grid.addWidget(self.b, 2, 1)

        layout.addLayout(grid)

        btn = QPushButton("Tính kết quả")
        btn.clicked.connect(self.tinh)
        layout.addWidget(btn)

        self.result = QLabel("Kết quả sẽ hiển thị ở đây.")
        self.result.setAlignment(Qt.AlignCenter)
        self.result.setStyleSheet("font-size: 18px;")
        layout.addWidget(self.result)

    def tinh(self):
        try:
            a = float(self.a.text())
            b = float(self.b.text())
            op = self.op.currentText()

            if op == "+":
                kq = a + b
            elif op == "-":
                kq = a - b
            elif op == "*":
                kq = a * b
            else:
                if b == 0:
                    self.result.setText("Không thể chia cho 0!")
                    return
                kq = a / b

            self.result.setText(f"Kết quả: {kq:g}")

        except ValueError:
            QMessageBox.warning(
                self, "Lỗi nhập liệu",
                "Vui lòng nhập hai số hợp lệ."
            )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalculatorApp()
    window.show()
    sys.exit(app.exec_())
