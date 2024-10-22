import zipfile
import rarfile
import os
import itertools
import string
import time
import threading
import argparse
import py7zr
from pystyle import *

Write.Print("""
 ________    ______ .______          ___       ______  __  ___  __  .__   __.   _______ 
|       /   /      ||   _  \        /   \     /      ||  |/  / |  | |  \ |  |  /  _____|
`---/  /   |  ,----'|  |_)  |      /  ^  \   |  ,----'|  '  /  |  | |   \|  | |  |  __  
   /  /    |  |     |      /      /  /_\  \  |  |     |    <   |  | |  . `  | |  | |_ | 
  /  /----.|  `----.|  |\  \----./  _____  \ |  `----.|  .  \  |  | |  |\   | |  |__| | 
 /________| \______|| _| `._____/__/     \__\ \______||__|\__\ |__| |__| \__|  \______|                                                                                          
  INFO.. [
                                                                                            ✮✮ V0.3.3.4v          Follower 12
                                                                                            ✮✮ Followers : 45     Likes : 90
                                                                                            ✮✮ Views : 109         Downloads or Useed Tool.. : 45 Done
                                                                                            ✮✮ Tools : 17         Versions of This Tool : 6 .T.v
                                                                                            ✮✮ Update Of : 2024 / 10 / 22
                                                                                            ✮✮ Last Update : 2024 / 10 / 22 of V0.3.3.4
                                                                                            [-] Created By : Mohammed Alaa Mohammed
                                                                                                ]
""", Colors.blue_to_cyan, interval=.001)

Write.Print('\n[-] Message : It may take a while to fetch the password for Your file.\n', Colors.green_to_cyan, interval=0.030)
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


# دالة لفك ضغط ملفات 7z باستخدام كلمة المرور
def extract_7z(file_path, password):
    try:
        with py7zr.SevenZipFile(file_path, mode='r', password=password) as z:
            z.extractall()  # محاولة استخراج الملفات باستخدام كلمة المرور
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
        chars += '02468'  # أرقام زوجية فقط
    if use_odd_digits:
        chars += '13579'  # أرقام فردية فقط
    if use_symbols:
        chars += string.punctuation
    if use_letters:
        chars += string.ascii_letters

    attempts = 0
    start_time = time.time()
    password_found = [False]  # لمشاركة الحالة بين الخيوط

    def worker(passwords):
        nonlocal attempts
        for password in passwords:
            if password_found[0]:
                return
            attempts += 1
            print(f"\33[33;1m[-] Trying password:\33[39;0m {password} (Attempt: {attempts})")
            if file_type == 'zip' and extract_zip(file_path, password):
                print("Password found:", password)
                password_found[0] = True
                return
            elif file_type == 'rar' and extract_rar(file_path, password):
                print("Password found:", password)
                password_found[0] = True
                return
            elif file_type == '7z' and extract_7z(file_path, password):
                print("Password found:", password)
                password_found[0] = True
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
        print(f"Password found in {end_time - start_time} seconds.")
    else:
        print("[❌] Password not found.")
    print(f"Total attempts: {attempts}")

    # تصدير النتائج إلى ملف نصي
    with open("brute_force_results.txt", "w") as f:
        f.write(f"File: {file_path}\n")
        f.write(f"Time taken: {end_time - start_time} seconds\n")
        f.write(f"Total attempts: {attempts}\n")
        f.write(f"Password found: {'Yes' if password_found[0] else 'No'}\n")


# الدالة الرئيسية للبرنامج
def main():
    parser = argparse.ArgumentParser(description="Brute force password recovery for zip, rar, and 7z files.")
    parser.add_argument("file_path", help="Path to the encrypted file.")
    parser.add_argument("min_length", type=int, help="Minimum length of the password.")
    parser.add_argument("max_length", type=int, help="Maximum length of the password.")
    parser.add_argument("--use_digits", action="store_true", help="Use all digits.")
    parser.add_argument("--use_even_digits", action="store_true", help="Use even digits only.")
    parser.add_argument("--use_odd_digits", action="store_true", help="Use odd digits only.")
    parser.add_argument("--use_symbols", action="store_true", help="Use symbols.")
    parser.add_argument("--use_letters", action="store_true", help="Use letters.")
    parser.add_argument("--num_threads", type=int, default=4, help="Number of threads to use.")

    args = parser.parse_args()

    if not os.path.isfile(args.file_path):
        print("\n[❌]\33[31;1m File does not exist. Please enter a valid file path.\33[39;0m")
        return

    file_type = os.path.splitext(args.file_path)[1][1:].lower()  # استخراج نوع الملف من الامتداد
    if file_type not in ['zip', 'rar', '7z']:
        print("\33[31;1m[❌] Unsupported file type. Please enter a zip, rar, or 7z file.\33[39;0m")
        return

    brute_force(args.file_path, file_type, args.min_length, args.max_length, args.use_digits,
                args.use_even_digits, args.use_odd_digits, args.use_symbols, args.use_letters, args.num_threads)


if __name__ == "__main__":
    main()

# python brute_force.py <path_to_file> <min_length> <max_length> --use_digits --use_even_digits --num_threads 4

# v.3.4.5T
# Mohammed Alaa Mohammed
