import sqlite3
from pathlib import Path
DB = Path(__file__).with_name("phim.db")

def ket_noi():
    return sqlite3.connect(DB)

def tao_bang():
    with ket_noi() as c:
        c.execute("""CREATE TABLE IF NOT EXISTS phim(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ten_phim TEXT NOT NULL, dao_dien TEXT, the_loai TEXT,
            nam_phat_hanh INTEGER, danh_gia REAL DEFAULT 0,
            da_xem INTEGER DEFAULT 0)""")

def them_phim(ten, dao_dien, the_loai, nam, danh_gia):
    with ket_noi() as c:
        c.execute("INSERT INTO phim(ten_phim,dao_dien,the_loai,nam_phat_hanh,danh_gia) VALUES(?,?,?,?,?)",
                  (ten,dao_dien,the_loai,nam,danh_gia))

def lay_danh_sach(tu_khoa="", the_loai="Tất cả"):
    sql = "SELECT id,ten_phim,dao_dien,the_loai,nam_phat_hanh,danh_gia,da_xem FROM phim WHERE ten_phim LIKE ?"
    args = [f"%{tu_khoa}%"]
    if the_loai != "Tất cả":
        sql += " AND the_loai=?"
        args.append(the_loai)
    sql += " ORDER BY id DESC"
    with ket_noi() as c:
        return c.execute(sql,args).fetchall()

def cap_nhat_phim(pid, ten, dao_dien, the_loai, nam, danh_gia):
    with ket_noi() as c:
        c.execute("UPDATE phim SET ten_phim=?,dao_dien=?,the_loai=?,nam_phat_hanh=?,danh_gia=? WHERE id=?",
                  (ten,dao_dien,the_loai,nam,danh_gia,pid))

def xoa_phim(pid):
    with ket_noi() as c:
        c.execute("DELETE FROM phim WHERE id=?",(pid,))

def doi_trang_thai(pid, da_xem):
    with ket_noi() as c:
        c.execute("UPDATE phim SET da_xem=? WHERE id=?",(da_xem,pid))

def thong_ke_the_loai():
    with ket_noi() as c:
        return c.execute("SELECT the_loai,COUNT(*) FROM phim GROUP BY the_loai").fetchall()

def dem_trang_thai():
    with ket_noi() as c:
        a=c.execute("SELECT COUNT(*) FROM phim WHERE da_xem=1").fetchone()[0]
        b=c.execute("SELECT COUNT(*) FROM phim WHERE da_xem=0").fetchone()[0]
    return a,b
