import random
import os
import string
os.system('clear')
# Hàm tạo tên file ngẫu nhiên
def random_filename(extension='py'):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(10)) + '.' + extension

# Nhập tên file cần đọc
print("\033[1;97m[———————[COPYRIGHT : MINHNGUYEN3004 AND NGOCVU3007]———————]")

print("\033[97m[#########################################################]")
import os

def print_banner(directory_path):
    # In thông báo


    # Lấy danh sách các file trong thư mục
    try:
        files = os.listdir(directory_path)
        file_count = 0  # Đếm số lượng file đã in trên dòng hiện tại

        # In danh sách các file
        for file in files:
            if os.path.isfile(os.path.join(directory_path, file)):
                print(f"\033[97m\033[97m[ \033[97m\033[97m{file}\033[97m\033[97m ]", end=" ")
                file_count += 1
                if file_count % 3 == 0:
                    print()  # Xuống dòng sau mỗi 3 file

        # Nếu có file còn lại sau vòng lặp
        if file_count % 3 != 0:
            print()

    except FileNotFoundError:
        print("\033[97m[#########################################################]")
        print("\033[97m║ Error : Thư mục không tồn tại !")
        print("\033[97m[#########################################################]")

    print("\033[97m[#########################################################]")
    

# Thay đổi đường dẫn nếu cần, hoặc sử dụng thư mục hiện tại
current_directory = os.getcwd()
print_banner(current_directory)
input_file = input("[NAME FILE DISTURBANCE]\n[>_<] ")
print("\033[97m[#########################################################]")

# Đọc nội dung từ file đã cho
with open(input_file, 'rb') as f:
    a = f.read()

# Tạo tên file ngẫu nhiên
random_file = random_filename()

# Ghi nội dung vào file ngẫu nhiên
with open(random_file, 'wb') as f:
    # Ghi dòng "a = " và nội dung của a vào file
    f.write(b"a = " + a + b"\n")  
    # Ghi thêm câu lệnh mở và ghi vào file MinhNguyen3004.py
    f.write(b"open('MinhNguyen3004.py', 'wb').write(a)\n")

# Ghi nội dung vào file 1.py (ghi thêm vào cuối file)
with open('1.py', 'ab') as f:
    f.write(a)

# Lấy tên file hiện tại (h.py)
current_file = os.path.basename(__file__)

# Thực thi file vừa tạo
os.system(f'python {random_file}')

# Danh sách các file cần giữ lại
files_to_keep = ['MinhNguyen3004.py', 'dec.py', 'ha.py', 'hi.py', 'j.py', 'jj.py', 'jjj.py', 'cc.py', '2.py', 'hook.py', 'hai.py', 'vc.py', 'vl.py', 'decmrs1.py', 'obf_and_deobf.py', current_file]

# Xóa tất cả các file không nằm trong danh sách giữ lại
for file in os.listdir('.'):
    if file not in files_to_keep and os.path.isfile(file):
        os.remove(file)

print("[SAVE FILE]\n[>_<] MinhNguyen3004.py")
print("\033[97m[#########################################################]")