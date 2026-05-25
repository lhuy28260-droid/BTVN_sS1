import random
print("--- KIOSK KHAI BÁO Y TẾ TỰ PHỤC VỤ ---")
print("Vui lòng nhập chính xác các thông tin dưới đây.\n")

patient_name = input("1. Nhập họ tên (VD: Nguyen Van A): ").strip().title()
gender = input("2. Giới tính (Nam/Nu): ").strip()
birth_year_raw = input("3. Năm sinh (VD: 1998): ")
phone_number = input("4. Số điện thoại: ")
email = input("5. Email liên lạc: ")
symptom = input("6. Triệu chứng ban đầu: ")
fee_raw = input("7. Chi phí khám (VD: 200000.5): ")

# ==========================================
# KHỐI 2: XỬ LÝ ÉP KIỂU & CHUẨN HÓA DỮ LIỆU
# ==========================================
# Ép kiểu dữ liệu số
birth_year = int(birth_year_raw)
medical_fee = float(fee_raw)

# Tạo 3 số ngẫu nhiên cho mã bệnh nhân
random_suffix = random.randint(100, 999)

# Sinh mã bệnh nhân tự động theo quy tắc: BN + Năm sinh + 3 số ngẫu nhiên
patient_id = f"BN{birth_year}{random_suffix}"

# ==========================================
# KHỐI 3: HIỂN THỊ THẺ THÔNG TIN BỆNH NHÂN
# ==========================================
print("\n" + "═"*40)
print(f"{'THẺ THÔNG TIN BỆNH NHÂN':^40}")
print("═"*40)
print(f"Mã bệnh nhân   : {patient_id}")
print(f"Họ và tên      : {patient_name}")
print(f"Giới tính      : {gender}")
print(f"Năm sinh       : {birth_year}")
print(f"Số điện thoại  : {phone_number}")
print(f"Email          : {email}")
print(f"Triệu chứng    : {symptom}")
print(f"Chi phí dự kiến: {medical_fee:,.1f} VNĐ")
print("═"*40)

# ==========================================
# KHỐI 4: LOG HỆ THỐNG (DÀNH CHO IT/ADMIN)
# ==========================================
print("\n[LOG HỆ THỐNG - KIỂM TRA KIỂU DỮ LIỆU]")
print(f"- patient_id   : {type(patient_id)}")
print(f"- birth_year   : {type(birth_year)}")
print(f"- medical_fee  : {type(medical_fee)}")
print(f"- patient_name : {type(patient_name)}")
print("-" * 40)
print("Thông báo: Dữ liệu đã được chuẩn hóa và lưu trữ thành công!")