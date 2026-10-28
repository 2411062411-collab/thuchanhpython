import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QMessageBox
)


class FormDangNhap(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Form đăng nhập")
        self.resize(350, 250)

        self.o_nhap_tai_khoan = QLineEdit()
        self.o_nhap_tai_khoan.setPlaceholderText(
            "Nhập tài khoản"
        )

        self.o_nhap_mat_khau = QLineEdit()
        self.o_nhap_mat_khau.setPlaceholderText(
            "Nhập mật khẩu"
        )
        self.o_nhap_mat_khau.setEchoMode(
            QLineEdit.Password
        )

        self.nut_dang_nhap = QPushButton("Đăng nhập")

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Tài khoản:"))
        layout.addWidget(self.o_nhap_tai_khoan)
        layout.addWidget(QLabel("Mật khẩu:"))
        layout.addWidget(self.o_nhap_mat_khau)
        layout.addWidget(self.nut_dang_nhap)

        self.setLayout(layout)

        self.nut_dang_nhap.clicked.connect(
            self.xu_ly_dang_nhap
        )

    def xu_ly_dang_nhap(self):
        tai_khoan = self.o_nhap_tai_khoan.text().strip()
        mat_khau = self.o_nhap_mat_khau.text()

        if not tai_khoan or not mat_khau:
            QMessageBox.warning(
                self,
                "Lỗi",
                "Vui lòng nhập đầy đủ tài khoản và mật khẩu!"
            )
            return

        QMessageBox.information(
            self,
            "Thông báo",
            f"Đăng nhập minh họa thành công: {tai_khoan}"
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    cua_so = FormDangNhap()
    cua_so.show()
    sys.exit(app.exec_())
