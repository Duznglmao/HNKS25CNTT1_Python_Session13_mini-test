import time

LINE = "=" * 50

parking = [{
    "id": 1,
    "type": "Xe may",
    "owner": "Nguyen Van A"
},
{
    "id": 2,
    "type": "O to",
    "owner": "Tran Van B"
}]

next_id = 3

while True:
    print(f"""
{LINE}
        QUẢN LÝ BÃI XE - SMART PARKING
{LINE}
    1. Thêm xe mới vào bãi
    2. Hiển thị danh sách xe trong bãi
    3. Tìm kiếm xe theo mã (id)
    4. Xóa xe khỏi bãi (khi xe ra)
    5. Thoát chương trình
{LINE}
""")
    user_choice_input = input("Mời nhập vào lựa chọn (1-5): ").strip()
    if not user_choice_input.isdigit():
        print("Lựa chọn không hợp lệ!")
        continue
            
    user_choice = int(user_choice_input)
    if user_choice not in [1, 2, 3, 4, 5]:
        print("Vui lòng chọn các số trong khoảng từ 1 đến 5!")
        continue

    match user_choice:
        case 1:
            while True:
                type_vehicle = input("Mời nhập vào loại xe: ").strip()
                if not type_vehicle:
                    print("Loại xe không được để trống. Vui lòng nhập lại!")
                    continue
                break
            
            while True:
                owner_vehicle = input("Mời nhập vào chủ xe: ").strip()
                if not owner_vehicle:
                    print("Chủ xe không được để trống. Vui lòng nhập lại!")
                    continue
                break
                
            new_vehicle = {
                "id": next_id,
                "type": type_vehicle,
                "owner": owner_vehicle
            }
            
            parking.append(new_vehicle)
            print(f"Thêm xe mới thành công!")
            next_id += 1
            
        case 2:
            if len(parking) == 0:
                print("Bãi xe hiện đang trống!")
            else:
                print(f"\n{'ID':<5} | {'Loại xe':<15} | {'Chủ xe':<20}")
                print("-" * 50)
                for vehicle in parking:
                    print(f"{vehicle['id']:<5} | {vehicle['type']:<15} | {vehicle['owner']:<20}")
                
        case 3:
            try:
                id_search_input = input("Vui lòng nhập vào ID để tìm kiếm: ").strip()
                if not id_search_input.isdigit():
                    raise ValueError("ID tìm kiếm phải là số dương!")
                    
                id_search = int(id_search_input)
                
                is_found = None
                for vehicle in parking:
                    if vehicle["id"] == id_search:
                        is_found = vehicle
                        break
                
                if is_found is not None:
                    print(f"Kết quả tìm thấy: {is_found}")
                else:
                    raise ValueError(f"Không tìm thấy xe có ID {id_search}!")
                    
            except ValueError as e:
                print(f"Lỗi: {e}")
                
        case 4:
            try:
                delete_id_input = input("Vui lòng nhập vào ID cần xóa: ").strip()
                if not delete_id_input.isdigit():
                    raise ValueError("ID cần xóa phải là số dương!")
                    
                delete_id = int(delete_id_input)
                
                target_index = -1
                for index, vehicle in enumerate(parking):
                    if vehicle["id"] == delete_id:
                        target_index = index
                        break
                    
                if target_index == -1:
                    raise ValueError("Không tìm thấy xe để xóa!")
                else:
                    parking.pop(target_index)
                    print(f"Đã xóa xe ID {delete_id} thành công!")
                    
            except ValueError as e:
                print(f"Lỗi: {e}")
            
        case 5:
            bye = "Cảm ơn vì đã sử dụng chương trình!"
            for char in bye:
                print(char, end="", flush=True)
                time.sleep(0.1)
            break