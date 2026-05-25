print("--- HỆ THỐNG QUẢN LÝ PHÒNG KHÁM ĐA KHOA ---")
print("Vui lòng nhập thông tin bệnh nhân mới bên dưới:\n")

full_name = input("Họ và tên bệnh nhân: ").strip().title()
patient_code = input("Mã bệnh án (BAxxxx): ").strip().upper()
department = input("Khoa/Phòng khám chỉ định: ").strip()


print("\n" + "="*30)
print("     PHIẾU KHÁM BỆNH ĐIỆN TỬ")
print("="*30)

# Sử dụng F-string để hiển thị theo đúng định dạng yêu cầu
electronic_ticket = f"Bệnh nhân: {full_name} - Mã BA: {patient_code} - Chuyển tới: {department}"

print(electronic_ticket)
print("="*30)
print("XÁC NHẬN: Thông tin đã được lưu vào hệ thống.")