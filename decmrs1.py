import marshal
import os, sys, time
os.system('clear')
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
while True:
    cc = input('[NAME FILE MARSHAL]\n[>_<] ')
    print("\033[97m[#########################################################]")
    try:
        with open(cc, 'r') as u:
            content = u.read()
            break
    except Exception as e:
        print(str(e))
        continue
file_name = cc.replace('.py', '').replace('.', '').replace('.php', '').replace('.txt', '')
folder = f"{file_name}_dump"
if not os.path.exists(folder):
    os.mkdir(folder)
x = marshal.loads
def dump(*j):
    global folder, count, file_name, cc
    h = x(*j)
    a = (f"exec(__import__('marshal').loads({j[0]}))")
    if "exec(__import__('marshal').loads(<memory at" not in a:
        count += 1
        print(f"\033[1;97m[\033[1;91m<\033[1;97m/\033[1;91m>\033[1;97m]\033[1;97m >>\033[1;97m\033[1;91m \033[1;97m[\033[1;93m{count}\033[1;97m] dump_file --\033[1;91m>\033[1;92m {file_name}_\033[1;97m(\033[1;96mmarshal\033[1;97m)\033[1;97m!")
        copyright = f"# Decode By MinhNguyen3004\n# File Name : [{cc}]\n# Dump Count -> {count}"
        with open(f"{folder}/dump_{count}_{file_name}.py", "w") as o:
            o.write(f"{copyright}\n\n{a}")
    return h
marshal.loads = dump
count = 0

time.sleep(0.05)
exec(content)
print("\033[97m[#########################################################]")
