import instaloader
import json
import os
from tqdm import tqdm
import time
from datetime import datetime
from pystyle import *

# إنشاء كائن Instaloader
L = instaloader.Instaloader()

# Logo of a Tool set one ...✓→⇲
print("""
\33[31;1m▄︻デ══━一💥\33[39;0m @Developer Mohammed Alaa   \33[32;1m▄︻デ══━ 一💥\33[39;0m
\33[33;1m▄︻デ══━一💥\33[39;0m @Developer Mohammed Alaa   \33[34;1m▄︻デ══━ 一💥\33[39;0m
\33[36;1m▄︻デ══━一💥\33[39;0m @Developer Mohammed Alaa   \33[35;1m▄︻デ══━ 一💥\33[39;0m
\n\33[31;1m▄▄︻┻┳═══════════════════════════一 𖦏 💨💨💨\33[39;0m
""")


# عرض قائمة الخيارات للمستخدم
def display_menu():
    print("\n\33[36;1mOptions:\33[39;0m")
    print("1 - Download profile information")
    print("2 - Download profile picture")
    print("3 - Download recent posts")
    print("4 - Download all information (Profile Info, Picture, Posts)")
    print("0 - Exit\n")


Write.Print("Developer ::| Mohammed Alaa Mohammed.\n", Colors.cyan_to_green, interval=.02)
Write.Print("\nGithub ::| https://www.github.com/DARKGITHUBPRO/.\n\n", Colors.green_to_yellow, interval=.02)


# اختيار المستخدم
def user_choice():
    while True:
        try:
            choice = int(input("\nEnter your choice (1/2/3/4/0): "))
            if choice in [1, 2, 3, 4, 0]:
                return choice
            else:
                print("\n\33[31;1mInvalid option, please choose 1, 2, 3, 4 or 0.\33[39;0m")
        except ValueError:
            print("\n\33[31;1mInvalid input, please enter a number.\33[39;0m")


# عرض شريط التقدم
def show_progress():
    for i in tqdm(range(100), "\33[0032;1mProcessing...\33[39m", unit="\33[36;1m steps\33[39;002m"):
        time.sleep(0.01)


# تسجيل عملية التحميل في ملف نصي
def log_download(action, username):
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    with open("download_schedule_log.txt", "a") as log_file:
        log_file.write(f"[{timestamp}] {action} for user: {username}\n")


# تحميل المعلومات الشخصية
def download_profile_info(username):
    profile = instaloader.Profile.from_username(L.context, username)

    profile_info = {
        "Username": profile.username,
        "Full Name": profile.full_name,
        "Bio": profile.biography,
        "Followers": profile.followers,
        "Following": profile.followees,
        "Number of Posts": profile.mediacount,
        "Profile Picture URL": profile.profile_pic_url,
        "Recent Posts": []
    }

    # جلب آخر 10 منشورات
    for post in profile.get_posts():
        if len(profile_info["Recent Posts"]) >= 10:
            break
        profile_info["Recent Posts"].append({
            "Post URL": f"https://www.instagram.com/p/{post.shortcode}/",
            "Caption": post.caption,
            "Likes": post.likes,
            "Comments": post.comments
        })

    # حفظ المعلومات في ملف JSON
    with open(f"{username}_profile_info.json", "w", encoding='utf-8') as json_file:
        json.dump(profile_info, json_file, indent=4, ensure_ascii=False)

    log_download("Profile information downloaded", username)
    print(f"\n\33[35;1mProfile information saved as {username}_profile_info.json\33[39;0m")


# تحميل صورة الملف الشخصي
def download_profile_pic(username):
    profile = instaloader.Profile.from_username(L.context, username)
    L.download_profile(username, profile_pic_only=True)

    log_download("Profile picture downloaded", username)
    print(f"\n\33[36;1mProfile picture for {username} downloaded.\33[39;0m")


# تحميل المنشورات الأخيرة
def download_recent_posts(username):
    profile = instaloader.Profile.from_username(L.context, username)
    posts_dir = f"\n{username}_recent_posts"
    os.makedirs(posts_dir, exist_ok=True)

    count = 0
    for post in profile.get_posts():
        if count >= 5:  # تحميل آخر 5 منشورات
            break
        L.download_post(post, target=posts_dir)
        count += 1

    log_download("Recent posts downloaded", username)
    print(f"\n\33[36;1mLast 5 posts downloaded to {posts_dir}.\33[39;0m")


# تحميل جميع المعلومات (المعلومات الشخصية + صورة الملف الشخصي + المنشورات)
def download_all_info(username):
    show_progress()
    download_profile_info(username)
    download_profile_pic(username)
    download_recent_posts(username)


# الوظيفة الرئيسية
def main():
    username = input('\33[33;1mEnter the Instagram username: \33[39;0m').lower()

    while True:
        display_menu()
        choice = user_choice()

        if choice == 1:
            show_progress()
            download_profile_info(username)
        elif choice == 2:
            show_progress()
            download_profile_pic(username)
        elif choice == 3:
            show_progress()
            download_recent_posts(username)
        elif choice == 4:
            show_progress()
            download_all_info(username)
        elif choice == 0:
            print("\n\33[31;1mExiting...\33[39;0m\n")
            break


# تشغيل البرنامج
if __name__ == "__main__":
    main()

# developer ::| Mohammed Alaa Mohammed
# V.4.0.0
# name of tool ==:| Instagram Tool
