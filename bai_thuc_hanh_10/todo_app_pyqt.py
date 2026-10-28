import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QListWidget, QVBoxLayout,
    QHBoxLayout, QMessageBox
)
from PyQt5.QtGui import QColor


class TodoApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Quản lý công việc - To-do List")
        self.resize(500, 400)

        tieu_de = QLabel("DANH SÁCH CÔNG VIỆC")
        tieu_de.setStyleSheet(
            "font-size: 20px; font-weight: bold;"
        )

        self.o_nhap = QLineEdit()
        self.o_nhap.setPlaceholderText("Nhập công việc mới...")

        self.nut_them = QPushButton("Thêm")
        self.nut_them.clicked.connect(self.them_cong_viec)

        hang_nhap = QHBoxLayout()
        hang_nhap.addWidget(self.o_nhap)
        hang_nhap.addWidget(self.nut_them)

        self.danh_sach = QListWidget()

        self.nut_hoan_thanh = QPushButton("Hoàn thành")
        self.nut_hoan_thanh.clicked.connect(
            self.danh_dau_hoan_thanh
        )

        self.nut_xoa = QPushButton("Xóa công việc")
        self.nut_xoa.clicked.connect(self.xoa_cong_viec)

        hang_nut = QHBoxLayout()
        hang_nut.addWidget(self.nut_hoan_thanh)
        hang_nut.addWidget(self.nut_xoa)

        layout = QVBoxLayout()
        layout.addWidget(tieu_de)
        layout.addLayout(hang_nhap)
        layout.addWidget(self.danh_sach)
        layout.addLayout(hang_nut)

        self.setLayout(layout)

    def them_cong_viec(self):
        cong_viec = self.o_nhap.text().strip()

        if not cong_viec:
            QMessageBox.warning(
                self, "Lỗi", "Vui lòng nhập công việc!"
            )
            return

        self.danh_sach.addItem(cong_viec)
        self.o_nhap.clear()

    def danh_dau_hoan_thanh(self):
        vi_tri = self.danh_sach.currentRow()

        if vi_tri < 0:
            QMessageBox.warning(
                self, "Lỗi", "Hãy chọn công việc!"
            )
            return

        muc = self.danh_sach.item(vi_tri)

        if not muc.text().startswith("✓ "):
            muc.setText("✓ " + muc.text())
            muc.setForeground(QColor("gray"))

    def xoa_cong_viec(self):
        vi_tri = self.danh_sach.currentRow()

        if vi_tri < 0:
            QMessageBox.warning(
                self, "Lỗi", "Hãy chọn công việc cần xóa!"
            )
            return

        self.danh_sach.takeItem(vi_tri)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    cua_so = TodoApp()
    cua_so.show()
    sys.exit(app.exec_())
