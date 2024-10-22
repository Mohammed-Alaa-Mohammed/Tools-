import zipfile
import rarfile
import os
import itertools
import string
import time
import threading
from pystyle import *

Write.Print("""
 ________    ______ .______          ___       ______  __  ___  __  .__   __.   _______ 
|       /   /      ||   _  \        /   \     /      ||  |/  / |  | |  \ |  |  /  _____|
`---/  /   |  ,----'|  |_)  |      /  ^  \   |  ,----'|  '  /  |  | |   \|  | |  |  __  
   /  /    |  |     |      /      /  /_\  \  |  |     |    <   |  | |  . `  | |  | |_ | 
  /  /----.|  `----.|  |\  \----./  _____  \ |  `----.|  .  \  |  | |  |\   | |  |__| | 
 /________| \______|| _| `._____/__/     \__\ \______||__|\__\ |__| |__| \__|  \______|                                                                                          

                                                                                INFO.. [
                                                                                        ✮✮ V0.2.3.3v          Follower 12
                                                                                        ✮✮ Followers : 45     Likes : 205 
                                                                                        ✮✮ Views : 115         Downloads or Useed Tool.. : 86 Done 
                                                                                        ✮✮ Tools : 15         Versions of This Tool : 6 .T.v
                                                                                        ✮✮ Last Update : 2024 - 10 - 22
                                                                                        [-] Created By : Mohammed Alaa Mohammed
                                                                                         ]
""", Colors.blue_to_white, interval=.001)

Write.Print('\n[-] Message : It may take a while to fetch the password for Your file.\n', Colors.green_to_cyan,
            interval=0.030)
Write.Print('\n[-] GitHub : https://www.github.com/DARKGITHUBPRO\n', Colors.red_to_yellow, interval=0.020)


# دالة لفك ضغط ملفات zip باستخدام كلمة المرور
def extract_zip(file_path, password):
    try:
        with zipfile.ZipFile(file_path) as zf:
            zf.extractall(pwd=password.encode())  # محاولة استخراج الملفات باستخدام كلمة المرور
        return True
    except Exception as e:
        return False


# دالة لفك ضغط ملفات rar باستخدام كلمة المرور
def extract_rar(file_path, password):
    try:
        with rarfile.RarFile(file_path) as rf:
            rf.extractall(pwd=password)  # محاولة استخراج الملفات باستخدام كلمة المرور
        return True
    except Exception as e:
        return False


# دالة لتنفيذ هجوم القاموس باستخدام الخيوط
def brute_force(file_path, file_type, min_length, max_length, use_digits, use_even_digits, use_odd_digits, use_symbols,
                use_letters, num_threads):
    chars = ''
    if use_digits:
        chars += string.digits
    if use_even_digits:
        chars += '2468121416'  # أرقام زوجية فقط
    if use_odd_digits:
        chars += '12345678910'  # أرقام فردية فقط
    if use_symbols:
        chars += string.punctuation
    if use_letters:
        chars += string.ascii_letters

    # إضافة الأرقام من 12345678 إلى قائمة كلمات المرور
    predefined_passwords = ['12345678']  # إضافة كلمات المرور المعروفة

    attempts = 0
    start_time = time.time()
    password_found = [False]  # لمشاركة الحالة بين الخيوط

    def worker(passwords):
        nonlocal attempts
        for password in passwords:
            if password_found[0]:
                return
            attempts += 1
            print(f"\n\33[33;1m[-] Trying password:\33[39;0m {password} (Attempt: {attempts})")
            if file_type == 'zip' and extract_zip(file_path, password):
                print("\nPassword found:", password)
                password_found[0] = True
                return
            elif file_type == 'rar' and extract_rar(file_path, password):
                print("\nPassword found:", password)
                password_found[0] = True
                return

    # تجربة كلمات المرور المحددة أولاً
    for password in predefined_passwords:
        attempts += 1
        print(f"\n\33[33;1m[-] Trying predefined password:\33[39;0m {password} (Attempt: {attempts})")
        if file_type == 'zip' and extract_zip(file_path, password):
            print("\nPassword found:", password)
            print(f"\nPassword found in {time.time() - start_time} seconds.")
            return
        elif file_type == 'rar' and extract_rar(file_path, password):
            print("\nPassword found:", password)
            print(f"\nPassword found in {time.time() - start_time} seconds.")
            return

    # تقسيم كلمات المرور إلى أجزاء على حسب عدد الخيوط
    all_passwords = [''.join(p) for length in range(min_length, max_length + 1) for p in
                     itertools.product(chars, repeat=length)]
    chunk_size = len(all_passwords) // num_threads
    threads = []

    for i in range(num_threads):
        start_index = i * chunk_size
        end_index = (i + 1) * chunk_size if i != num_threads - 1 else len(all_passwords)
        thread = threading.Thread(target=worker, args=(all_passwords[start_index:end_index],))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    if password_found[0]:
        print(f"\nPassword found in {end_time - start_time} seconds.")
    else:
        print("\n[❌] Password not found.")
    print(f"\nTotal attempts: {attempts}")

    # تصدير النتائج إلى ملف نصي
    with open("brute_force_results.txt", "w") as f:
        f.write(f"File: {file_path}\n")
        f.write(f"Time taken: {end_time - start_time} seconds\n")
        f.write(f"Total attempts: {attempts}\n")
        f.write(f"Password found: {'Yes' if password_found[0] else 'No'}\n")


# الدالة الرئيسية للبرنامج
def main():
    file_path = input(
        "\n[-] Enter the path of the file (e.g., C:/files/archive.zip): ")  # طلب إدخال مسار الملف من المستخدم
    if not os.path.isfile(file_path):
        print("\n[❌]\33[31;1m File does not exist. Please enter a valid file path.\33[39;0m")
        return

    file_type = os.path.splitext(file_path)[1][1:].lower()  # استخراج نوع الملف من الامتداد
    if file_type not in ['zip', 'rar']:
        print("\n\33[31;1m[❌] Unsupported file type. Please enter a zip or rar file.\33[39;0m")
        return

    min_length = int(
        input("\n[-] Enter the minimum length of the password: "))  # طلب إدخال الحد الأدنى لطول كلمة المرور
    max_length = int(
        input("\n[-] Enter the maximum length of the password: "))  # طلب إدخال الحد الأقصى لطول كلمة المرور
    use_digits = input("\n[-] Use all digits? (y/n): ").lower() == 'y'  # طلب إدخال استخدام الأرقام كاملة
    use_even_digits = input("\n[-] Use even digits only? (y/n): ").lower() == 'y'  # طلب إدخال استخدام الأرقام الزوجية
    use_odd_digits = input("\n[-] Use odd digits only? (y/n): ").lower() == 'y'  # طلب إدخال استخدام الأرقام الفردية
    use_symbols = input("\n[-] Use symbols? (y/n): ").lower() == 'y'  # طلب إدخال استخدام الرموز
    use_letters = input("\n[-] Use letters? (y/n): ").lower() == 'y'  # طلب إدخال استخدام الأحرف
    num_threads = int(input("\n[-] Enter number of threads to use (e.g., 4): "))  # إدخال عدد الخيوط

    brute_force(file_path, file_type, min_length, max_length, use_digits, use_even_digits, use_odd_digits, use_symbols,
                use_letters, num_threads)


if __name__ == "__main__":
    main()
# Last Update
# Mohammed Alaa 
