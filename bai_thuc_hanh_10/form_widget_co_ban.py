import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QComboBox, QVBoxLayout, QMessageBox
)


class FormWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Form thông tin cá nhân")
        self.resize(350, 280)

        self.o_nhap_ten = QLineEdit()
        self.o_nhap_ten.setPlaceholderText("Nhập họ tên")

        self.chon_thanh_pho = QComboBox()
        self.chon_thanh_pho.addItems(
            ["Hà Nội", "Đà Nẵng", "Bắc Ninh", "TP.HCM", "Huế"]
        )

        self.nut_xac_nhan = QPushButton("Xác nhận")
        self.nhan_ket_qua = QLabel("")

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Họ tên:"))
        layout.addWidget(self.o_nhap_ten)
        layout.addWidget(QLabel("Thành phố:"))
        layout.addWidget(self.chon_thanh_pho)
        layout.addWidget(self.nut_xac_nhan)
        layout.addWidget(self.nhan_ket_qua)

        self.setLayout(layout)

        self.nut_xac_nhan.clicked.connect(
            self.xu_ly_xac_nhan
        )

    def xu_ly_xac_nhan(self):
        ten = self.o_nhap_ten.text().strip()
        thanh_pho = self.chon_thanh_pho.currentText()

        if ten == "":
            QMessageBox.warning(
                self, "Thông báo", "Vui lòng nhập họ tên!"
            )
            return

        self.nhan_ket_qua.setText(
            f"Xin chào {ten}, bạn ở {thanh_pho}."
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    cua_so = FormWidget()
    cua_so.show()
    sys.exit(app.exec_())
