import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas
from matplotlib.figure import Figure
import csdl_phim as db

THE_LOAI=["Hành động","Tình cảm","Hài","Khoa học viễn tưởng","Hoạt hình","Kinh dị","Tài liệu","Tội phạm","Khác"]

class BieuDo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Thống kê phim theo thể loại")
        self.resize(800,500)
        fig=Figure(figsize=(8,4))
        canvas=Canvas(fig)
        layout=QVBoxLayout(self); layout.addWidget(canvas)
        ax=fig.add_subplot(111); data=db.thong_ke_the_loai()
        if data:
            ax.bar([x[0] for x in data],[x[1] for x in data])
            ax.set_title("Số lượng phim theo thể loại")
            ax.set_xlabel("Thể loại"); ax.set_ylabel("Số phim")
            ax.tick_params(axis="x",labelrotation=25)
        else:
            ax.text(.5,.5,"Chưa có dữ liệu phim",ha="center",va="center")
            ax.set_axis_off()
        fig.tight_layout(); canvas.draw()

class UngDung(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PHẦN MỀM QUẢN LÝ PHIM CÁ NHÂN")
        self.resize(1100,700); self.pid=None
        root=QWidget(); self.setCentralWidget(root); main=QVBoxLayout(root)
        title=QLabel("QUẢN LÝ PHIM CÁ NHÂN")
        title.setAlignment(Qt.AlignCenter); title.setStyleSheet("font-size:23px;font-weight:bold;padding:10px")
        main.addWidget(title)
        group=QGroupBox("Thông tin phim"); form=QFormLayout(group)
        self.ten=QLineEdit(); self.dao_dien=QLineEdit()
        self.the_loai=QComboBox(); self.the_loai.addItems(THE_LOAI)
        self.nam=QSpinBox(); self.nam.setRange(1888,2100); self.nam.setValue(2024)
        self.danh_gia=QDoubleSpinBox(); self.danh_gia.setRange(0,10); self.danh_gia.setSingleStep(.5); self.danh_gia.setSuffix(" / 10")
        form.addRow("Tên phim:",self.ten); form.addRow("Đạo diễn:",self.dao_dien)
        form.addRow("Thể loại:",self.the_loai); form.addRow("Năm phát hành:",self.nam); form.addRow("Đánh giá:",self.danh_gia)
        main.addWidget(group)
        buttons=QHBoxLayout()
        for label,fn in [("Thêm phim",self.them),("Cập nhật",self.cap_nhat),("Xóa phim",self.xoa),("Đánh dấu đã xem",self.danh_dau),("Làm mới",self.lam_moi)]:
            b=QPushButton(label); b.clicked.connect(fn); buttons.addWidget(b)
        main.addLayout(buttons)
        search=QHBoxLayout(); self.tim=QLineEdit(); self.tim.setPlaceholderText("Nhập tên phim cần tìm...")
        self.loc=QComboBox(); self.loc.addItems(["Tất cả"]+THE_LOAI)
        self.tim.textChanged.connect(self.tai_bang); self.loc.currentTextChanged.connect(self.tai_bang)
        search.addWidget(QLabel("Tìm kiếm:")); search.addWidget(self.tim); search.addWidget(QLabel("Lọc thể loại:")); search.addWidget(self.loc)
        main.addLayout(search)
        self.bang=QTableWidget(0,7); self.bang.setHorizontalHeaderLabels(["ID","Tên phim","Đạo diễn","Thể loại","Năm","Đánh giá","Trạng thái"])
        self.bang.setSelectionBehavior(QTableWidget.SelectRows); self.bang.setEditTriggers(QTableWidget.NoEditTriggers)
        self.bang.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch); self.bang.itemSelectionChanged.connect(self.chon)
        main.addWidget(self.bang)
        bottom=QHBoxLayout(); self.tong=QLabel(); chart=QPushButton("Xem biểu đồ thống kê"); chart.clicked.connect(self.mo_bieu_do)
        bottom.addWidget(self.tong); bottom.addStretch(); bottom.addWidget(chart); main.addLayout(bottom)
        self.tai_bang()

    def du_lieu(self):
        ten=self.ten.text().strip()
        if not ten:
            QMessageBox.warning(self,"Thiếu thông tin","Vui lòng nhập tên phim."); return None
        return (ten,self.dao_dien.text().strip(),self.the_loai.currentText(),self.nam.value(),self.danh_gia.value())

    def them(self):
        d=self.du_lieu()
        if d: db.them_phim(*d); self.lam_moi(); QMessageBox.information(self,"Thông báo","Đã thêm phim.")

    def cap_nhat(self):
        if self.pid is None:
            QMessageBox.warning(self,"Thông báo","Hãy chọn phim trong bảng."); return
        d=self.du_lieu()
        if d: db.cap_nhat_phim(self.pid,*d); self.lam_moi(); QMessageBox.information(self,"Thông báo","Đã cập nhật phim.")

    def xoa(self):
        if self.pid is None:
            QMessageBox.warning(self,"Thông báo","Hãy chọn phim cần xóa."); return
        if QMessageBox.question(self,"Xác nhận","Bạn có chắc muốn xóa phim này?")==QMessageBox.Yes:
            db.xoa_phim(self.pid); self.lam_moi()

    def danh_dau(self):
        if self.pid is None:
            QMessageBox.warning(self,"Thông báo","Hãy chọn phim."); return
        row=self.bang.currentRow()
        status=1 if self.bang.item(row,6).text()=="Chưa xem" else 0
        db.doi_trang_thai(self.pid,status); self.tai_bang()

    def chon(self):
        row=self.bang.currentRow()
        if row<0: self.pid=None; return
        self.pid=int(self.bang.item(row,0).text())
        self.ten.setText(self.bang.item(row,1).text()); self.dao_dien.setText(self.bang.item(row,2).text())
        self.the_loai.setCurrentText(self.bang.item(row,3).text()); self.nam.setValue(int(self.bang.item(row,4).text()))
        self.danh_gia.setValue(float(self.bang.item(row,5).text()))

    def lam_moi(self):
        self.pid=None; self.ten.clear(); self.dao_dien.clear(); self.the_loai.setCurrentIndex(0)
        self.nam.setValue(2024); self.danh_gia.setValue(0); self.bang.clearSelection(); self.tai_bang()

    def tai_bang(self,*args):
        ds=db.lay_danh_sach(self.tim.text(),self.loc.currentText())
        self.bang.setRowCount(len(ds))
        for i,p in enumerate(ds):
            values=list(p[:6])+["Đã xem" if p[6] else "Chưa xem"]
            for j,v in enumerate(values):
                item=QTableWidgetItem(str(v))
                if j in (0,4,5): item.setTextAlignment(Qt.AlignCenter)
                self.bang.setItem(i,j,item)
        da_xem,chua_xem=db.dem_trang_thai()
        self.tong.setText(f"Tổng số phim: {da_xem+chua_xem} | Đã xem: {da_xem} | Chưa xem: {chua_xem}")

    def mo_bieu_do(self):
        self.chart=BieuDo(); self.chart.show()

if __name__=="__main__":
    db.tao_bang()
    app=QApplication(sys.argv); window=UngDung(); window.show(); sys.exit(app.exec_())
