import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QMessageBox
)


class CuaSoDangNhap(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Đăng nhập hệ thống")
        self.resize(350, 250)

        # Ô nhập tài khoản
        self.o_nhap_tai_khoan = QLineEdit()
        self.o_nhap_tai_khoan.setPlaceholderText(
            "Nhập tài khoản"
        )

        # Ô nhập mật khẩu
        self.o_nhap_mat_khau = QLineEdit()
        self.o_nhap_mat_khau.setPlaceholderText(
            "Nhập mật khẩu"
        )
        self.o_nhap_mat_khau.setEchoMode(
            QLineEdit.Password
        )

        # Nút đăng nhập
        self.nut_dang_nhap = QPushButton("Đăng nhập")

        # Bố cục giao diện
        layout = QVBoxLayout()
        layout.addWidget(QLabel("TÀI KHOẢN:"))
        layout.addWidget(self.o_nhap_tai_khoan)
        layout.addWidget(QLabel("MẬT KHẨU:"))
        layout.addWidget(self.o_nhap_mat_khau)
        layout.addWidget(self.nut_dang_nhap)

        self.setLayout(layout)

        # Kết nối nút với hàm xử lý
        self.nut_dang_nhap.clicked.connect(
            self.xu_ly_dang_nhap
        )

    def xu_ly_dang_nhap(self):
        tai_khoan = self.o_nhap_tai_khoan.text().strip()
        mat_khau = self.o_nhap_mat_khau.text()

        if tai_khoan == "" or mat_khau == "":
            QMessageBox.warning(
                self,
                "Thông báo",
                "Vui lòng nhập đầy đủ tài khoản và mật khẩu!"
            )
            return

        # Tài khoản mẫu để thực hành
        if tai_khoan == "admin" and mat_khau == "123456":
            QMessageBox.information(
                self,
                "Thành công",
                "Đăng nhập thành công!"
            )
        else:
            QMessageBox.critical(
                self,
                "Thất bại",
                "Tài khoản hoặc mật khẩu không đúng!"
            )


if __name__ == "__main__":
    app = QApplication(sys.argv)

    cua_so = CuaSoDangNhap()
    cua_so.show()

    sys.exit(app.exec_())
