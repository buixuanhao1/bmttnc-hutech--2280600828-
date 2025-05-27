soGL = float(input("Nhập số giờ làm mỗi tuần: "))
luong = float(input("Nhập thù lao trên mỗi giờ làm tiêu chuẩn: "))
gio_tieu_chuan = 44
gio_vuot_chuan = max(0, soGL - gio_tieu_chuan)
thuc_linh = gio_tieu_chuan * luong + gio_vuot_chuan * luong * 1.5
print(f"Số tiền thực lĩnh cua rnhana viên : {thuc_linh}")