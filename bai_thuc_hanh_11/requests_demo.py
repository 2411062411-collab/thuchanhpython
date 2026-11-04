import sys
import requests

from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QPushButton, QTextEdit, QLabel
)


class RequestsApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hoạt động 5 - Requests API")
        self.resize(650, 450)

        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("LẤY DỮ LIỆU TỪ API"))

        btn_github = QPushButton("Thông tin GitHub CPython")
        btn_github.clicked.connect(self.github)
        layout.addWidget(btn_github)

        btn_rate = QPushButton("Tỷ giá USD/VND")
        btn_rate.clicked.connect(self.ty_gia)
        layout.addWidget(btn_rate)

        self.output = QTextEdit()
        self.output.setReadOnly(True)
        layout.addWidget(self.output)

    def github(self):
        self.output.setPlainText("Đang tải dữ liệu GitHub...")
        QApplication.processEvents()

        try:
            r = requests.get(
                "https://api.github.com/repos/python/cpython",
                timeout=15
            )
            r.raise_for_status()
            data = r.json()

            text = (
                f"Tên repository: {data.get('full_name')}\n"
                f"Số lượt gắn sao: {data.get('stargazers_count')}\n"
                f"Ngôn ngữ: {data.get('language')}"
            )
        except (requests.RequestException, ValueError) as e:
            text = f"Không lấy được dữ liệu:\n{e}"

        self.output.setPlainText(text)

    def ty_gia(self):
        self.output.setPlainText("Đang tải tỷ giá...")
        QApplication.processEvents()

        try:
            r = requests.get(
                "https://open.er-api.com/v6/latest/USD",
                timeout=15
            )
            r.raise_for_status()
            data = r.json()

            if data.get("result") == "success":
                rate = data["rates"]["VND"]
                text = f"1 USD = {rate:,.0f} VND"
            else:
                text = "API không trả về tỷ giá hợp lệ."
        except (requests.RequestException, ValueError, KeyError) as e:
            text = f"Không lấy được tỷ giá:\n{e}"

        self.output.setPlainText(text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RequestsApp()
    window.show()
    sys.exit(app.exec_())
