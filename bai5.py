patient_info = []

print("--- HỆ THỐNG NHẬP LIỆU DANH SÁCH BỆNH NHÂN ---")
name = input("Nhập tên bệnh nhân: ")
age = int(input("Nhập tuổi: "))
symptom = input("Nhập triệu chứng: ")

# 3. Đưa dữ liệu vào danh sách bằng phương thức append
patient_info.append(name)
patient_info.append(age)
patient_info.append(symptom)

# Hiển thị thông tin bằng cách truy xuất Index
print("\n" + "="*30)
print("     THÔNG TIN LƯU TRỮ TRONG LIST")
print("="*30)

#  Index trong Python bắt đầu từ 0
print(f"1. Tên bệnh nhân (Index 0): {patient_info[0]}")
print(f"2. Tuổi bệnh nhân (Index 1): {patient_info[1]}")
print(f"3. Triệu chứng    (Index 2): {patient_info[2]}")

print("\nToàn bộ danh sách hiện tại:", patient_info)
print("="*30)