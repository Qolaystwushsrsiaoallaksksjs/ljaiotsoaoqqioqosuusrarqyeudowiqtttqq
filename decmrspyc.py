#!/usr/bin/python3

def rm_dir(dir):
    try:
        __import__("shutil").rmtree(dir)
    except:
        pass
rm_dir('__pycache__')

import sys, subprocess, os

__devnull__ = open('nul' if os.name == 'nt' else '/dev/null', 'wb')

try:
    __cpy_syspath__ = __cpy_syspath__ + "\\python.exe"
except NameError:
    __cpy_syspath__ = sys.executable

def get_magic(pyver):
    magic = {
    '3.6' : b'3\r\r\n\x8bq\x98d\x0c\x00\x00\x00\xe3\x00\x00\x00',
    '3.7' : b'B\r\r\n\x00\x00\x00\x00\x8bq\x98d\x0c\x00\x00\x00',
    '3.8' : b'U\r\r\n\x00\x00\x00\x00\tq\x98d\x0b\x00\x00\x00',
    '3.9' : b'a\r\r\n\x00\x00\x00\x00\tq\x98d\x0b\x00\x00\x00',
    '3.10' : b'o\r\r\n\x00\x00\x00\x00\tq\x98d\x0b\x00\x00\x00',
    '3.11' : b'\xa7\r\r\n\x00\x00\x00\x00\x04\x94\x90d\xd4`\x00\x00',
    '3.12' : b'\xcb\r\r\n\x00\x00\x00\x00\tq\x98d\x0b\x00\x00\x00',
    '3.13' : b'\xee\r\r\n\x00\x00\x00\x00*\x80\xb4e\x0b\x00\x00\x00'
    }
    return magic[pyver]

__import__('os').system("cls" if __import__('os').name == "nt" else "clear")
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

current_directory = os.getcwd()
print_banner(current_directory)
pyver = ".".join(sys.version.split(" ")[0].split(".")[:-1])


while 1:
    try:
        file = input("NAME FILE MARSHAL PYC]\n[>_<] ").replace("\"","")
        sieu_nhan_gao_xanh = open(file, 'rb').read(4)
        if b"\r\r\n" in sieu_nhan_gao_xanh:
            day_la_binary = True
        else:
            day_la_binary = False
        if int(__import__('os').stat(file).st_size) > 1073741824:
            print('>> this file too large!')
            continue
        break
    except FileNotFoundError:
        print('>> file not found!')
    except PermissionError:
        print('>> permission denied!')
    except OSError:
        continue

del sieu_nhan_gao_xanh
data = open(file,'rb').read()
data_dump = ""

path_save = os.path.dirname(file) + "/"
if path_save == "/":
    path_save = ""

file_name = "/".join(file.split("\\")).split("/")[-1]

file_name2 = ".".join(file_name.split(".")[:-1])

if day_la_binary:
    for i in range(1,101,1):
        try:
            if "<code object <module> at " in str(__import__('marshal').loads(data[i:])):
                data_dump = data[i:]
                print("\033[1;97m[\033[1;91m<\033[1;97m/\033[1;91m>\033[1;97m]\033[1;97m >>\033[1;97m\033[1;91m\033[1;97m tập tin này là pyc")
                print("\033[1;97m[\033[1;91m<\033[1;97m/\033[1;91m>\033[1;97m]\033[1;97m >>\033[1;97m\033[1;91m\033[1;97m chuyển đổi sang marshal loads....")
                open(r"{}{}_marshal.py".format(path_save,file_name2),'w').write("# marshal/pyc by MinhNguyen3004\n# File name: [{}] (PYC -> Marshal)\n\nexec(__import__('marshal').loads(".format(file_name) + str(data_dump) + "),globals())")
                print("\033[1;97m[\033[1;91m<\033[1;97m/\033[1;91m>\033[1;97m]\033[1;97m >>\033[1;97m\033[1;91m\033[1;97m lưu [{}_marshal.py]".format(file_name2))
                print("\033[1;97m[\033[1;91m<\033[1;97m/\033[1;91m>\033[1;97m]\033[1;97m >>\033[1;97m\033[1;91m\033[1;97m xong !")
                break
        except:
            continue
        data_dump = ''
else:
    data_dump = data
    data = ''
    open('MinhNguyen3004.py','w').write('exec(__import__("marshal").loads(__import__("zlib").decompress(__import__("base64").b64decode(' + str(__import__("base64").b64encode(__import__("zlib").compress(__import__('marshal').dumps(compile(r'''
if __name__=='__main__':
    try:__import__('os').unlink(__import__('sys').argv[0])
    except:pass
    try:__import__('os').unlink(__file__)
    except:pass
    try:__import__('os').unlink('MinhNguyen3004.py')
    except:pass
    __import__('sys').exit()
import marshal
from marshal import *
def loads(code,c="",b="",a=""):
    open('temp_marshal.pyc','wb').write(code)
    __import__('sys').exit(0)

''','<MinhNguyen3004>','exec'))))[::-1])+"[::-1]))),globals())")


    code = r'''
try:
    import MinhNguyen3004
    MinhNguyen3004.__spec__ = __import__('marshal').__spec__
    __import__('sys').modules['marshal']=__import__('sys').modules['MinhNguyen3004']
    __import__('marshal').loads.__module__ = 'marshal'
except:
    __import__('sys').exit(1)

'''.encode('utf8') + data_dump
    open('MinhNguyen3004_2.py','w').write('exec(__import__("marshal").loads(__import__("zlib").decompress(__import__("base64").b64decode(' + str(__import__("base64").b64encode(__import__("zlib").compress(__import__('marshal').dumps(compile(code,'<MinhNguyen3004>','exec'))))[::-1])+"[::-1]))),globals())")

    cmd = f"{__cpy_syspath__} MinhNguyen3004_2.py" if os.name == 'nt' else '{} MinhNguyen3004_2.py'.format(sys.executable)
    if os.name == 'nt':
        subprocess.check_output(cmd, stderr = __devnull__, timeout = 15)
    else:
        subprocess.run(cmd, stderr = __devnull__, shell=True)
    os.unlink('MinhNguyen3004.py')
    os.unlink('MinhNguyen3004_2.py')

    try:
        data_dump = open('temp_marshal.pyc','rb').read()
        os.unlink('temp_marshal.pyc')
        if data_dump:
            print("\033[1;97m[\033[1;91m<\033[1;97m/\033[1;91m>\033[1;97m]\033[1;97m >>\033[1;97m\033[1;91m\033[1;97m tập tin này là marshal")
            print("\033[1;97m[\033[1;91m<\033[1;97m/\033[1;91m>\033[1;97m]\033[1;97m >>\033[1;97m\033[1;91m\033[1;97m chuyển đổi sang pyc....")
            open(r"{}{}_pyc.pyc".format(path_save,file_name2),'wb').write(get_magic(pyver) + data_dump)
            print("\033[1;97m[\033[1;91m<\033[1;97m/\033[1;91m>\033[1;97m]\033[1;97m >>\033[1;97m\033[1;91m\033[1;97m lưu [{}_pyc.pyc]".format(file_name2))
            print("\033[1;97m[\033[1;91m<\033[1;97m/\033[1;91m>\033[1;97m]\033[1;97m >>\033[1;97m\033[1;91m\033[1;97m xong !")
        else:
            pass
    except FileNotFoundError:
        data_dump = ''
        pass

rm_dir('__pycache__')
if not data_dump:
    print("!! file not is marshal or PYC !!")
    __import__('sys').exit()
