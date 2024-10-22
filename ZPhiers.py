import zipfile
import rarfile
import os
import itertools
import string
import time
from google.protobuf.json_format import MessageToJson
from pystyle import *
from setuptools.command.develop import develop
Write.Print ("""
 ________    ______ .______          ___       ______  __  ___  __  .__   __.   _______ 
|       /   /      ||   _  \        /   \     /      ||  |/  / |  | |  \ |  |  /  _____|
`---/  /   |  ,----'|  |_)  |      /  ^  \   |  ,----'|  '  /  |  | |   \|  | |  |  __  
   /  /    |  |     |      /      /  /_\  \  |  |     |    <   |  | |  . `  | |  | |_ | 
  /  /----.|  `----.|  |\  \----./  _____  \ |  `----.|  .  \  |  | |  |\   | |  |__| | 
 /________| \______|| _| `._____/__/     \__\ \______||__|\__\ |__| |__| \__|  \______|   
                                                                                         INFO.. [
                                                                                         
                                                                                        ✮ V0.1.2.3v
                                                                                        ✮ Follower : 12 Follower
                                                                                        ✮ Followers : 25 Followers
                                                                                        ✮ Likes : 10 Linkes
                                                                                        ✮ Views : 98
                                                                                        ✮ Downloads or Useed Tool.. : 40 Done 
                                                                                        ✮ Tools : 15 .T
                                                                                        ✮ Versions of This Tool : 0 .T.v
                                                                                        ✮ Created By : Mohammed Alaa Mohammed
                                                                                         
                                                                                         ]
                                                                                         
""",Colors.blue_to_cyan ,interval=.001)
Write.Print('\n[-] Message : It may take a while to fetch the password for Your file.\n', Colors.green_to_cyan, interval=0.030)
Write.Print('\n[-] GitHub : https://www.github.com/DARKGITHUBPRO\n', Colors.red_to_yellow, interval=0.020)

# دالة لفك ضغط ملفات zip باستخدام كلمة المرور
def extract_zip(file_path, password):
    try:
        with zipfile.ZipFile(file_path) as zf:
            zf.extractall(pwd=password.encode())  # محاولة استخراج الملفات باستخدام كلمة المرور
        print("Password found:", password)
        return True
    except Exception as e:
        return False

# دالة لفك ضغط ملفات rar باستخدام كلمة المرور
def extract_rar(file_path, password):
    try:
        with rarfile.RarFile(file_path) as rf:
            rf.extractall(pwd=password)  # محاولة استخراج الملفات باستخدام كلمة المرور
        print("Password found:", password)
        return True
    except Exception as e:
        return False

# دالة لتنفيذ هجوم القاموس على الملف المضغوط باستخدام مجموعة موسعة من الأحرف والأرقام والرموز
def brute_force(file_path, file_type, min_length, max_length, use_digits, use_symbols, use_letters):
    chars = ''
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation
    if use_letters:
        chars += string.ascii_letters

    start_time = time.time()
    for length in range(min_length, max_length + 1):  # ضبط النطاق لطول كلمة المرور المراد تجربتها
        for password in map(lambda x: ''.join(x), itertools.product(chars, repeat=length)):
            print("\33[33;1m[-] Trying password:\33[39;0m", password)  # طباعة كلمات المرور المجربة
            if file_type == 'zip' and extract_zip(file_path, password):  # تجربة كلمة المرور على ملفات zip
                print("Time taken:", time.time() - start_time, "seconds")
                return
            elif file_type == 'rar' and extract_rar(file_path, password):  # تجربة كلمة المرور على ملفات rar
                print("Time taken:", time.time() - start_time, "seconds")
                return
    print("\33[31;1mPassword not found\33[39;0m")

# الدالة الرئيسية للبرنامج
def main():
    file_path = input("\n[-] Enter the path of the file (e.g., C:/files/archive.zip): ")  # طلب إدخال مسار الملف من المستخدم
    if not os.path.isfile(file_path):
        print("\n[-]\33[36;1m File does not exist. Please enter a valid file path.\33[39;0m")
        return

    file_type = os.path.splitext(file_path)[1][1:].lower()  # استخراج نوع الملف من الامتداد
    if file_type not in ['zip', 'rar']:
        print("\33[31;1m[-] Unsupported file type. Please enter a zip or rar file.\33[39;0m")
        return

    min_length = int(input("\n[-] Enter the minimum length of the password: "))  # طلب إدخال الحد الأدنى لطول كلمة المرور
    max_length = int(input("\n[-] Enter the maximum length of the password: "))  # طلب إدخال الحد الأقصى لطول كلمة المرور

    use_digits = input("\n[-] Use digits? (y/n): ").lower() == 'y'  # طلب إدخال استخدام الأرقام
    use_symbols = input("\n[-] Use symbols? (y/n): ").lower() == 'y'  # طلب إدخال استخدام الرموز
    use_letters = input("\n[-] Use letters? (y/n): ").lower() == 'y'  # طلب إدخال استخدام الأحرف

    brute_force(file_path, file_type, min_length, max_length, use_digits, use_symbols, use_letters)  # بدء هجوم القاموس على الملف

if __name__ == "__main__":
    main()


# V.00.2.3v
# by : Mohammed Alaa Mohammed [ developer ]
