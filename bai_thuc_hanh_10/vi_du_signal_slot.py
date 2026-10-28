import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel,
    QPushButton, QLineEdit, QVBoxLayout
)


class ViDuSignalSlot(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ví dụ Signal - Slot")
        self.resize(350, 200)

        self.o_nhap = QLineEdit()
        self.o_nhap.setPlaceholderText("Nhập nội dung...")

        self.nut_hien_thi = QPushButton("Hiển thị")
        self.nhan_ket_qua = QLabel("Chưa có nội dung")

        layout = QVBoxLayout()
        layout.addWidget(self.o_nhap)
        layout.addWidget(self.nut_hien_thi)
        layout.addWidget(self.nhan_ket_qua)
        self.setLayout(layout)

        self.nut_hien_thi.clicked.connect(
            self.hien_thi_noi_dung
        )

    def hien_thi_noi_dung(self):
        noi_dung = self.o_nhap.text().strip()

        if noi_dung:
            self.nhan_ket_qua.setText(noi_dung)
        else:
            self.nhan_ket_qua.setText(
                "Bạn chưa nhập nội dung!"
            )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    cua_so = ViDuSignalSlot()
    cua_so.show()
    sys.exit(app.exec_())
