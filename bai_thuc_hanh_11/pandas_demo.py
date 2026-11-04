import sys
import os
import pandas as pd

from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QTableWidget, QTableWidgetItem,
    QTextEdit, QMessageBox, QLabel
)


class PandasApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hoạt động 2 - Pandas")
        self.resize(850, 600)

        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("QUẢN LÝ VÀ THỐNG KÊ ĐIỂM SINH VIÊN"))

        buttons = QHBoxLayout()

        btn_load = QPushButton("Đọc file CSV")
        btn_load.clicked.connect(self.doc_csv)
        buttons.addWidget(btn_load)

        btn_stats = QPushButton("Thống kê điểm")
        btn_stats.clicked.connect(self.thong_ke)
        buttons.addWidget(btn_stats)

        layout.addLayout(buttons)

        self.table = QTableWidget()
        layout.addWidget(self.table)

        self.output = QTextEdit()
        self.output.setReadOnly(True)
        layout.addWidget(self.output)

    def doc_du_lieu(self):
        path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "diem_sinh_vien.csv"
        )
        if not os.path.exists(path):
            QMessageBox.warning(
                self, "Lỗi", "Không tìm thấy diem_sinh_vien.csv"
            )
            return None
        return pd.read_csv(path)

    def doc_csv(self):
        df = self.doc_du_lieu()
        if df is None:
            return

        self.table.setRowCount(len(df))
        self.table.setColumnCount(len(df.columns))
        self.table.setHorizontalHeaderLabels(list(df.columns))

        for i in range(len(df)):
            for j, col in enumerate(df.columns):
                self.table.setItem(
                    i, j, QTableWidgetItem(str(df.iloc[i, j]))
                )

        self.table.resizeColumnsToContents()
        self.output.setPlainText(
            f"Đã đọc thành công {len(df)} dòng, "
            f"{len(df.columns)} cột."
        )

    def thong_ke(self):
        df = self.doc_du_lieu()
        if df is None:
            return

        theo_mon = df.groupby("mon_hoc")["diem"].mean()
        theo_sv = df.groupby("ho_ten")["diem"].mean().round(2)

        text = (
            f"Kích thước dữ liệu: {df.shape}\n\n"
            f"Điểm trung bình theo môn:\n{theo_mon.to_string()}\n\n"
            f"Điểm trung bình toàn bộ: {df['diem'].mean():.2f}\n"
            f"Điểm cao nhất: {df['diem'].max()}\n"
            f"Điểm thấp nhất: {df['diem'].min()}\n\n"
            f"Điểm trung bình sinh viên:\n{theo_sv.to_string()}\n\n"
            f"Sinh viên đạt (ĐTB >= 5):\n"
            f"{theo_sv[theo_sv >= 5].to_string()}\n\n"
            f"Sinh viên chưa đạt (ĐTB < 5):\n"
            f"{theo_sv[theo_sv < 5].to_string() or 'Không có'}"
        )
        self.output.setPlainText(text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PandasApp()
    window.show()
    sys.exit(app.exec_())
