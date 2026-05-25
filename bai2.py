name_patient = input("Nhập tên bệnh nhân : ")


# Chuyển đổi từ 'string' sang 'float' để có thể tính toán
weight = float(input("Nhập cân nặng bệnh nhân : "))

print("\n--- KIỂM TRA DỮ LIỆU LƯU TRỮ ---")
print("Bệnh nhân : ", name_patient)
print("Cân nặng đã nhập : ", weight)

# Kiểm tra kiểu dữ liệu sau khi sửa
print(" Kiểu dữ liệu đang lưu là : ", type(weight))