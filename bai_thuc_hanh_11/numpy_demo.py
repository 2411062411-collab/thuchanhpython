import sys
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QPushButton, QTextEdit, QLabel
)


class NumPyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hoạt động 1 - NumPy")
        self.resize(650, 450)

        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("THỰC HÀNH THƯ VIỆN NUMPY"))

        btn = QPushButton("Chạy chương trình")
        btn.clicked.connect(self.chay)
        layout.addWidget(btn)

        self.output = QTextEdit()
        self.output.setReadOnly(True)
        layout.addWidget(self.output)

    def chay(self):
        diem_list = [8.5, 7.0, 9.2, 6.5, 5.5]
        diem = np.array(diem_list)
        ma_tran = np.array([[1, 2, 3], [4, 5, 6]])

        text = (
            f"Danh sách Python: {diem_list}\n"
            f"Mảng NumPy: {diem}\n"
            f"Cộng thêm 0.5: {diem + 0.5}\n"
            f"Trung bình: {np.mean(diem):.2f}\n"
            f"Lớn nhất: {np.max(diem)}\n"
            f"Nhỏ nhất: {np.min(diem)}\n"
            f"Độ lệch chuẩn: {np.std(diem):.2f}\n\n"
            f"Ma trận:\n{ma_tran}\n"
            f"Kích thước: {ma_tran.shape}\n"
            f"Ma trận nhân 2:\n{ma_tran * 2}"
        )
        self.output.setPlainText(text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NumPyApp()
    window.show()
    sys.exit(app.exec_())
