patient_id = input("Nhập mã bệnh nhân (Ví dụ: BN999): ")

# Ép kiểu Float cho nhiệt độ
temperature = float(input("Nhập nhiệt độ cơ thể: "))

# Ép kiểu Int cho nhịp tim
heart_rate = int(input("Nhập nhịp tim: "))

print("\n--- KẾT QUẢ CHUẨN HÓA DỮ LIỆU ---")
print(f"Mã bệnh nhân: {patient_id}")

print(f"Nhiệt độ cơ thể: {temperature} độ C")
print(f" => Kiểu dữ liệu hệ thống ghi nhận: {type(temperature)}")

print(f"Nhịp tim: {heart_rate} nhịp/phút")
print(f" => Kiểu dữ liệu hệ thống ghi nhận: {type(heart_rate)}")

print("-" * 33)
print("Thông báo: Dữ liệu hợp lệ. Màn hình Monitor đã sẵn sàng kết nối!")