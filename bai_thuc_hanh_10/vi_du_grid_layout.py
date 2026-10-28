import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel,
    QPushButton, QGridLayout
)


class ViDuGridLayout(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ví dụ QGridLayout")
        self.resize(400, 250)

        layout = QGridLayout()

        layout.addWidget(QLabel("Họ tên:"), 0, 0)
        layout.addWidget(QLabel("Nguyễn Đăng Cảnh"), 0, 1)

        layout.addWidget(QLabel("Tuổi:"), 1, 0)
        layout.addWidget(QLabel("20"), 1, 1)

        nut_luu = QPushButton("Lưu")
        nut_huy = QPushButton("Hủy")

        layout.addWidget(nut_luu, 2, 0)
        layout.addWidget(nut_huy, 2, 1)

        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    cua_so = ViDuGridLayout()
    cua_so.show()
    sys.exit(app.exec_())
